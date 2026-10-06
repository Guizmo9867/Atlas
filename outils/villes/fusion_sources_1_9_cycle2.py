"""Fusion au registre des réponses d'Ether au lot 1.9, cycle 2 (remise commune du 05/10/2026). À lancer UNE fois,
après fusion_sources_1_8_cycle3.py (v1.28 -> v1.29), avant fusion_sources_audit_1x.py.
Delta : data/sources/deltas_ether/2026-10-05_villes_1-9_reponses_cycle2_delta.json (4 ajouts, 12 compléments).
Relecture : data/sources/verifications_claude/2026-10-05_villes_1-9_cycle2.json (pages en ligne par WebFetch ; captures et pages
de PDF déposées par Ether lues par Claude, hors dépôt). Règles : outils/villes/remise_ether_2026_10_05.py.
"""
import json, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from remise_ether_2026_10_05 import RACINE, fusionner, attendus_par_source, roles_usage
R = RACINE / 'data/sources/atlas_registre_sources.json'
reg = json.load(open(R, encoding='utf-8'))
delta = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-05_villes_1-9_reponses_cycle2_delta.json', encoding='utf-8'))['sources']
ops = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-05_villes_1-9_corrections_cycle2_ether.json', encoding='utf-8'))['corrections']
lot = json.load(open(RACINE / 'data/snapshot0/villes_1-9_iberie_marges.json', encoding='utf-8'))
roles_ville = {e['entite_id']: set(e['etats'][0]['proprietes']['roles']) for e in lot['entites']}
att = attendus_par_source([lot])
for o in ops:
    for a in o.get('sources_a_ajouter', []):
        att.setdefault((a['source_id'], o['entite_id']), set()).update(set(roles_usage(a['usage'])) & roles_ville[o['entite_id']])
ajouts = [s for s in delta if s.get('operation_registre') == 'ajouter']
completes = [s for s in delta if s.get('operation_registre') != 'ajouter']
bilan = fusionner(reg, ajouts, completes, 'data/sources/verifications_claude/2026-10-05_villes_1-9_cycle2.json', 'villes 1.9, cycle 2',
                  'complement_ether_cycle2_2026_10_05', att, '1.28', '1.29')
R.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for k, b in bilan.items(): print(' ', k, b)
print(len(reg['sources']), 'sources (v1.29)')
