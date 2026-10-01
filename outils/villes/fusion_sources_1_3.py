"""Fusion au registre des 53 sources du lot villes 1.3 (Ether, 01/10/2026). À lancer UNE fois.
Sources : extrait du document d'Ether (data/sources/deltas_ether/2026-10-01_villes_1-3_extrait_du_brief.json) ;
statut : relecture de Claude (data/sources/verifications_claude/2026-10-01_villes_1-3.json).
"""
import json, pathlib
RACINE = pathlib.Path(__file__).resolve().parents[2]
R = RACINE / 'data/sources/atlas_registre_sources.json'
reg = json.load(open(R, encoding='utf-8'))
assert reg['metadata']['version'] == '1.9', 'fusion déjà faite ?'
ext = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-01_villes_1-3_extrait_du_brief.json', encoding='utf-8'))
verif = {r['id']: r for r in json.load(open(RACINE / 'data/sources/verifications_claude/2026-10-01_villes_1-3.json', encoding='utf-8'))['resultats']}
ids = {s['source_id'] for s in reg['sources']}; urls = {s['url'] for s in reg['sources']}
for s in ext['sources']:
    assert s['source_id'] not in ids and s['url'] not in urls, s['source_id']
    v = verif[s['source_id']]
    reg['sources'].append({
        'source_id': s['source_id'], 'niveau': s['niveau'], 'type_source': 'notice_historique_institutionnelle', 'titre': s['titre'],
        'institution': s['institution'], 'url': s['url'], 'date_consultation': '2026-10-01', 'periode_couverte': [], 'zones': [],
        'usages_atlas': ['rôle de ville au 01/01/1945 (ratissage villes 1.3)'], 'cibles': s['cibles'], 'locator': s['locator'],
        'resume_passage': v['citation'] if v['statut'] in ('ok', 'limite') else '', 'archive_locale': None,
        'verification_claude': v['statut'],
        'notes': f"Proposée par Ether (villes 1.3, 01/10/2026, réf. S{s['S']}). Limite annoncée par Ether : {s['limite']} Relecture Claude 01/10/2026 : {v['commentaire']}",
    })
reg['metadata']['version'] = '1.10'
R.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(reg['sources']), 'sources (v1.10)')
