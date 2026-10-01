import { useEffect, useRef } from 'react'
import * as maplibregl from 'maplibre-gl'
import './worker'
import type { FeatureCollection, Polygon } from 'geojson'
import type { CouchesDuJour } from '../engine/features'
import { pointRepresentatif } from '../engine/features'
import type { Selection } from '../types'
import { LIBELLES } from '../theme/palettes'
import { espaceLibre, largeurNom, largeurSousTitre, largeurVille, placerEtiquettes, type Obstacle, type Place } from './etiquettes'

export interface Calques {
  territoires: boolean
  frontieres: boolean
  fronts: boolean
  ponts: boolean
  evenements: boolean
  parcours: boolean
  villes: boolean
  reperesModernes: boolean
}

// Seuils de zoom des pastilles selon profondeur_affichage (gabarit événement)
export const ZOOM_MIN = { atlas: 0, regional: 5, archive: 6.5 } as const
const PROFONDEURS = ['atlas', 'regional', 'archive'] as const

// Villes : priorité d'affichage automatique selon le zoom (Ether, 30/09/2026) — A capitales, B grandes villes, C nœuds régionaux, D micro-histoire
export const ZOOM_VILLES = { A: 3.8, B: 5, C: 6.5, D: 7.5 } as const
const IMPORTANCES = ['A', 'B', 'C', 'D'] as const

const ETAGES = [0, 1, 2]
const couche = (base: string, d: number) => (d === 0 ? base : `${base}-${d}`)
const VIDE: FeatureCollection = { type: 'FeatureCollection', features: [] }
const GROUPES: Record<keyof Calques, string[]> = {
  territoires: [...ETAGES.flatMap((d) => [...(d > 0 ? [`territoires-masque-${d}`] : []), couche('territoires-fond', d), couche('territoires-hachures', d)]), 'territoires-lisere', 'territoires-contour'],
  frontieres: ['frontieres'],
  fronts: ['fronts-bande', 'fronts-trait'],
  ponts: ['ponts'],
  evenements: PROFONDEURS.map((p) => `pastilles-${p}`),
  parcours: PROFONDEURS.map((p) => `parcours-${p}`),
  villes: IMPORTANCES.map((i) => `villes-${i}`),
  reperesModernes: ['osm'],
}
const CLIQUABLES = [...IMPORTANCES.map((i) => `villes-${i}`), ...PROFONDEURS.map((p) => `pastilles-${p}`), ...PROFONDEURS.map((p) => `parcours-${p}`), 'ponts', 'frontieres', ...[...ETAGES].reverse().map((d) => couche('territoires-fond', d))]

interface Props {
  emprise: [number, number, number, number]
  couches: CouchesDuJour
  calques: Calques
  selection: Selection
  onSelect: (s: Selection) => void
  onZoom: (z: number) => void
}

