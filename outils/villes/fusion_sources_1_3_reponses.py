"""Fusion au registre des 6 sources de la réponse d'Ether au lot villes 1.3 (01/10/2026). À lancer UNE fois.
Sources : data/sources/deltas_ether/2026-10-01_villes_1-3_reponses_delta.json (S44 complétée + 5 ajouts) ;
statut : relecture de Claude (data/sources/verifications_claude/2026-10-01_villes_1-3_reponses.json).
"""
import json, pathlib
RACINE = pathlib.Path(__file__).resolve().parents[2]
R = RACINE / 'data/sources/atlas_registre_sources.json'
reg = json.load(open(R, encoding='utf-8'))
assert reg['metadata']['version'] == '1.12', 'fusion déjà faite ?'
delta = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-01_villes_1-3_reponses_delta.json', encoding='utf-8'))
verif = {r['id']: r for r in json.load(open(RACINE / 'data/sources/verifications_claude/2026-10-01_villes_1-3_reponses.json', encoding='utf-8'))['resultats']}
par_id = {s['source_id']: s for s in reg['sources']}; urls = {s['url'] for s in reg['sources']}
for s in delta['sources']:
    v = verif[s['source_id']]
    relecture = f"Relecture Claude 01/10/2026 : {v['commentaire']}"
    ve = {'statut': s['verification']['statut'], 'passages': s['verification']['passages']}
    if s['operation_registre'] == 'completer_fiche_existante':
        x = par_id[s['source_id']]
        x.update({'titre': s['titre'], 'locator': s['locator'], 'usages_atlas': s['usages_atlas'], 'verification_claude': v['statut'],
                  'resume_passage': v['citation'] if v['statut'] in ('ok', 'limite') else '', 'verification_ether': ve})
        x['notes'] = x['notes'].split(' Relecture Claude')[0] + f" Complétée par Ether le 01/10/2026 (réponse aux questions du lot 1.3) : {s['note']} {relecture}"
        continue
    assert s['source_id'] not in par_id and s['url'] not in urls, s['source_id']
    reg['sources'].append({
        'source_id': s['source_id'], 'niveau': s['niveau'], 'type_source': s['type_source'], 'titre': s['titre'],
        'institution': s['institution'], 'url': s['url'], 'date_consultation': s['date_consultation'], 'periode_couverte': [], 'zones': [],
        'usages_atlas': s['usages_atlas'], 'cibles': s['cibles'], 'locator': s['locator'],
        'resume_passage': v['citation'] if v['statut'] in ('ok', 'limite') else '', 'archive_locale': None,
        'verification_claude': v['statut'], 'verification_ether': ve,
        'notes': f"Proposée par Ether (réponse aux questions du lot villes 1.3, 01/10/2026). Limite annoncée par Ether : {s['note']} {relecture}",
    })
par_id['src-13-hu-miskolc-fusion']['url'] += '#page=102'  # lien direct vers la page citée
reg['metadata']['version'] = '1.13'
R.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(reg['sources']), 'sources (v1.13)')
