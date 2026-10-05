"""Fusion au registre des réponses d'Ether au lot 1.8, cycle 3 (remise commune du 05/10/2026). À lancer UNE fois,
après fusion_sources_1_9.py (v1.27 -> v1.28).
Delta : data/sources/deltas_ether/2026-10-05_villes_1-8_reponses_cycle3_delta.json (5 ajouts, 1 complément : src-18-it-re-1946-ligne89).
Relecture : data/sources/verifications_claude/2026-10-05_villes_1-8_cycle3.json (pages en ligne par WebFetch ; page 36 d'EX LIBRIS
et captures vue2/vue3 du rapport RE lues par Claude, hors dépôt). Règles : outils/villes/remise_ether_2026_10_05.py.
"""
import json, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from remise_ether_2026_10_05 import RACINE, fusionner, attendus_par_source, roles_usage
R = RACINE / 'data/sources/atlas_registre_sources.json'
reg = json.load(open(R, encoding='utf-8'))
delta = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-05_villes_1-8_reponses_cycle3_delta.json', encoding='utf-8'))['sources']
ops = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-05_villes_1-8_corrections_cycle3_ether.json', encoding='utf-8'))['corrections']
lot = json.load(open(RACINE / 'data/snapshot0/villes_1-8_balkans_grece_italie.json', encoding='utf-8'))
roles_ville = {e['entite_id']: set(e['etats'][0]['proprietes']['roles']) for e in lot['entites']}
att = attendus_par_source([lot])
for o in ops:
    for a in o.get('sources_a_ajouter', []):
        att.setdefault((a['source_id'], o['entite_id']), set()).update(set(roles_usage(a['usage'])) & roles_ville[o['entite_id']])
ajouts = [s for s in delta if s.get('operation_registre') == 'ajouter']
completes = [s for s in delta if s.get('operation_registre') != 'ajouter']
bilan = fusionner(reg, ajouts, completes, 'data/sources/verifications_claude/2026-10-05_villes_1-8_cycle3.json', 'villes 1.8, cycle 3',
                  'complement_ether_cycle3_2026_10_05', att, '1.27', '1.28')
R.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for k, b in bilan.items(): print(' ', k, b)
print(len(reg['sources']), 'sources (v1.28)')
