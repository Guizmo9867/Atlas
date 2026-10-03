"""Fusion au registre des réponses d'Ether au lot villes 1.5 (cycle 2, 03/10/2026). À lancer UNE fois (v1.17 -> v1.18).
Delta : data/sources/deltas_ether/2026-10-03_villes_1-5_reponses_cycle2_delta.json (13 compléments : 11 sources Q15-03, Kichinev, Soumy).
Relecture : data/sources/verifications_claude/2026-10-03_villes_1-6.json (mêmes sous-agents que le lot 1.6, WebFetch seul).
Règles : cibles/usages par union ; localisateur d'Ether repris (l'ancien est gardé dans les notes) ; verification_ether_cycle2 conservé ;
verification_claude ne monte jamais sur la seule relecture d'Ether. « faible » devient « non_verifiee » quand la relecture montre
que l'outil n'a lu qu'un début de page (passage pas atteint, et non absent).
"""
import json, pathlib
RACINE = pathlib.Path(__file__).resolve().parents[2]
R = RACINE / 'data/sources/atlas_registre_sources.json'
reg = json.load(open(R, encoding='utf-8'))
assert reg['metadata']['version'] == '1.17', 'fusion déjà faite ?'
delta = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-03_villes_1-5_reponses_cycle2_delta.json', encoding='utf-8'))['sources']
verif = {r['id']: r for r in json.load(open(RACINE / 'data/sources/verifications_claude/2026-10-03_villes_1-6.json', encoding='utf-8'))['resultats']}
par_id = {s['source_id']: s for s in reg['sources']}
TRONQUEES = {'src-karelia-patrimoine-guerre-1941-1945', 'src-belomorsk-bibliotheque-gare-2024', 'src-rushydro-ouglitch-histoire-2015',
             'src-jdv-tome3-bielorussie-1944', 'src-grodno-encyclopedie-1989-1944', 'src-jdv-tome3-carpates-kertch-1944'}
for s in delta:
    x = par_id[s['source_id']]; v = verif[s['source_id']]; avant = x['verification_claude']
    x['cibles'] = list(dict.fromkeys([*x.get('cibles', []), *s['cibles']]))
    x['usages_atlas'] = list(dict.fromkeys([*x.get('usages_atlas', []), *s['usages_atlas']]))
    if s['locator'] != x.get('locator'):
        x['notes'] += f" Ancien localisateur : {x.get('locator')}."
        x['locator'] = s['locator']
    x['verification_ether_cycle2'] = s['verification_ether_cycle2']
    if s['source_id'] in TRONQUEES and avant == 'faible':
        x['verification_claude'] = 'non_verifiee'
    if v['statut'] == 'ok' and avant != 'ok':
        x['verification_claude'] = 'ok'; x['resume_passage'] = v['citation']
    x['notes'] += (f" Réponse d'Ether (cycle 2, 03/10/2026, Q15-03) : {s['verification_ether_cycle2'].get('constat') or s['verification_ether_cycle2'].get('limite', '')}"
                   + (f" Note d'Ether : {s['note']}" if s['source_id'] == 'src-kichinev-ordre-173-19440824' else '')
                   + f" Relecture Claude 03/10/2026 : {v['commentaire']} (statut : {avant} -> {x['verification_claude']}).")
reg['metadata']['version'] = '1.18'
R.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(delta), 'compléments ;', {k: par_id[k]['verification_claude'] for k in [s['source_id'] for s in delta]})
