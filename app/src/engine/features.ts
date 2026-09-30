// Transforme le corpus en couches GeoJSON pour UNE date donnée.
// Rien n'est stocké « par date » : la carte est toujours recalculée à partir des états valides ce jour-là.
import type { Feature, FeatureCollection, Geometry, Position } from 'geojson'
import type { Entite, Evenement, ModeLecture } from '../types'
import { etatActif, phaseEvenement } from './temporal'
import { CAMP_HORS_CORPUS, couleurPour, HACHURE_CLAIRE, HACHURE_NEUTRE, HACHURE_NON_TRANCHE, LISERES } from '../theme/palettes'

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
  // Camp de chaque acteur ce jour-là, lu dans les données : l'alignement du territoire « racine » dont il est souverain
  // Sert à colorer les hachures d'occupation en mode Alignements.
  // (le territoire dont il est souverain, sans parent ; ex. hongrie → axis_associe_ww2, royaume_uni → allies_ww2)
  // Territoires presque entièrement couverts (≥ 90 %) par leurs zones « enfants » ce jour-là :
  // de près, leur étiquette s'efface au profit de celles des zones (Italie → Italie du Nord / Italie libérée)
  const geomDe = (id: string) => { const et = actifs.get(id); return et?.geometrie ?? (et?.geometrie_ref ? geometries[et.geometrie_ref] : undefined) }
  const couvert = new Map<string, number>()
  for (const e of entites) {
    const pid = actifs.get(e.entite_id)?.proprietes?.parent_id; const g = geomDe(e.entite_id)
    if (pid && g) couvert.set(pid, (couvert.get(pid) ?? 0) + aireGeometrie(g))
  }
  const aDesEnfants = new Set<string>()
  for (const [pid, a] of couvert) { const g = geomDe(pid); if (g && a >= 0.9 * aireGeometrie(g)) aDesEnfants.add(pid) }
  const campActeur = new Map<string, string>()
  for (const e of entites) {
    const pp = actifs.get(e.entite_id)?.proprietes
    if (pp && !pp.parent_id && pp.alignement_id && pp.souverainete_id && !campActeur.has(pp.souverainete_id)) campActeur.set(pp.souverainete_id, pp.alignement_id)
  }

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
        valeur_mode: valeurMode, couleur: couleurPour(mode, valeurMode), profondeur: profondeur(ent.entite_id), a_enfants: aDesEnfants.has(ent.entite_id),
        type: ent.type_entite,
        // Occupation / contrôle concurrent = HACHURES par-dessus la couleur de fond (jamais une nouvelle couleur).
        // Mode souveraineté : hachures à la couleur de l'occupant. Mode alignements : à la couleur du camp de l'occupant.
        // Mode contrôle : rien (le fond montre déjà l'occupant).
        hachure: mode !== 'controle' && concurrent ? `hachure-${couleurHachure(mode, p.controle_id, valeurMode, campActeur).slice(1)}`
          // souverain connu mais contrôle réel non tranché (champ absent) : rayures croisées grises (ex. Grèce des Dekemvriana)
          : p.souverainete_id && !p.controle_id && ent.type_entite === 'territoire' ? `croise-${HACHURE_NON_TRANCHE.slice(1)}` : '',
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

/** Couleur des hachures d'occupation. Si elle se confond avec le fond (même camp), rayures claires. */
function couleurHachure(mode: ModeLecture, controle: string, fond: string, campActeur: Map<string, string>): string {
  if (mode === 'souverainete') return couleurPour('controle', controle)
  const camp = campActeur.get(controle) ?? CAMP_HORS_CORPUS[controle]
  if (!camp) return HACHURE_NEUTRE
  const c = couleurPour('alignement', camp)
  return c === couleurPour('alignement', fond) ? (c === HACHURE_CLAIRE ? HACHURE_NEUTRE : HACHURE_CLAIRE) : c
}

/** Où poser la pastille ou l'étiquette : le point lui-même, le milieu d'une ligne, le « cœur » d'une zone.
 *  Mis en cache par géométrie : le calcul n'est fait qu'une fois, pas à chaque changement de date. */
const cachePoints = new WeakMap<object, Position>()
export function pointRepresentatif(g: Geometry): Position {
  const deja = cachePoints.get(g)
  if (deja) return deja
  const p = calculerPoint(g)
  cachePoints.set(g, p)
  return p
}
function calculerPoint(g: Geometry): Position {
  if (g.type === 'Point') return g.coordinates
  if (g.type === 'LineString') return g.coordinates[Math.floor(g.coordinates.length / 2)]
  if (g.type === 'MultiPolygon') {
    // le plus grand morceau (en surface), pour ne pas poser l'étiquette sur un îlot
    const principal = [...g.coordinates].sort((a, b) => Math.abs(aire(allege(b[0]))) - Math.abs(aire(allege(a[0]))))[0]
    return poleInaccessibilite(principal.map(allege))
  }
  if (g.type === 'Polygon') return poleInaccessibilite(g.coordinates.map(allege))
  const pts: Position[] = []
  const collecter = (x: unknown): void => {
    if (Array.isArray(x) && typeof x[0] === 'number') pts.push(x as Position)
    else if (Array.isArray(x)) x.forEach(collecter)
  }
  if (g.type === 'GeometryCollection') g.geometries.forEach((sg) => collecter((sg as { coordinates: unknown }).coordinates))
  else collecter(g.coordinates)
  const n = pts.length || 1
  return [pts.reduce((s, p) => s + p[0], 0) / n, pts.reduce((s, p) => s + p[1], 0) / n]
}

