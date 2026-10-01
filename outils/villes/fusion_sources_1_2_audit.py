"""Fusion au registre du delta de sources de l'audit villes 1.2 (Ether, 01/10/2026). À lancer UNE fois.

- 75 sources nouvelles : ajoutées avec le résultat de la relecture de Claude
  (data/sources/deltas_ether/2026-10-01_villes_1-2_audit_verification_claude.json).
- 35 sources existantes : enrichies sans rien effacer (cibles réunies, statut d'usage et lecture d'Ether ajoutés,
  note d'Ether ajoutée à la suite). Les 7 références non relues prennent date_consultation = null
  (date initiale gardée à part), comme demandé par Ether.
Relancer : python outils/villes/fusion_sources_1_2_audit.py (depuis la racine du dépôt).
"""
import json, pathlib

RACINE = pathlib.Path(__file__).resolve().parents[2]
R = RACINE / 'data/sources/atlas_registre_sources.json'
reg = json.load(open(R, encoding='utf-8'))
delta = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-01_villes_1-2_audit_delta.json', encoding='utf-8'))
verif = {r['id']: r for r in json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-01_villes_1-2_audit_verification_claude.json', encoding='utf-8'))['resultats']}
par_id = {s['source_id']: s for s in reg['sources']}
assert reg['metadata']['version'] == '1.7', 'fusion déjà faite ?'

for s in delta['sources_a_ajouter_si_absentes']:
    sid = s['source_id']
    assert sid not in par_id, sid
    v = verif[sid]
    commentaire = f"Relecture Claude 01/10/2026 : {v['commentaire']}"
    reg['sources'].append({
        'source_id': sid, 'niveau': s['niveau'], 'type_source': s['type_source'], 'titre': s['titre'], 'institution': s['institution'],
        'url': s['url'], 'date_consultation': s['date_consultation'], 'periode_couverte': [], 'zones': [],
        'usages_atlas': s['usages_atlas'], 'cibles': s['cibles'], 'locator': s['locator'],
        'resume_passage': v['citation'] if v['statut'] in ('ok', 'limite') else '',
        'archive_locale': None, 'verification_claude': v['statut'],
        'verification_ether': s.get('verification'),
        'notes': f"Proposée par Ether (audit villes 1.2, 01/10/2026). Note d'Ether : {s['note']} {commentaire}",
    })

for s in delta['sources_a_enrichir_si_presentes_sinon_ajouter']:
    e = par_id[s['source_id']]
    e['cibles'] = list(dict.fromkeys([*e.get('cibles', []), *s.get('cibles', [])]))
    e['usages_atlas'] = list(dict.fromkeys([*e.get('usages_atlas', []), *s.get('usages_atlas', [])]))
    if s.get('statut_usage'): e['statut_usage'] = s['statut_usage']
    if s.get('sources_remplacement'): e['sources_remplacement'] = s['sources_remplacement']
    if 'date_consultation_initialement_declaree' in s:
        e['date_consultation_initiale'] = s['date_consultation_initialement_declaree']
        e['date_consultation'] = None
    if s.get('locator') and not e.get('locator'): e['locator'] = s['locator']
    e['verification_ether'] = s.get('verification')
    e['notes'] = (e.get('notes') or '') + f" Audit Ether 01/10/2026 : {s['note']}"

# Bâle (DHS) : article long, l'extrait lu par Claude s'arrête avant les passages cités par Ether
par_id2 = {s['source_id']: s for s in reg['sources']}
par_id2['src-12a-dhs-basel']['notes'] += " L'article est long : l'extrait que Claude a pu lire (deux essais + un essai ciblé) ne contient ni la chimie ni les ports ; non confirmé, pas infirmé."

reg['metadata']['version'] = '1.8'
R.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(reg['sources']), 'sources au registre (v1.8)')
