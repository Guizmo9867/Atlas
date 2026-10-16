"""Villes 1.10, cycle 2 (réponses d'Ether du 16/10/2026 à Q110-01 et Q110-02) : fusion au registre. À lancer UNE fois (v1.37 -> v1.38).
Delta : data/sources/deltas_ether/2026-10-16_villes_1-10_cycle2_delta.json (30 compléments, aucune source nouvelle).
Relecture : data/sources/verifications_claude/2026-10-16_villes_1-10_cycle2.json (pièces locales d'Ether : copies HTML à empreinte
contrôlée et captures lues par Claude ; pas de nouvelle URL). Les champs d'Ether déjà au registre ne sont pas écrasés ; le complément
d'Ether est gardé sous complement_ether_cycle2 ; seul l'avis de Claude change, avec une phrase dans les notes.
"""
import json, pathlib
RACINE = pathlib.Path(__file__).resolve().parents[2]
R = RACINE / 'data/sources/atlas_registre_sources.json'
reg = json.load(open(R, encoding='utf-8'))
assert reg['metadata']['version'] == '1.37', 'ordre des fusions ?'
delta = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-16_villes_1-10_cycle2_delta.json', encoding='utf-8'))['sources']
V = {r['id']: r for r in json.load(open(RACINE / 'data/sources/verifications_claude/2026-10-16_villes_1-10_cycle2.json', encoding='utf-8'))['resultats']}
par_id = {s['source_id']: s for s in reg['sources']}
bilan = {}
for s in delta:
    sid = s['source_id']; assert s['operation_registre'] == 'completer' and sid in par_id, sid
    x = par_id[sid]
    x['complement_ether_cycle2'] = s.get('complement_ether_cycle2')
    x['preuves_ether'] = x.get('preuves_ether', []) + [p for p in s.get('preuves_ether', []) if p not in x.get('preuves_ether', [])]
    if s.get('locator') and s['locator'] != x.get('locator'):
        x['locator_ether_cycle2'] = s['locator']
    v = V.get(sid)
    if not v:
        x['notes'] += " Cycle 2 (16/10/2026) : attribution précisée par Ether (avant-propos de Claude Borcard) ; avis « ok » de Claude inchangé."
        continue
    avant = x.get('verification_claude')
    x['verification_claude'] = v['statut']
    if not x.get('resume_passage'): x['resume_passage'] = v['citation']
    x['notes'] += f" Relecture Claude cycle 2 (16/10/2026, pièce locale d'Ether, pas le site en ligne) : {v['commentaire']} Avis : {avant} -> {v['statut']}."
    bilan[f'{avant}->{v["statut"]}'] = bilan.get(f'{avant}->{v["statut"]}', 0) + 1
reg['metadata']['version'] = '1.38'
R.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(delta), 'compléments', bilan, ';', len(reg['sources']), 'sources (v1.38)')
