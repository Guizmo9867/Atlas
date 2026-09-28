// Transforme le corpus en couches GeoJSON pour UNE date donnée.
// Rien n'est stocké « par date » : la carte est toujours recalculée à partir des états valides ce jour-là.
import type { Feature, FeatureCollection, Geometry, Position } from 'geojson'
import type { Entite, Evenement, ModeLecture } from '../types'
import { etatActif, phaseEvenement } from './temporal'
import { couleurPour, HACHURE_NEUTRE, LISERES } from '../theme/palettes'

const vide = (): FeatureCollection => ({ type: 'FeatureCollection', features: [] })

export interface CouchesDuJour {
  territoires: FeatureCollection
  frontieres: FeatureCollection
  ponts: FeatureCollection
  pastilles: FeatureCollection
  parcours: FeatureCollection
  sansGeometrie: string[]
}

export function construireCouches(
  entites: Entite[],
  evenements: Evenement[],
  date: string,
  mode: ModeLecture,
  geometries: Record<string, Geometry> = {},
): CouchesDuJour {
  const c: CouchesDuJour = { territoires: vide(), frontieres: vide(), ponts: vide(), pastilles: vide(), parcours: vide(), sansGeometrie: [] }

  // Les territoires « parents » d'abord, les « enfants » (parent_id) par-dessus
  const actifs = new Map(entites.map((e) => [e.entite_id, etatActif(e, date)]))
  const profondeur = (id: string, n = 0): number => {
    const pid = actifs.get(id)?.proprietes?.parent_id
    return pid && n < 10 ? profondeur(pid, n + 1) : n
  }
  const ordonnees = [...entites].sort((a, b) => profondeur(a.entite_id) - profondeur(b.entite_id))

  for (const ent of ordonnees) {
    const etat = actifs.get(ent.entite_id)
    if (!etat) continue
    const geom = etat.geometrie ?? (etat.geometrie_ref ? geometries[etat.geometrie_ref] : undefined)
    if (!geom) { c.sansGeometrie.push(ent.entite_id); continue }
    const p = etat.proprietes ?? {}
    const parent = p.parent_id ? actifs.get(p.parent_id)?.proprietes : undefined
    // Alignement : un « enfant » sans valeur hérite de celle de son parent (ex. Courlande → Lettonie).
    // Pas d'héritage pour la souveraineté : une souveraineté absente = volontairement non tranchée.
    const heriter = (id: string | undefined, n = 0): string => {
      if (!id || n > 10) return ''
      const pp = actifs.get(id)?.proprietes
      return pp?.alignement_id ?? heriter(pp?.parent_id, n + 1)
    }
    const valeurMode = p[`${mode}_id`] ?? (mode === 'alignement' ? heriter(p.parent_id) : '')
    // Contrôle concurrent : le contrôleur diffère du souverain (ou, sans souverain déclaré, du contrôleur du parent)
    const reference = p.souverainete_id ?? parent?.controle_id
    const concurrent = !!(p.controle_id && reference && p.controle_id !== reference)
    const f: Feature = {
      type: 'Feature',
      geometry: geom,
      properties: {
        entite_id: ent.entite_id, nom: ent.nom, nom_court: ent.nom_court ?? ent.nom.replace(' (FICTIF)', ''), etat_id: etat.etat_id, statut: etat.statut,
        valeur_mode: valeurMode, couleur: couleurPour(mode, valeurMode), profondeur: profondeur(ent.entite_id),
        type: ent.type_entite,
        // Occupation / contrôle concurrent = HACHURES par-dessus la couleur de fond (jamais une nouvelle couleur).
        // Mode souveraineté : hachures à la couleur de l'occupant. Mode alignements : hachures sombres. Mode contrôle : rien (le fond montre déjà l'occupant).
        hachure: mode !== 'controle' && concurrent
          ? `hachure-${(mode === 'souverainete' ? couleurPour('controle', p.controle_id) : HACHURE_NEUTRE).slice(1)}` : '',
        lisere: mode === 'alignement' ? (LISERES[valeurMode] ?? '') : '',
      },
    }
    if (ent.type_entite === 'territoire') c.territoires.features.push(f)
    else if (ent.type_entite === 'frontiere' || ent.type_entite === 'ligne_front') c.frontieres.features.push(f)
    else if (ent.type_entite === 'pont') c.ponts.features.push(f)
  }

  for (const ev of evenements) {
    const phase = phaseEvenement(ev, date)
    if (phase === 'futur') continue
    const g = ev.geographie.geometrie ?? (ev.geographie.geometrie_ref ? geometries[ev.geographie.geometrie_ref] : undefined)
    if (!g) continue
    const props = {
      id: ev.id, titre: ev.titre, phase, profondeur: ev.profondeur_affichage,
      categorie: ev.categories[0] ?? 'autre', couleur: couleurPour('categorie', ev.categories[0] ?? 'autre'),
    }
    c.pastilles.features.push({ type: 'Feature', geometry: { type: 'Point', coordinates: pointRepresentatif(g) }, properties: props })
    if ((ev.geographie.type === 'parcours' || ev.geographie.type === 'corridor') && g.type.includes('LineString')) {
      c.parcours.features.push({ type: 'Feature', geometry: g, properties: props })
    }
  }
  return c
}

/** Où poser la pastille : le point lui-même, le milieu d'une ligne, le centre d'une zone. */
export function pointRepresentatif(g: Geometry): Position {
  const pts: Position[] = []
  const collecter = (x: unknown): void => {
    if (Array.isArray(x) && typeof x[0] === 'number') pts.push(x as Position)
    else if (Array.isArray(x)) x.forEach(collecter)
  }
  if (g.type === 'GeometryCollection') g.geometries.forEach((sg) => collecter((sg as { coordinates: unknown }).coordinates))
  else collecter(g.coordinates)
  if (g.type === 'Point') return g.coordinates
  if (g.type === 'LineString') return g.coordinates[Math.floor(g.coordinates.length / 2)]
  if (g.type === 'MultiPolygon') {
    // le plus grand morceau (en nombre de points), pour ne pas poser l'étiquette en mer
    const principal = [...g.coordinates].sort((a, b) => b[0].length - a[0].length)[0]
    return pointRepresentatif({ type: 'Polygon', coordinates: principal })
  }
  if (g.type === 'Polygon') {
    // centre du rectangle englobant (boucle simple : les anneaux réels ont des centaines de milliers de points)
    let [x0, y0, x1, y1] = [Infinity, Infinity, -Infinity, -Infinity]
    for (const [x, y] of g.coordinates[0]) { if (x < x0) x0 = x; if (x > x1) x1 = x; if (y < y0) y0 = y; if (y > y1) y1 = y }
    return [(x0 + x1) / 2, (y0 + y1) / 2]
  }
  const n = pts.length || 1
  return [pts.reduce((s, p) => s + p[0], 0) / n, pts.reduce((s, p) => s + p[1], 0) / n]
}
