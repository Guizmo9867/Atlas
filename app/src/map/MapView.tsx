import { useEffect, useRef } from 'react'
import * as maplibregl from 'maplibre-gl'
import './worker'
import type { FeatureCollection, Polygon } from 'geojson'
import type { CouchesDuJour } from '../engine/features'
import { pointRepresentatif } from '../engine/features'
import type { Selection } from '../types'
import { LIBELLES } from '../theme/palettes'

export interface Calques {
  territoires: boolean
  frontieres: boolean
  fronts: boolean
  ponts: boolean
  evenements: boolean
  parcours: boolean
  reperesModernes: boolean
}

// Seuils de zoom des pastilles selon profondeur_affichage (gabarit événement)
export const ZOOM_MIN = { atlas: 0, regional: 5, archive: 6.5 } as const
const PROFONDEURS = ['atlas', 'regional', 'archive'] as const

const VIDE: FeatureCollection = { type: 'FeatureCollection', features: [] }
const GROUPES: Record<keyof Calques, string[]> = {
  territoires: ['territoires-fond', 'territoires-hachures', 'territoires-lisere', 'territoires-contour'],
  frontieres: ['frontieres'],
  fronts: ['fronts-bande', 'fronts-trait'],
  ponts: ['ponts'],
  evenements: PROFONDEURS.map((p) => `pastilles-${p}`),
  parcours: PROFONDEURS.map((p) => `parcours-${p}`),
  reperesModernes: ['osm'],
}
const CLIQUABLES = [...PROFONDEURS.map((p) => `pastilles-${p}`), ...PROFONDEURS.map((p) => `parcours-${p}`), 'ponts', 'frontieres', 'territoires-fond']

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
  const derniers = useRef({ couches, calques, selection, onSelect, onZoom })
  derniers.current = { couches, calques, selection, onSelect, onZoom }

  // --- création de la carte (une seule fois) ---
  useEffect(() => {
    const map = new maplibregl.Map({
      container: conteneur.current!,
      bounds: emprise,
      fitBoundsOptions: { padding: { top: 30, bottom: 140, left: 30, right: 30 } },
      minZoom: 2,
      maxZoom: 12,
      attributionControl: {
        compact: true,
        customAttribution: '<a href="https://www.openhistoricalmap.org/copyright" target="_blank">OpenHistoricalMap</a> (CC0) · Kartverket (CC BY 4.0) · GURS Slovénie (CC BY 4.0) · OCHA (CC BY-IGO)',
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
        },
        layers: [
          { id: 'mer', type: 'background', paint: { 'background-color': '#c6d6dd' } },
          // Terres « sans données » : gris clair neutre, pour ne pas les confondre avec les pays neutres (ivoire)
          { id: 'terres', type: 'fill', source: 'terres', paint: { 'fill-color': '#e2e0d9' } },
          { id: 'osm', type: 'raster', source: 'osm', layout: { visibility: 'none' }, paint: { 'raster-opacity': 0.55 } },
          { id: 'territoires-fond', type: 'fill', source: 'territoires', paint: { 'fill-color': ['get', 'couleur'], 'fill-opacity': 0.62 } },
          { id: 'territoires-hachures', type: 'fill', source: 'territoires', filter: ['!=', ['get', 'hachure'], ''],
            paint: { 'fill-pattern': ['get', 'hachure'] as unknown as string } },
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
      if (!id.startsWith('hachure-') || map.hasImage(id)) return
      map.addImage(id, dessinerHachure(`#${id.slice(8)}`), { pixelRatio: 2 })
    })
    map.addControl(new maplibregl.ScaleControl({ unit: 'metric' }), 'bottom-right')

    const survol = new maplibregl.Popup({ closeButton: false, closeOnClick: false, offset: 12, className: 'survol' })
    map.on('mousemove', (e) => {
      const f = map.queryRenderedFeatures(e.point, { layers: CLIQUABLES })[0]
      map.getCanvas().style.cursor = f ? 'pointer' : ''
      const titre = f && (f.properties.titre ?? (f.layer.id === 'territoires-fond' ? null : f.properties.nom))
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
      // à petite échelle, on n'étiquette que les territoires « parents » (sinon tout se chevauche)
      map.getContainer().classList.toggle('zoom-faible', map.getZoom() < 3.8)
      map.getContainer().classList.toggle('zoom-moyen', map.getZoom() < 5)
    }
    map.on('zoom', majZoom)
    map.on('load', majZoom)
    map.on('load', () => {
      prete.current = true
      appliquer(map, derniers.current.couches, etiquettes)
      visibilite(map, derniers.current.calques)
      surligner(map, derniers.current.selection)
      derniers.current.onZoom(map.getZoom())
    })
    carte.current = map
    ;(window as unknown as { __atlasCarte?: maplibregl.Map }).__atlasCarte = map // accès pour les tests automatiques
    return () => { prete.current = false; map.remove(); carte.current = null }
  }, [])

  useEffect(() => {
    if (carte.current && prete.current) { appliquer(carte.current, couches, etiquettes); visibilite(carte.current, derniers.current.calques) }
  }, [couches])
  useEffect(() => { if (carte.current && prete.current) visibilite(carte.current, calques) }, [calques])
  // Changement de corpus : on recadre la carte
  useEffect(() => {
    carte.current?.fitBounds(emprise, { padding: { top: 30, bottom: 140, left: 30, right: 30 }, duration: 800 })
  }, [emprise[0], emprise[1], emprise[2], emprise[3]])
  useEffect(() => { if (carte.current && prete.current) surligner(carte.current, selection) }, [selection])

  return <div ref={conteneur} className="carte" />
}

function appliquer(map: maplibregl.Map, c: CouchesDuJour, etiquettes: React.MutableRefObject<maplibregl.Marker[]>) {
  const src = (id: string) => map.getSource(id) as maplibregl.GeoJSONSource
  src('territoires').setData(c.territoires)
  src('frontieres').setData(c.frontieres)
  src('ponts').setData(c.ponts)
  src('pastilles').setData(c.pastilles)
  src('parcours').setData(c.parcours)
  // Étiquettes des territoires (éléments HTML : pas besoin de serveur de polices)
  etiquettes.current.forEach((m) => m.remove())
  etiquettes.current = c.territoires.features.map((f) => {
    const el = document.createElement('div')
    el.className = 'etiquette'
    const nom = String(f.properties?.nom_court ?? f.properties?.nom ?? '')
    el.dataset.profondeur = String(f.properties?.profondeur ?? 0)
    el.dataset.petit = etendue(f.geometry) < 25 ? '1' : '0' // < ~25 degrés² : petit territoire
    const v = String(f.properties?.valeur_mode ?? '')
    const libelle = LIBELLES[v] ?? v
    // Sous-titre seulement s'il apporte une info (ex. « Cordanie (occupant) » en mode contrôle)
    el.innerHTML = `<strong>${nom}</strong>${v && libelle !== nom ? `<span>${libelle}</span>` : ''}`
    return new maplibregl.Marker({ element: el }).setLngLat(pointRepresentatif(f.geometry as Polygon) as [number, number]).addTo(map)
  })
}

function visibilite(map: maplibregl.Map, calques: Calques) {
  for (const [cle, ids] of Object.entries(GROUPES)) {
    for (const id of ids) map.setLayoutProperty(id, 'visibility', calques[cle as keyof Calques] ? 'visible' : 'none')
  }
  document.querySelectorAll<HTMLElement>('.etiquette').forEach((el) => { el.style.display = calques.territoires ? '' : 'none' })
}

function surligner(map: maplibregl.Map, s: Selection) {
  map.setFilter('selection-ligne', ['==', ['get', 'entite_id'], s?.kind === 'entite' ? s.id : ''])
  map.setFilter('selection-pastille', ['==', ['get', 'id'], s?.kind === 'evenement' ? s.id : ''])
}

/** Un carreau 16×16 px de rayures diagonales (se répète sans couture). */
function dessinerHachure(couleur: string): ImageData {
  const t = 16
  const ctx = Object.assign(document.createElement('canvas'), { width: t, height: t }).getContext('2d')!
  ctx.strokeStyle = couleur
  ctx.globalAlpha = 0.75
  ctx.lineWidth = 2.5
  for (const d of [-t, 0, t]) { ctx.beginPath(); ctx.moveTo(d, t); ctx.lineTo(d + t, 0); ctx.stroke() }
  return ctx.getImageData(0, 0, t, t)
}

/** Surface approximative du rectangle englobant, en degrés² (pour masquer les petites étiquettes à petite échelle). */
function etendue(g: GeoJSON.Geometry): number {
  let [x0, y0, x1, y1] = [Infinity, Infinity, -Infinity, -Infinity]
  const anneaux = g.type === 'Polygon' ? [g.coordinates[0]] : g.type === 'MultiPolygon' ? g.coordinates.map((p) => p[0]) : []
  for (const a of anneaux) for (const [x, y] of a) { if (x < x0) x0 = x; if (x > x1) x1 = x; if (y < y0) y0 = y; if (y > y1) y1 = y }
  return anneaux.length ? (x1 - x0) * (y1 - y0) : 0
}
