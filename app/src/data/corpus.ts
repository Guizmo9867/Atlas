// Point d'entrée des données. Le corpus vit dans /data à la racine du dépôt,
// indépendant de ce code : si on change un jour de framework, les données restent.
import type { Feature, Geometry } from 'geojson'
import type { Entite, Evenement, SourceRegistre } from '../types'
import entitesProto from '../../../data/prototype_v0/entites.json'
import evenementsProto from '../../../data/prototype_v0/evenements.json'
import registreProto from '../../../data/prototype_v0/registre_sources_fictif.json'
import registreReel from '../../../data/sources/atlas_registre_sources.json'

// Tous les lots du Snapshot 0 (data/snapshot0/*.json), chargés ensemble
const LOTS_SNAPSHOT0 = import.meta.glob('../../../data/snapshot0/*.json', { eager: true, import: 'default' }) as Record<string, { entites: Entite[] }>

// Les géométries partagées (geometrie_ref) : un fichier .geojson par géométrie, chargé à la demande.
const URLS_GEOMETRIES = import.meta.glob('../../../data/geometries/**/*.geojson', { query: '?url', import: 'default', eager: true }) as Record<string, string>

export type IdCorpus = 'snapshot0' | 'prototype'

export interface Corpus {
  id: IdCorpus
  nom: string
  fictif: boolean
  entites: Entite[]
  evenements: Evenement[]
  sources: SourceRegistre[]
  geometries: Record<string, Feature>
  debut: string
  fin: string
  emprise: [number, number, number, number] // [ouest, sud, est, nord] pour cadrer la carte
}

export const LISTE_CORPUS: { id: IdCorpus; nom: string; aide: string }[] = [
  { id: 'snapshot0', nom: 'Snapshot 0 — 1er janvier 1945', aide: 'Données réelles (lots 01 à 03). Tracés provisoires.' },
  { id: 'prototype', nom: 'Prototype V0 (fictif)', aide: 'Ruritanie et Kovalie : pour tester le moteur.' },
]

export async function chargerCorpus(id: IdCorpus): Promise<Corpus> {
  if (id === 'prototype') {
    return {
      id, nom: 'Prototype V0', fictif: true,
      entites: entitesProto.entites as unknown as Entite[],
      evenements: evenementsProto.evenements as unknown as Evenement[],
      sources: registreProto.sources as unknown as SourceRegistre[],
      geometries: {}, debut: '1945-01-01', fin: '1945-01-31', emprise: [15.5, 45.3, 26.5, 50.9],
    }
  }
  const entites = Object.keys(LOTS_SNAPSHOT0).sort().flatMap((k) => LOTS_SNAPSHOT0[k].entites ?? [])
  const refs = new Set(entites.flatMap((e) => e.etats.map((s) => s.geometrie_ref).filter(Boolean)))
  const geometries: Record<string, Feature> = {}
  await Promise.all(Object.entries(URLS_GEOMETRIES).map(async ([chemin, url]) => {
    const ref = chemin.split('/').pop()!.replace('.geojson', '')
    if (!refs.has(ref)) return
    geometries[ref] = await (await fetch(url)).json()
  }))
  return {
    id, nom: 'Snapshot 0', fictif: false, entites, evenements: [],
    sources: registreReel.sources as unknown as SourceRegistre[],
    geometries, debut: '1945-01-01', fin: '1945-01-31', emprise: [5, 38, 150, 76],
  }
}

export const geometriesSeules = (c: Corpus): Record<string, Geometry> =>
  Object.fromEntries(Object.entries(c.geometries).map(([k, f]) => [k, f.geometry]))
