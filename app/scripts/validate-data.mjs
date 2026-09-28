// npm run validate:data — contrôle le corpus (dossier data/ à la racine du dépôt).
// Erreur = à corriger avant intégration. Avertissement = à surveiller.
import { readFileSync, readdirSync, statSync } from 'node:fs'
import { join, relative, dirname } from 'node:path'
import { fileURLToPath } from 'node:url'

const RACINE = join(dirname(fileURLToPath(import.meta.url)), '..', '..')
const DATA = join(RACINE, 'data')
const erreurs = [], avertissements = [], provisoires = []
const err = (f, m) => erreurs.push(`${f} : ${m}`)
const avert = (f, m) => avertissements.push(`${f} : ${m}`)

const TYPES_ENTITE = ['frontiere', 'route', 'pont', 'port', 'ferry', 'poste_frontiere', 'territoire', 'voie_ferree', 'ligne_front', 'autre']
const RELATIONS_ENTITE = ['precede', 'suit', 'entraine', 'modifie', 'explique', 'detache_de']
const RELATIONS_EVENEMENT = ['precede', 'suit', 'entraine', 'modifie', 'explique']
const PRECISIONS = ['exacte', 'mois', 'annee', 'inconnue', 'en_cours']
const PROFONDEURS = ['atlas', 'regional', 'archive']
const NIVEAUX = ['structurel', 'evenement_majeur', 'micro_histoire']
const RE_ID_ENTITE = /^[a-z_]+-[a-z]{2}-[a-z0-9]+(-[a-z0-9]+)*$/
const RE_ID_EVENEMENT = /^\d{4}-[a-z]{2}-[a-z0-9]+(-[a-z0-9]+)*$/
const RE_DATE = /^(\d{4})(-\d{2})?(-\d{2})?$/

const norm = (s) => !s ? null : /^\d{4}$/.test(s) ? `${s}-01-01` : /^\d{4}-\d{2}$/.test(s) ? `${s}-01` : s

function fichiersJson(dossier) {
  return readdirSync(dossier).flatMap((n) => {
    const p = join(dossier, n)
    return statSync(p).isDirectory() ? fichiersJson(p) : n.endsWith('.json') ? [p] : []
  })
}

function verifierGeometrie(f, ou, g) {
  if (!g || !g.type) return err(f, `${ou} : géométrie sans type`)
  const pts = []
  const collect = (c) => { if (typeof c?.[0] === 'number') pts.push(c); else if (Array.isArray(c)) c.forEach(collect) }
  collect(g.coordinates)
  if (!pts.length) return err(f, `${ou} : géométrie vide`)
  for (const [lon, lat] of pts) {
    if (Math.abs(lat) > 90 || Math.abs(lon) > 180) return err(f, `${ou} : coordonnée hors limites [${lon}, ${lat}] — ordre [longitude, latitude] inversé ?`)
  }
  if (g.type === 'Polygon') for (const anneau of g.coordinates) {
    const [a, b] = [anneau[0], anneau.at(-1)]
    if (a[0] !== b[0] || a[1] !== b[1]) err(f, `${ou} : polygone non fermé (le dernier point doit répéter le premier)`)
  }
}

// --- 1. Lecture de tous les fichiers ---
const fichiers = fichiersJson(DATA).map((p) => {
  try { return { p, nom: relative(RACINE, p), json: JSON.parse(readFileSync(p, 'utf8')) } }
  catch (e) { err(relative(RACINE, p), `JSON invalide (${e.message})`); return null }
}).filter(Boolean)

// Chaque dossier a son registre : le prototype fictif ne doit jamais citer le registre réel, et inversement
const registres = {}
for (const f of fichiers) if (Array.isArray(f.json.sources) && f.json.metadata?.nom?.includes('registre')) {
  const ids = f.json.sources.map((s) => s.source_id)
  ids.filter((id, i) => ids.indexOf(id) !== i).forEach((id) => err(f.nom, `source_id en double : ${id}`))
  registres[f.nom.includes('prototype') ? 'fictif' : 'reel'] = new Set(ids)
}
const registrePour = (nom) => registres[nom.includes('prototype') ? 'fictif' : 'reel'] ?? new Set()

