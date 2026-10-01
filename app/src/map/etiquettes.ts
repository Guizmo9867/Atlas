import type * as maplibregl from 'maplibre-gl'
import type { Geometry, Position } from 'geojson'

/**
 * Taille des noms de territoires selon le zoom (demande de Guizmo, 01/10/2026) :
 * un nom ne s'affiche que s'il tient, lisible, À L'INTÉRIEUR de son territoire, à la taille la plus grande possible
 * (plafonnée selon le zoom). S'il ne tient pas, il apparaîtra à un zoom suivant. Ensuite, deux noms qui se
 * chevaucheraient : le plus grand gagne.
 */

const TAILLE_MIN = 9 // px : en dessous, illisible → le nom attend un zoom suivant
const tailleMax = (z: number) => Math.min(20, 12 + 1.5 * z)
const MARGE = 0.9 // le nom occupe au plus 90 % de l'espace disponible
const HAUTEUR_LIGNE = 1.15

export interface Place {
  el: HTMLElement
  point: Position
  demiLargeur: number // degrés de longitude libres de part et d'autre du point (dans le territoire)
  demiHauteur: number // idem en hauteur, en unités Mercator (0..1 pour le monde entier)
  largeur16: number // largeur du nom écrit en 16 px
  largeurSous11: number // largeur du sous-titre écrit en 11 px (0 s'il n'y en a pas)
  profondeur: number
  parent: boolean
}

/** Nom de ville déjà posé sur la carte (prioritaire : les noms de pays l'évitent). */
export interface Obstacle { point: Position; largeur: number; seuil: number }

let ctx: CanvasRenderingContext2D | null = null
function mesurer(texte: string, police: string, espacementEm = 0, taille = 16): number {
  ctx ??= document.createElement('canvas').getContext('2d')
  if (!ctx) return texte.length * taille * 0.7
  ctx.font = police
  return ctx.measureText(texte).width + texte.length * espacementEm * taille
}
export const largeurNom = (nom: string) => mesurer(nom.toUpperCase(), 'bold 16px Georgia, serif', 0.12)
export const largeurVille = (nom: string, importance: string) =>
  mesurer(nom, importance === 'A' ? 'bold 13px Georgia, serif' : importance === 'B' ? '12px Georgia, serif' : '11px Georgia, serif')
export const largeurSousTitre = (t: string) => (t ? mesurer(t, '11px system-ui, sans-serif', 0, 11) : 0)

const mercY = (lat: number) => (1 - Math.log(Math.tan(Math.PI / 4 + (Math.max(-85, Math.min(85, lat)) * Math.PI) / 360)) / Math.PI) / 2

/**
 * Où poser le nom et quelle place il a : on part du point le plus « intérieur » du territoire, on glisse le nom au milieu
 * du segment horizontal qui traverse le territoire à cette hauteur (toute la largeur est utilisable), puis on mesure la
 * hauteur libre à cet endroit.
 */
export function espaceLibre(g: Geometry, p: Position): { point: Position; demiLargeur: number; demiHauteur: number } {
  const rien = { point: p, demiLargeur: 0, demiHauteur: 0 }
  const polygones = g.type === 'Polygon' ? [g.coordinates] : g.type === 'MultiPolygon' ? g.coordinates : []
  const [px, py] = p
  const contient = (anneaux: Position[][]) => { // règle pair-impair
    let dedans = false
    for (const a of anneaux) for (let i = 0, j = a.length - 1; i < a.length; j = i++) {
      const [xi, yi] = a[i], [xj, yj] = a[j]
      if ((yi > py) !== (yj > py) && px < xj + ((py - yj) * (xi - xj)) / (yi - yj)) dedans = !dedans
    }
    return dedans
  }
  const morceau = polygones.find(contient)
  if (!morceau) return rien
  let gauche = -Infinity, droite = Infinity
  for (const a of morceau) for (let i = 0, j = a.length - 1; i < a.length; j = i++) {
    const [xi, yi] = a[i], [xj, yj] = a[j]
    if ((yi > py) !== (yj > py)) {
      const x = xj + ((py - yj) * (xi - xj)) / (yi - yj)
      if (x < px) gauche = Math.max(gauche, x); else droite = Math.min(droite, x)
    }
  }
  if (!isFinite(gauche) || !isFinite(droite)) return rien
  const cx = (gauche + droite) / 2
  let haut = Infinity, bas = -Infinity
  for (const a of morceau) for (let i = 0, j = a.length - 1; i < a.length; j = i++) {
    const [xi, yi] = a[i], [xj, yj] = a[j]
    if ((xi > cx) !== (xj > cx)) {
      const y = yj + ((cx - xj) * (yi - yj)) / (xi - xj)
      if (y > py) haut = Math.min(haut, y); else bas = Math.max(bas, y)
    }
  }
  if (!isFinite(haut) || !isFinite(bas)) return rien
  return {
    point: [cx, py],
    demiLargeur: (droite - gauche) / 2,
    demiHauteur: Math.min(mercY(py) - mercY(haut), mercY(bas) - mercY(py)),
  }
}