/** Aire approximative (degrés², anneaux allégés) : sert seulement à comparer un territoire à ses zones. Mise en cache. */
const cacheAires = new WeakMap<object, number>()
function aireGeometrie(g: Geometry): number {
  const deja = cacheAires.get(g)
  if (deja !== undefined) return deja
  const polys = g.type === 'Polygon' ? [g.coordinates] : g.type === 'MultiPolygon' ? g.coordinates : []
  let a = 0
  for (const p of polys) p.forEach((r, i) => { a += (i === 0 ? 1 : -1) * Math.abs(aire(allege(r))) })
  cacheAires.set(g, a)
  return a
}

/** Anneau allégé (≤ 400 points) : suffisant pour placer une étiquette, sans parcourir des centaines de milliers de points. */
function allege(r: Position[]): Position[] {
  const pas = Math.max(1, Math.ceil(r.length / 400))
  if (pas === 1) return r
  const out: Position[] = []
  for (let i = 0; i < r.length; i += pas) out.push(r[i])
  out.push(r[0])
  return out
}
function aire(r: Position[]): number {
  let a = 0
  for (let i = 0, j = r.length - 1; i < r.length; j = i++) a += (r[j][0] - r[i][0]) * (r[j][1] + r[i][1])
  return a / 2
}
/** Distance signée d'un point au bord du polygone (positive à l'intérieur). */
function distanceBord(x: number, y: number, anneaux: Position[][]): number {
  let dedans = false, min = Infinity
  for (const r of anneaux) {
    for (let i = 0, j = r.length - 1; i < r.length; j = i++) {
      const [ax, ay] = r[i], [bx, by] = r[j]
      if ((ay > y) !== (by > y) && x < ((bx - ax) * (y - ay)) / (by - ay) + ax) dedans = !dedans
      const dx = bx - ax, dy = by - ay, l = dx * dx + dy * dy
      let t = l ? ((x - ax) * dx + (y - ay) * dy) / l : 0
      t = Math.max(0, Math.min(1, t))
      const ex = ax + t * dx - x, ey = ay + t * dy - y, d = ex * ex + ey * ey
      if (d < min) min = d
    }
  }
  return (dedans ? 1 : -1) * Math.sqrt(min)
}
/** « Pôle d'inaccessibilité » (algorithme polylabel) : le point le plus éloigné des bords, là où l'étiquette tient le mieux.
 *  Évite par exemple de poser « Norvège » au milieu de la Suède (centre du rectangle englobant). */
function poleInaccessibilite(anneaux: Position[][]): Position {
  let [x0, y0, x1, y1] = [Infinity, Infinity, -Infinity, -Infinity]
  for (const [x, y] of anneaux[0]) { if (x < x0) x0 = x; if (x > x1) x1 = x; if (y < y0) y0 = y; if (y > y1) y1 = y }
  const taille = Math.min(x1 - x0, y1 - y0)
  if (!taille) return [x0, y0]
  const precision = taille / 60
  type Cellule = { x: number; y: number; h: number; d: number; max: number }
  const cellule = (x: number, y: number, h: number): Cellule => { const d = distanceBord(x, y, anneaux); return { x, y, h, d, max: d + h * Math.SQRT2 } }
  // file de priorité (tas binaire) : la cellule la plus prometteuse d'abord
  const tas: Cellule[] = []
  const pousser = (c: Cellule) => {
    tas.push(c); let i = tas.length - 1
    while (i > 0) { const p = (i - 1) >> 1; if (tas[p].max >= tas[i].max) break; [tas[p], tas[i]] = [tas[i], tas[p]]; i = p }
  }
  const tirer = (): Cellule => {
    const haut = tas[0], dernier = tas.pop()!
    if (tas.length) {
      tas[0] = dernier; let i = 0
      for (;;) {
        const g = 2 * i + 1, d = g + 1; let m = i
        if (g < tas.length && tas[g].max > tas[m].max) m = g
        if (d < tas.length && tas[d].max > tas[m].max) m = d
        if (m === i) break
        ;[tas[m], tas[i]] = [tas[i], tas[m]]; i = m
      }
    }
    return haut
  }
  let h = taille / 2
  for (let x = x0; x < x1; x += taille) for (let y = y0; y < y1; y += taille) pousser(cellule(x + h, y + h, h))
  let best = cellule((x0 + x1) / 2, (y0 + y1) / 2, 0)
  let n = 0
  while (tas.length && n++ < 400) {
    const c = tirer()
    if (c.d > best.d) best = c
    if (c.max - best.d <= precision) continue
    h = c.h / 2
    pousser(cellule(c.x - h, c.y - h, h)); pousser(cellule(c.x + h, c.y - h, h)); pousser(cellule(c.x - h, c.y + h, h)); pousser(cellule(c.x + h, c.y + h, h))
  }
  return [best.x, best.y]
}