export default function MapView({ emprise, couches, calques, selection, onSelect, onZoom }: Props) {
  const conteneur = useRef<HTMLDivElement>(null)
  const carte = useRef<maplibregl.Map | null>(null)
  const prete = useRef(false)
  const etiquettes = useRef<maplibregl.Marker[]>([])
  const places = useRef<Place[]>([])
  const obstacles = useRef<Obstacle[]>([])
  const derniers = useRef({ couches, calques, selection, onSelect, onZoom })
  derniers.current = { couches, calques, selection, onSelect, onZoom }

  // --- création de la carte (une seule fois) ---
  useEffect(() => {
    const map = new maplibregl.Map({
      container: conteneur.current!,
      bounds: emprise,
      fitBoundsOptions: { padding: { top: 90, bottom: 90, left: 30, right: 30 } },
      minZoom: 2,
      maxZoom: 12,
      attributionControl: {
        compact: true,
        customAttribution: '<a href="https://www.openhistoricalmap.org/copyright" target="_blank">OpenHistoricalMap</a> (CC0) · Kartverket (CC BY 4.0) · GURS Slovénie (CC BY 4.0) · OCHA (CC BY-IGO) · fronts : <a href="https://dhc.westpoint.edu/atlases/" target="_blank">West Point</a> · <a href="https://github.com/Guizmo9867/Atlas" target="_blank">Atlas Eurasie</a> (CC BY 4.0)',
      },
      style: {
        version: 8,
        sources: {
          // Fond Natural Earth 1:10m : le MÊME trait de côte que celui qui découpe les territoires (sinon décalages au zoom)
          terres: { type: 'geojson', data: '/fond/terres_10m.geojson', attribution: 'Natural Earth' },
          lacs: { type: 'geojson', data: '/fond/lacs_10m.geojson' },
          fleuves: { type: 'geojson', data: '/fond/fleuves_10m.geojson' },
          osm: { type: 'raster', tiles: ['https://tile.openstreetmap.org/{z}/{x}/{y}.png'], tileSize: 256, maxzoom: 19, attribution: '© OpenStreetMap contributors' },
          territoires: { type: 'geojson', data: VIDE },
          frontieres: { type: 'geojson', data: VIDE },
          ponts: { type: 'geojson', data: VIDE },
          pastilles: { type: 'geojson', data: VIDE },
          parcours: { type: 'geojson', data: VIDE },
          villes: { type: 'geojson', data: VIDE },
        },
        layers: [
          { id: 'mer', type: 'background', paint: { 'background-color': '#c6d6dd' } },
          // Terres « sans données » : gris clair neutre, pour ne pas les confondre avec les pays neutres (ivoire)
          { id: 'terres', type: 'fill', source: 'terres', paint: { 'fill-color': '#e2e0d9' } },
          { id: 'osm', type: 'raster', source: 'osm', layout: { visibility: 'none' }, paint: { 'raster-opacity': 0.55 } },
          // Un étage par profondeur (pays, puis zones « enfants », puis sous-zones) : un enfant masque d'abord
          // le fond ET les hachures de son parent (sinon les hachures du parent débordent sur une zone libérée).
          ...ETAGES.flatMap((d) => [
            ...(d > 0 ? [{ id: `territoires-masque-${d}`, type: 'fill' as const, source: 'territoires',
              filter: ['==', ['get', 'profondeur'], d] as maplibregl.FilterSpecification, paint: { 'fill-color': '#e2e0d9' } }] : []),
            { id: couche('territoires-fond', d), type: 'fill' as const, source: 'territoires',
              filter: (d < ETAGES.length - 1 ? ['==', ['get', 'profondeur'], d] : ['>=', ['get', 'profondeur'], d]) as maplibregl.FilterSpecification,
              paint: { 'fill-color': ['get', 'couleur'] as unknown as string, 'fill-opacity': 0.62 } },
            { id: couche('territoires-hachures', d), type: 'fill' as const, source: 'territoires',
              filter: ['all', ['!=', ['get', 'hachure'], ''], d < ETAGES.length - 1 ? ['==', ['get', 'profondeur'], d] : ['>=', ['get', 'profondeur'], d]] as maplibregl.FilterSpecification,
              paint: { 'fill-pattern': ['get', 'hachure'] as unknown as string } },
          ]),
          { id: 'territoires-lisere', type: 'line', source: 'territoires', filter: ['!=', ['get', 'lisere'], ''],
            paint: { 'line-color': ['get', 'lisere'] as unknown as string, 'line-width': 3, 'line-opacity': 0.85 } },
          { id: 'territoires-contour', type: 'line', source: 'territoires', paint: { 'line-color': '#5b5448', 'line-width': 0.8 } },
          // L'eau PAR-DESSUS les territoires : lacs et fleuves restent visibles quel que soit le calque
          { id: 'lacs', type: 'fill', source: 'lacs', paint: { 'fill-color': '#c6d6dd' } },
          { id: 'fleuves-majeurs', type: 'line', source: 'fleuves', filter: ['<=', ['get', 'scalerank'], 6],
            layout: { 'line-cap': 'round', 'line-join': 'round' },
            paint: { 'line-color': '#8fb3c4', 'line-width': ['interpolate', ['linear'], ['zoom'], 3, 0.6, 8, 2.2] } },
          { id: 'fleuves-mineurs', type: 'line', source: 'fleuves', minzoom: 5, filter: ['>', ['get', 'scalerank'], 6],
            layout: { 'line-cap': 'round', 'line-join': 'round' },
            paint: { 'line-color': '#8fb3c4', 'line-width': ['interpolate', ['linear'], ['zoom'], 5, 0.4, 9, 1.4] } },
          // Lignes de front : une bande semi-transparente + un trait fin (jamais une couleur politique)
          { id: 'fronts-bande', type: 'line', source: 'frontieres', filter: ['==', ['get', 'type'], 'ligne_front'],
            layout: { 'line-cap': 'round', 'line-join': 'round' },
            paint: { 'line-color': '#8b2f2f', 'line-width': 12, 'line-opacity': 0.28, 'line-blur': 2 } },
          { id: 'fronts-trait', type: 'line', source: 'frontieres', filter: ['==', ['get', 'type'], 'ligne_front'],
            paint: { 'line-color': '#8b2f2f', 'line-width': 1.6 } },
          { id: 'frontieres', type: 'line', source: 'frontieres', filter: ['!=', ['get', 'type'], 'ligne_front'],
            paint: { 'line-color': '#2a2622', 'line-width': 2.4 } },
          ...PROFONDEURS.map((p) => ({
            id: `parcours-${p}`, type: 'line' as const, source: 'parcours', minzoom: ZOOM_MIN[p],
            filter: ['==', ['get', 'profondeur'], p] as maplibregl.FilterSpecification,
            layout: { 'line-cap': 'round' as const, 'line-join': 'round' as const },
            paint: { 'line-color': ['get', 'couleur'] as unknown as string, 'line-width': 3.5, 'line-dasharray': [1.5, 1.2],
              'line-opacity': ['case', ['==', ['get', 'phase'], 'en_cours'], 0.95, 0.45] as unknown as number },
          })),
          ...IMPORTANCES.map((i) => ({
            id: `villes-${i}`, type: 'circle' as const, source: 'villes', minzoom: ZOOM_VILLES[i],
            filter: ['==', ['get', 'importance'], i] as maplibregl.FilterSpecification,
            paint: {
              'circle-radius': (i === 'A' ? 4.5 : i === 'B' ? 3.6 : 2.8) as number,
              // ville détruite ou évacuée au jour affiché : point gris (flux coupés)
              'circle-color': ['case', ['!=', ['get', 'situation'], ''], '#a59d90', ['!=', ['get', 'capitale'], ''], '#2a2622', '#fffdf8'] as unknown as string,
              'circle-stroke-color': ['case', ['!=', ['get', 'capitale'], ''], '#fffdf8', '#2a2622'] as unknown as string,
              'circle-stroke-width': (i === 'A' ? 2 : 1.4) as number,
            },
          })),
          { id: 'selection-ligne', type: 'line', source: 'territoires', filter: ['==', ['get', 'entite_id'], ''],
            paint: { 'line-color': '#111', 'line-width': 3 } },
          { id: 'ponts', type: 'circle', source: 'ponts',
            paint: { 'circle-radius': 6, 'circle-color': ['match', ['get', 'statut'], 'detruit', '#c0392b', '#ffffff'],
              'circle-stroke-color': '#222', 'circle-stroke-width': 2 } },
          ...PROFONDEURS.map((p) => ({
            id: `pastilles-${p}`, type: 'circle' as const, source: 'pastilles', minzoom: ZOOM_MIN[p],
            filter: ['==', ['get', 'profondeur'], p] as maplibregl.FilterSpecification,
            paint: {
              'circle-radius': ['case', ['==', ['get', 'phase'], 'en_cours'], 9, 6] as unknown as number,
              'circle-color': ['get', 'couleur'] as unknown as string,
              'circle-opacity': ['case', ['==', ['get', 'phase'], 'en_cours'], 1, 0.5] as unknown as number,
              'circle-stroke-color': '#ffffff', 'circle-stroke-width': 2.5,
            },
          })),
          { id: 'selection-pastille', type: 'circle', source: 'pastilles', filter: ['==', ['get', 'id'], ''],
            paint: { 'circle-radius': 14, 'circle-color': 'rgba(0,0,0,0)', 'circle-stroke-color': '#111', 'circle-stroke-width': 2.5 } },
        ],
      },
    })
    map.addControl(new maplibregl.NavigationControl({ showCompass: false }), 'top-right')
    // Motifs de hachures fabriqués à la demande : « hachure-rrggbb » → rayures diagonales de cette couleur
    map.setMissingStyleImageResolver((id) => {
      if (map.hasImage(id)) return
      if (id.startsWith('hachure-')) map.addImage(id, dessinerHachure(`#${id.slice(8)}`), { pixelRatio: 2 })
      else if (id.startsWith('croise-')) map.addImage(id, dessinerHachure(`#${id.slice(7)}`, true), { pixelRatio: 2 })
    })
    map.addControl(new maplibregl.ScaleControl({ unit: 'metric' }), 'bottom-right')

    const survol = new maplibregl.Popup({ closeButton: false, closeOnClick: false, offset: 12, className: 'survol' })
    map.on('mousemove', (e) => {
      const f = map.queryRenderedFeatures(e.point, { layers: CLIQUABLES })[0]
      map.getCanvas().style.cursor = f ? 'pointer' : ''
      const titre = f && (f.properties.titre ?? (f.layer.id.startsWith('territoires-fond') ? null : f.properties.nom))
      if (titre) survol.setLngLat(e.lngLat).setText(String(titre)).addTo(map)
      else survol.remove()
    })
    map.on('click', (e) => {
      const trouves = map.queryRenderedFeatures(e.point, { layers: CLIQUABLES })
      trouves.sort((a, b) => CLIQUABLES.indexOf(a.layer.id) - CLIQUABLES.indexOf(b.layer.id))
      const f = trouves[0]
      if (!f) return derniers.current.onSelect(null)
      if (f.properties.id) derniers.current.onSelect({ kind: 'evenement', id: String(f.properties.id) })
      else derniers.current.onSelect({ kind: 'entite', id: String(f.properties.entite_id) })
    })
    const majZoom = () => {
      derniers.current.onZoom(map.getZoom())
      map.getContainer().classList.toggle('zoom-continent', map.getZoom() < ZOOM_VILLES.A)
      // à petite échelle, on n'étiquette que les territoires « parents » (sinon tout se chevauche)
      map.getContainer().classList.toggle('zoom-faible', map.getZoom() < 3.8)
      map.getContainer().classList.toggle('zoom-moyen', map.getZoom() < 5)
      map.getContainer().classList.toggle('zoom-regional', map.getZoom() < 6.5)
      map.getContainer().classList.toggle('zoom-local', map.getZoom() < 7.5)
    }
    map.on('zoom', majZoom)
    // noms des territoires : taille et visibilité recalculées au zoom (une fois par image au plus)
    let attente = 0
    map.on('zoom', () => { if (!attente) attente = requestAnimationFrame(() => { attente = 0; placerEtiquettes(map, places.current, derniers.current.calques.villes ? obstacles.current : []) }) })
    map.on('load', majZoom)
    map.on('load', () => {
      prete.current = true
      appliquer(map, derniers.current.couches, etiquettes, places, obstacles, derniers.current.calques.villes)
      visibilite(map, derniers.current.calques)
      surligner(map, derniers.current.selection)
      derniers.current.onZoom(map.getZoom())
    })
    carte.current = map
    ;(window as unknown as { __atlasCarte?: maplibregl.Map }).__atlasCarte = map // accès pour les tests automatiques
    return () => { prete.current = false; map.remove(); carte.current = null }
  }, [])

  useEffect(() => {
    if (carte.current && prete.current) { appliquer(carte.current, couches, etiquettes, places, obstacles, derniers.current.calques.villes); visibilite(carte.current, derniers.current.calques) }
  }, [couches])
  useEffect(() => {
    if (carte.current && prete.current) { visibilite(carte.current, calques); placerEtiquettes(carte.current, places.current, calques.villes ? obstacles.current : []) }
  }, [calques])
  // Changement de corpus : on recadre la carte
  useEffect(() => {
    carte.current?.fitBounds(emprise, { padding: { top: 30, bottom: 140, left: 30, right: 30 }, duration: 800 })
  }, [emprise[0], emprise[1], emprise[2], emprise[3]])
  useEffect(() => { if (carte.current && prete.current) surligner(carte.current, selection) }, [selection])

  return <div ref={conteneur} className="carte" />
}

