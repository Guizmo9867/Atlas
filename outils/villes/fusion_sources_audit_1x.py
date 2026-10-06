"""Fusion au registre des sources de l'audit transversal villes 1.x d'Ether (remise commune du 05/10/2026). À lancer UNE fois,
après fusion_sources_1_9_cycle2.py (v1.29 -> v1.30).
Delta : data/sources/deltas_ether/2026-10-05_audit_1x_sources_delta_ether.json (18 ajouts ; complément de src-wikidata = union des cibles).
Relecture : data/sources/verifications_claude/2026-10-05_villes_audit_1x.json (WebFetch seul, sans contournement).
Dans le delta, « usages_atlas » contient la phrase d'Ether : elle est gardée dans « lecture_ether » ; les usages_atlas deviennent les
rôles attendus par les villes qui citent la source (15 villes proposées et 23 relations sur des villes existantes).
"""
import json, sys, pathlib, glob
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from remise_ether_2026_10_05 import RACINE, fusionner, attendus_par_source, roles_usage
R = RACINE / 'data/sources/atlas_registre_sources.json'
reg = json.load(open(R, encoding='utf-8'))
D = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-05_audit_1x_sources_delta_ether.json', encoding='utf-8'))
ops = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-05_audit_1x_corrections_ether.json', encoding='utf-8'))['corrections']
nouvelles = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-05_audit_1x_complements_villes_ether.json', encoding='utf-8'))['proposition_ether']
lots = [json.load(open(f, encoding='utf-8')) for f in sorted(glob.glob(str(RACINE / 'data/snapshot0/villes_1-*.json')))]
roles_ville = {e['entite_id']: set(e['etats'][0]['proprietes']['roles']) for L in lots + [nouvelles] for e in L['entites']}
att = attendus_par_source([nouvelles])
for o in ops:
    for a in o.get('sources_a_ajouter', []):
        att.setdefault((a['source_id'], o['entite_id']), set()).update(set(roles_usage(a['usage'])) & roles_ville[o['entite_id']])
ajouts = []
for s in D['sources_a_ajouter']:
    s = dict(s)
    s['usages_atlas'] = sorted(set().union(*[r for (sid, _), r in att.items() if sid == s['source_id']] or [set()]))
    ajouts.append(s)
bilan = fusionner(reg, ajouts, [], 'data/sources/verifications_claude/2026-10-05_villes_audit_1x.json', 'audit transversal 1.x',
                  'complement_ether_audit_1x_2026_10_05', att, '1.29', '1.30')
wd = next(x for x in reg['sources'] if x['source_id'] == 'src-wikidata')
for c in D['sources_a_completer']:
    assert c['source_id'] == 'src-wikidata'
    avant = len(wd['cibles'])
    wd['cibles'] = list(dict.fromkeys([*wd['cibles'], *[e['entite_id'] for e in nouvelles['entites']]]))
    wd['notes'] = (wd.get('notes') or '') + " Audit 1.x d'Ether (05/10/2026) : 15 villes ajoutées aux cibles (positions recoupées par Claude par SPARQL)."
    bilan['src-wikidata'] = f"cibles {avant} -> {len(wd['cibles'])} (union seulement)"
R.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for k, b in bilan.items(): print(' ', k, b)
print(len(reg['sources']), 'sources (v1.30)')
