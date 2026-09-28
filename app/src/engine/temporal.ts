// Moteur temporel — la règle verrouillée dans le récap technique (§8) :
//   un état est actif à la date D si  valid_from <= D  ET  (valid_to vide OU D < valid_to)
// valid_to est EXCLUSIF : le jour de bascule appartient déjà au nouvel état.
// Un valid_to vide veut dire « toujours ouvert » : aucun document n'a encore fermé cet état.
import type { DateFloue, Entite, Etat, Evenement } from '../types'

/** "1918" → "1918-01-01", "1945-01" → "1945-01-01", "1945-01-15" inchangé. Vide → null. */
export function normaliser(d: DateFloue | string | undefined): string | null {
  const s = typeof d === 'string' ? d : d?.date
  if (!s) return null
  if (/^\d{4}$/.test(s)) return `${s}-01-01`
  if (/^\d{4}-\d{2}$/.test(s)) return `${s}-01`
  return s
}

export function etatEstActif(etat: Etat, date: string): boolean {
  const debut = normaliser(etat.valid_from)
  const fin = normaliser(etat.valid_to)
  return (debut === null || debut <= date) && (fin === null || date < fin)
}

/** L'état valable à cette date (ou null si l'entité n'existe pas encore / plus). */
export function etatActif(entite: Entite, date: string): Etat | null {
  const actifs = entite.etats.filter((e) => etatEstActif(e, date))
  if (actifs.length > 1) console.warn(`[Atlas] ${entite.entite_id} : ${actifs.length} états actifs le ${date} (chevauchement)`)
  return actifs[0] ?? null
}

export type PhaseEvenement = 'futur' | 'en_cours' | 'passe'

/** Un événement est « en cours » entre date_precise et date_fin (ou le jour même), « passé » ensuite. */
export function phaseEvenement(ev: Evenement, date: string): PhaseEvenement {
  const debut = normaliser(ev.date_precise)!
  const fin = normaliser(ev.date_fin) ?? debut
  if (date < debut) return 'futur'
  if (date <= fin) return 'en_cours'
  return 'passe'
}

// --- utilitaires de dates (tout en UTC, format AAAA-MM-JJ) ---
export function ajouterJours(date: string, n: number): string {
  const d = new Date(`${date}T00:00:00Z`)
  d.setUTCDate(d.getUTCDate() + n)
  return d.toISOString().slice(0, 10)
}
export function ecartJours(a: string, b: string): number {
  return Math.round((Date.parse(`${b}T00:00:00Z`) - Date.parse(`${a}T00:00:00Z`)) / 86400000)
}
export function dateLongue(date: string): string {
  return new Date(`${date}T00:00:00Z`).toLocaleDateString('fr-FR', {
    weekday: 'long', day: 'numeric', month: 'long', year: 'numeric', timeZone: 'UTC',
  })
}
export function dateCourte(d: DateFloue | string): string {
  const s = typeof d === 'string' ? d : d.date
  if (!s) return typeof d !== 'string' && d.precision === 'inconnue' ? 'fin non encore documentée' : 'en cours'
  if (/^\d{4}$/.test(s)) return s
  if (/^\d{4}-\d{2}$/.test(s)) return new Date(`${s}-01T00:00:00Z`).toLocaleDateString('fr-FR', { month: 'long', year: 'numeric', timeZone: 'UTC' })
  return new Date(`${s}T00:00:00Z`).toLocaleDateString('fr-FR', { day: 'numeric', month: 'short', year: 'numeric', timeZone: 'UTC' })
}