// Géométries partagées : data/geometries/**/<geometrie_ref>.geojson
const geometries = new Map()
const fichiersGeo = (dossier) => readdirSync(dossier).flatMap((n) => {
  const p = join(dossier, n)
  return statSync(p).isDirectory() ? fichiersGeo(p) : n.endsWith('.geojson') ? [p] : []
})
try {
  for (const p of fichiersGeo(join(DATA, 'geometries'))) {
    const nom = relative(RACINE, p)
    try {
      const f = JSON.parse(readFileSync(p, 'utf8'))
      const id = f.properties?.geometry_id
      if (id !== p.split(/[\\/]/).pop().replace('.geojson', '')) err(nom, `geometry_id « ${id} » ≠ nom du fichier`)
      verifierGeometrie(nom, id, f.geometry)
      for (const src of f.properties?.sources ?? []) if (!registrePour(nom).has(src.source_id)) err(nom, `source_id « ${src.source_id} » absent du registre`)
      if (!f.properties?.sources?.length) err(nom, 'géométrie sans source (protocole : jamais « tracée à la main » sans provenance)')
      geometries.set(id, { nom, statut: f.properties?.statut })
    } catch (e) { err(nom, `GeoJSON invalide (${e.message})`) }
  }
} catch { /* pas encore de dossier geometries */ }

const entites = new Map(), evenements = new Map()
for (const f of fichiers) {
  for (const e of f.json.entites ?? []) {
    if (entites.has(e.entite_id)) err(f.nom, `entite_id en double : ${e.entite_id}`)
    entites.set(e.entite_id, { e, f })
  }
  for (const ev of f.json.evenements ?? []) {
    if (evenements.has(ev.id)) err(f.nom, `id d'événement en double : ${ev.id}`)
    evenements.set(ev.id, { ev, f })
  }
}

// --- 2. Entités ---
for (const [id, { e, f }] of entites) {
  const lot = f.json
  const geomsDeclarees = new Set((lot.geometries_a_creer ?? []).map((g) => g.geometrie_ref))
  if (!RE_ID_ENTITE.test(id)) err(f.nom, `${id} : format d'ID invalide (type-pays-motcle, minuscules, sans accents)`)
  if (!TYPES_ENTITE.includes(e.type_entite)) err(f.nom, `${id} : type_entite inconnu « ${e.type_entite} »`)
  else if (id.split('-')[0] !== e.type_entite) err(f.nom, `${id} : l'ID doit commencer par son type_entite (« ${e.type_entite}- »)`)
  const etatIds = new Set()
  const intervalles = []
  for (const s of e.etats ?? []) {
    const ou = `${id}/${s.etat_id}`
    if (etatIds.has(s.etat_id)) err(f.nom, `${ou} : etat_id en double`)
    etatIds.add(s.etat_id)
    for (const cle of ['valid_from', 'valid_to']) {
      const d = s[cle]
      if (!d || !PRECISIONS.includes(d.precision)) err(f.nom, `${ou} : ${cle}.precision invalide`)
      if (d?.date && !RE_DATE.test(d.date)) err(f.nom, `${ou} : ${cle}.date mal formée « ${d.date} »`)
    }
    const debut = norm(s.valid_from?.date), fin = norm(s.valid_to?.date)
    if (debut && fin && !(debut < fin)) err(f.nom, `${ou} : valid_from doit être avant valid_to`)
    intervalles.push({ ou, debut: debut ?? '0000-00-00', fin: fin ?? '9999-99-99' })
    if (s.geometrie && s.geometrie_ref) err(f.nom, `${ou} : geometrie ET geometrie_ref (un seul des deux)`)
    if (s.geometrie) verifierGeometrie(f.nom, ou, s.geometrie)
    else if (s.geometrie_ref) {
      const g = geometries.get(s.geometrie_ref)
      if (!g && !geomsDeclarees.has(s.geometrie_ref)) err(f.nom, `${ou} : geometrie_ref « ${s.geometrie_ref} » introuvable (ni fichier, ni geometries_a_creer)`)
      else if (!g) avert(f.nom, `${ou} : géométrie pas encore tracée (${s.geometrie_ref})`)
      else if (String(g.statut).startsWith('provisoire')) provisoires.push(s.geometrie_ref)
    }
    else avert(f.nom, `${ou} : aucune géométrie`)
    const pid = s.proprietes?.parent_id
    if (pid && !entites.has(pid)) err(f.nom, `${ou} : parent_id « ${pid} » introuvable`)
    if (!s.sources?.length) err(f.nom, `${ou} : aucune source (règle : pas de fait sans source)`)
    for (const src of s.sources ?? []) {
      if (!src.source_id) err(f.nom, `${ou} : source sans source_id (ancien format ?)`)
      else if (!registrePour(f.nom).has(src.source_id)) err(f.nom, `${ou} : source_id « ${src.source_id} » absent du registre`)
    }
  }
  intervalles.sort((a, b) => (a.debut < b.debut ? -1 : 1))
  for (let i = 1; i < intervalles.length; i++) {
    if (intervalles[i].debut < intervalles[i - 1].fin) err(f.nom, `${intervalles[i - 1].ou} et ${intervalles[i].ou} se chevauchent`)
  }
  for (const r of e.relations ?? []) {
    if (!RELATIONS_ENTITE.includes(r.type)) err(f.nom, `${id} : type de relation inconnu « ${r.type} »`)
    const cible = r.cible_type === 'entite' ? entites : r.cible_type === 'evenement' ? evenements : null
    if (!cible) err(f.nom, `${id} : cible_type invalide « ${r.cible_type} »`)
    else if (!cible.has(r.cible_id)) err(f.nom, `${id} : relation vers « ${r.cible_id} » introuvable`)
  }
}