function appliquer(map: maplibregl.Map, c: CouchesDuJour, etiquettes: React.MutableRefObject<maplibregl.Marker[]>, places: React.MutableRefObject<Place[]>,
  obstacles: React.MutableRefObject<Obstacle[]>, villesVisibles: boolean) {
  const src = (id: string) => map.getSource(id) as maplibregl.GeoJSONSource
  src('territoires').setData(c.territoires)
  src('frontieres').setData(c.frontieres)
  src('ponts').setData(c.ponts)
  src('pastilles').setData(c.pastilles)
  src('parcours').setData(c.parcours)
  src('villes').setData(c.villes)
  // Étiquettes des territoires (éléments HTML : pas besoin de serveur de polices)
  etiquettes.current.forEach((m) => m.remove())
  places.current = []
  etiquettes.current = c.territoires.features.map((f) => {
    const el = document.createElement('div')
    el.className = 'etiquette'
    el.dataset.tient = '0' // visible seulement une fois placée (voir etiquettes.ts)
    const nom = String(f.properties?.nom_court ?? f.properties?.nom ?? '')
    const v = String(f.properties?.valeur_mode ?? '')
    const libelle = LIBELLES[v] ?? v
    // Sous-titre seulement s'il apporte une info (ex. « Cordanie (occupant) » en mode contrôle)
    const sousTitre = v && libelle !== nom ? libelle : ''
    el.innerHTML = `<strong>${nom}</strong>${sousTitre ? `<span>${sousTitre}</span>` : ''}`
    const place = espaceLibre(f.geometry, pointRepresentatif(f.geometry as Polygon))
    const point = place.point
    places.current.push({
      el, ...place,
      largeur16: largeurNom(nom), largeurSous11: largeurSousTitre(sousTitre),
      profondeur: Number(f.properties?.profondeur ?? 0),
      parent: Boolean(f.properties?.a_enfants), // de près, on lit les zones plutôt que l'enveloppe
    })
    return new maplibregl.Marker({ element: el }).setLngLat(point as [number, number]).addTo(map)
  })
  ;(window as unknown as { __atlasPlaces?: Place[] }).__atlasPlaces = places.current // pour les tests automatiques
  // Noms des villes : à droite du point (à gauche si la place est prise, cachés si aucune place : voir etiquettes.ts)
  obstacles.current = []
  etiquettes.current.push(...c.villes.features.map((f) => {
    const imp = String(f.properties?.importance ?? 'C') as keyof typeof ZOOM_VILLES
    const nom = String(f.properties?.nom ?? '')
    const el = document.createElement('div')
    el.className = 'ville-nom'
    el.dataset.importance = imp
    el.dataset.capitale = f.properties?.capitale ? '1' : '0'
    const span = document.createElement('span')
    span.textContent = nom
    el.append(span)
    const point = (f.geometry as GeoJSON.Point).coordinates
    obstacles.current.push({ point, largeur: largeurVille(nom, imp), seuil: ZOOM_VILLES[imp] ?? 6.5, el,
      rang: f.properties?.capitale ? 0 : 1 + 'ABCD'.indexOf(imp) })
    return new maplibregl.Marker({ element: el, anchor: 'left', offset: [7, 0] }).setLngLat(point as [number, number]).addTo(map)
  }))
  placerEtiquettes(map, places.current, villesVisibles ? obstacles.current : [])
}

