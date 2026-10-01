"""Les 53 sources du lot 1.3 avaient été versées au registre depuis le document d'Ether (v1.10).
Une fois son delta JSON reçu : on reprend son type de source, ses usages précis et sa trace de lecture,
sans toucher à la relecture de Claude. À lancer UNE fois (registre v1.10 -> v1.11).
"""
import json, pathlib
RACINE = pathlib.Path(__file__).resolve().parents[2]
R = RACINE / 'data/sources/atlas_registre_sources.json'
reg = json.load(open(R, encoding='utf-8'))
assert reg['metadata']['version'] == '1.10'
delta = {s['source_id']: s for s in json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-01_villes_1-3_delta.json', encoding='utf-8'))['sources']}
n = 0
for s in reg['sources']:
    d = delta.get(s['source_id'])
    if not d: continue
    assert d['url'] == s['url'], s['source_id']
    s['type_source'] = d['type_source']
    s['usages_atlas'] = d['usages_atlas']
    s['verification_ether'] = d['verification']
    n += 1
assert n == 53
reg['metadata']['version'] = '1.11'
R.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(n, 'sources enrichies (v1.11)')