// --- 3. Événements ---
for (const [id, { ev, f }] of evenements) {
  if (!RE_ID_EVENEMENT.test(id)) err(f.nom, `${id} : format d'ID invalide (annee-pays-motcle-titre)`)
  if (!RE_DATE.test(ev.date_precise ?? '')) err(f.nom, `${id} : date_precise mal formée`)
  if (ev.date_fin && norm(ev.date_fin) < norm(ev.date_precise)) err(f.nom, `${id} : date_fin avant date_precise`)
  if (!PROFONDEURS.includes(ev.profondeur_affichage)) err(f.nom, `${id} : profondeur_affichage inconnue`)
  if (!NIVEAUX.includes(ev.niveau_importance)) err(f.nom, `${id} : niveau_importance inconnu`)
  for (const pays of ev.pays ?? []) if (!/^[a-z]{2}$/.test(pays)) err(f.nom, `${id} : pays « ${pays} » doit être un code à 2 lettres`)
  if (ev.geographie?.geometrie) verifierGeometrie(f.nom, id, ev.geographie.geometrie)
  for (const r of ev.relations ?? []) {
    if (!RELATIONS_EVENEMENT.includes(r.type)) err(f.nom, `${id} : type de relation inconnu « ${r.type} »`)
    const cible = r.cible_type === 'entite' ? entites : evenements
    if (!cible.has(r.cible_id)) err(f.nom, `${id} : relation vers « ${r.cible_id} » introuvable`)
  }
  if (!ev.sources?.length) err(f.nom, `${id} : aucune source`)
  for (const src of ev.sources ?? []) if (!registrePour(f.nom).has(src.source_id)) err(f.nom, `${id} : source_id « ${src.source_id} » absent du registre`)
}

// --- 4. Bilan ---
console.log(`\nAtlas — validation du corpus : ${entites.size} entités, ${evenements.size} événements, ${geometries.size} géométries, ${fichiers.length} fichiers\n`)
if (provisoires.length) console.log(`ℹ  ${provisoires.length} géométrie(s) PROVISOIRE(S), à confirmer par une source A/B (voir points_a_verifier dans chaque fichier)\n`)
if (avertissements.length) console.log(`⚠  ${avertissements.length} avertissement(s)\n` + avertissements.map((a) => `   - ${a}`).join('\n') + '\n')
if (erreurs.length) { console.log(`✗  ${erreurs.length} erreur(s)\n` + erreurs.map((e) => `   - ${e}`).join('\n')); process.exit(1) }
console.log('✓  Aucune erreur.')