function visibilite(map: maplibregl.Map, calques: Calques) {
  for (const [cle, ids] of Object.entries(GROUPES)) {
    for (const id of ids) map.setLayoutProperty(id, 'visibility', calques[cle as keyof Calques] ? 'visible' : 'none')
  }
  document.querySelectorAll<HTMLElement>('.etiquette').forEach((el) => { el.style.display = calques.territoires ? '' : 'none' })
  document.querySelectorAll<HTMLElement>('.ville-nom').forEach((el) => { el.style.display = calques.villes ? '' : 'none' })
}

function surligner(map: maplibregl.Map, s: Selection) {
  map.setFilter('selection-ligne', ['==', ['get', 'entite_id'], s?.kind === 'entite' ? s.id : ''])
  map.setFilter('selection-pastille', ['==', ['get', 'id'], s?.kind === 'evenement' ? s.id : ''])
}

/** Un carreau 16×16 px de rayures diagonales (se répète sans couture). */
/** Rayures diagonales ; croisées = « contrôle non tranché » (souverain connu, contrôle réel disputé). */
function dessinerHachure(couleur: string, croise = false): ImageData {
  const t = 16
  const ctx = Object.assign(document.createElement('canvas'), { width: t, height: t }).getContext('2d')!
  ctx.strokeStyle = couleur
  ctx.globalAlpha = 0.75
  ctx.lineWidth = 2.5
  if (croise) { ctx.lineWidth = 1.2; ctx.setLineDash([3, 3]) }
  for (const d of [-t, 0, t]) { ctx.beginPath(); ctx.moveTo(d, t); ctx.lineTo(d + t, 0); ctx.stroke() }
  if (croise) for (const d of [-t, 0, t]) { ctx.beginPath(); ctx.moveTo(d, 0); ctx.lineTo(d + t, t); ctx.stroke() }
  return ctx.getImageData(0, 0, t, t)
}

