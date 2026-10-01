"""Fusion au registre des 58 sources du lot villes 1.4 (Ether, 01/10/2026). À lancer UNE fois (v1.11 -> v1.12).
Fiches : delta JSON d'Ether ; statut : relecture de Claude (data/sources/verifications_claude/2026-10-01_villes_1-4.json).
"""
import json, pathlib
RACINE = pathlib.Path(__file__).resolve().parents[2]
R = RACINE / 'data/sources/atlas_registre_sources.json'
reg = json.load(open(R, encoding='utf-8'))
assert reg['metadata']['version'] == '1.11', 'fusion déjà faite ?'
delta = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-01_villes_1-4_delta.json', encoding='utf-8'))['sources']
verif = {r['id']: r for r in json.load(open(RACINE / 'data/sources/verifications_claude/2026-10-01_villes_1-4.json', encoding='utf-8'))['resultats']}
ids = {s['source_id'] for s in reg['sources']}; urls = {s['url'] for s in reg['sources']}
for s in delta:
    assert s['source_id'] not in ids and s['url'] not in urls, s['source_id']
    v = verif[s['source_id']]
    reg['sources'].append({
        'source_id': s['source_id'], 'niveau': s['niveau'], 'type_source': s['type_source'], 'titre': s['titre'],
        'institution': s['institution'], 'url': s['url'], 'date_consultation': s['date_consultation'], 'periode_couverte': [], 'zones': [],
        'usages_atlas': s['usages_atlas'], 'cibles': s['cibles'], 'locator': s['locator'],
        'resume_passage': v['citation'] if v['statut'] in ('ok', 'limite') else '', 'archive_locale': None,
        'verification_claude': v['statut'], 'verification_ether': s.get('verification'),
        'notes': f"Proposée par Ether (villes 1.4, 01/10/2026). Note d'Ether : {s.get('note', '')} Relecture Claude 01/10/2026 : {v['commentaire']}",
    })
reg['metadata']['version'] = '1.12'
R.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(reg['sources']), 'sources (v1.12)')