/** Recalcule taille et visibilité de chaque nom pour le zoom courant. */
export function placerEtiquettes(map: maplibregl.Map, places: Place[], villes: Obstacle[] = []) {
  const z = map.getZoom()
  const monde = 512 * 2 ** z // largeur du monde en pixels
  const max = tailleMax(z)
  const candidats: { p: Place; taille: number; dispoH: number; dispoL: number; sous: number; l: number; h: number }[] = []
  for (const p of places) {
    // hiérarchie : de loin, seulement les territoires de premier niveau ; de près, les zones plutôt que l'enveloppe
    const admis = (z >= 3.8 || p.profondeur === 0) && !(z >= 5 && p.parent)
    const dispoL = (2 * p.demiLargeur * monde) / 360
    const dispoH = 2 * p.demiHauteur * monde
    const taille = Math.min(max, (MARGE * dispoL) / (p.largeur16 / 16), (MARGE * dispoH) / HAUTEUR_LIGNE)
    if (!admis || taille < TAILLE_MIN) { p.el.dataset.tient = '0'; continue }
    // sous-titre (alignement…) : seulement s'il tient aussi
    const sous = Math.max(9, Math.min(11, taille * 0.7))
    const lSous = (p.largeurSous11 * sous) / 11
    const avecSous = p.largeurSous11 > 0 && lSous <= MARGE * dispoL && taille * HAUTEUR_LIGNE + sous * 1.25 <= MARGE * dispoH
    p.el.style.setProperty('--taille-nom', `${taille.toFixed(1)}px`)
    p.el.style.setProperty('--taille-sous', `${sous.toFixed(1)}px`)
    p.el.dataset.sous = avecSous ? '1' : '0'
    candidats.push({ p, taille, dispoH, dispoL, sous: avecSous ? sous : 0, l: Math.max((p.largeur16 * taille) / 16, avecSous ? lSous : 0), h: taille * HAUTEUR_LIGNE + (avecSous ? sous * 1.25 : 0) })
  }
  // chevauchements : les plus grands noms d'abord
  candidats.sort((a, b) => b.taille - a.taille)
  const poses: [number, number, number, number][] = []
  for (const v of villes) { // les villes visibles à ce zoom : point + nom à droite
    if (z < v.seuil) continue
    const { x, y } = map.project(v.point as [number, number])
    poses.push([x - 5, y - 8, x + 9 + v.largeur, y + 8])
  }
  for (const c of candidats) {
    const { x, y } = map.project(c.p.point as [number, number])
    // si la place est prise (une ville, un autre nom), on essaie de décaler un peu le nom, sans sortir du territoire
    const pasY = c.h * 0.8, jeuY = (MARGE * c.dispoH - c.h) / 2
    const pasX = c.l * 0.35, jeuX = (MARGE * c.dispoL - c.l) / 2
    const ys = [0, pasY, -pasY, 2 * pasY, -2 * pasY].filter((d) => Math.abs(d) <= jeuY)
    const xs = [0, -pasX, pasX, -2 * pasX, 2 * pasX].filter((d) => Math.abs(d) <= jeuX)
    let pose: [number, number, number, number] | null = null
    let dx = 0, dy = 0
    chercher: for (const ex of xs) for (const ey of ys) {
      const r: [number, number, number, number] = [x + ex - c.l / 2 - 3, y + ey - c.h / 2 - 2, x + ex + c.l / 2 + 3, y + ey + c.h / 2 + 2]
      if (!poses.some((o) => r[0] < o[2] && r[2] > o[0] && r[1] < o[3] && r[3] > o[1])) { pose = r; dx = ex; dy = ey; break chercher }
    }
    c.p.el.dataset.tient = pose ? '1' : '0'
    c.p.el.style.marginTop = pose && dy ? `${dy.toFixed(0)}px` : ''
    c.p.el.style.marginLeft = pose && dx ? `${dx.toFixed(0)}px` : ''
    if (pose) poses.push(pose)
  }
}
