// Types calqués sur les gabarits (gabarits/*.json à la racine du dépôt).
import type { Geometry } from 'geojson'

export type Precision = 'exacte' | 'mois' | 'annee' | 'inconnue' | 'en_cours'
export interface DateFloue { date: string; precision: Precision }
export interface RefSource { source_id: string; locator?: string; usage?: string }

export interface Etat {
  etat_id: string
  valid_from: DateFloue
  valid_to: DateFloue
  statut: string
  // Valeurs simples, sauf souverainete_revendiquee_par (liste d'acteurs)
  proprietes: Record<string, string> & { souverainete_revendiquee_par?: string[] }
  geometrie?: Geometry
  geometrie_ref?: string
  zone_incertitude?: Geometry
  sources: RefSource[]
}

export interface Relation { type: string; cible_type: 'entite' | 'evenement'; cible_id: string; note?: string }

export interface Entite {
  entite_id: string
  type_entite: string
  nom: string
  nom_court?: string
  etats: Etat[]
  relations: Relation[]
}

export interface Evenement {
  id: string
  titre: string
  annee: number
  date_precise: string
  date_fin: string
  pays: string[]
  lieu: string
  geographie: { type: string; geometrie?: Geometry; geometrie_ref?: string }
  categories: string[]
  niveau_importance: string
  profondeur_affichage: 'atlas' | 'regional' | 'archive'
  resume: string
  contexte: string
  deroulement: string
  consequences: Record<string, string>
  relations: Relation[]
  certitude_evenement: string
  etat_sources: string
  notes_incertitude: string
  sources: RefSource[]
  temoignage_personnel: string
}

export interface SourceRegistre {
  source_id: string
  niveau: 'A' | 'B' | 'C'
  type_source: string
  titre: string
  institution: string
  url: string
  locator: string
  notes: string
}

export type ModeLecture = 'souverainete' | 'controle' | 'alignement'

export type Selection =
  | { kind: 'entite'; id: string }
  | { kind: 'evenement'; id: string }
  | null
