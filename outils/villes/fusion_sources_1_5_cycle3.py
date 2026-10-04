"""Fusion au registre des réponses d'Ether au lot villes 1.5 (cycle 3, remise du 03/10/2026). À lancer UNE fois (v1.19 -> v1.20).
Delta : data/sources/deltas_ether/2026-10-03_villes_1-5_reponses_cycle3_delta.json (8 compléments Q15-03 avec 12 captures).
Relecture : data/sources/verifications_claude/2026-10-04_villes_1-5_cycle3.json (captures d'Ether lues par Claude avec l'outil Read ;
les captures restent dans le dossier d'échange, 01_lots/villes_1-5/, jamais dans le dépôt public).
Règles : cibles/usages par union ; localisateur d'Ether repris (l'ancien gardé dans les notes) ; complement_ether_cycle3 conservé ;
statut = résultat de la lecture des captures. Deux sources servent aussi au lot 1.7 pour d'autres passages
(src-rosmorport-taganrog-reparation-1943, src-jdv-tome3-bielorussie-1944) : statut « limite » (seul le passage 1.5 est relu)
et villes prouvées notées dans confirmations_claude (voir confirmations_claude.py).
"""
import json, pathlib
RACINE = pathlib.Path(__file__).resolve().parents[2]
R = RACINE / 'data/sources/atlas_registre_sources.json'
reg = json.load(open(R, encoding='utf-8'))
assert reg['metadata']['version'] == '1.19', 'fusion déjà faite ?'
VERIF = 'data/sources/verifications_claude/2026-10-04_villes_1-5_cycle3.json'
delta = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-03_villes_1-5_reponses_cycle3_delta.json', encoding='utf-8'))['sources']
verif = {r['id']: r for r in json.load(open(RACINE / VERIF, encoding='utf-8'))['resultats']}
par_id = {s['source_id']: s for s in reg['sources']}
PARTAGEES_1_7 = {'src-rosmorport-taganrog-reparation-1943', 'src-jdv-tome3-bielorussie-1944'}
for s in delta:
    sid = s['source_id']; x = par_id[sid]; v = verif[sid]; avant = x['verification_claude']
    x['cibles'] = list(dict.fromkeys([*x.get('cibles', []), *s['cibles']]))
    x['usages_atlas'] = list(dict.fromkeys([*x.get('usages_atlas', []), *s['usages_atlas']]))
    if s['locator'] != x.get('locator'):
        x['notes'] += f" Ancien localisateur : {x.get('locator')}."
        x['locator'] = s['locator']
    x['complement_ether_cycle3'] = s['complement_ether_cycle3']
    statut = 'limite' if (sid in PARTAGEES_1_7 and v['statut'] == 'ok') else v['statut']
    x['verification_claude'] = statut
    if v.get('citation'): x['resume_passage'] = v['citation']
    if statut != 'ok':
        conf = x.setdefault('confirmations_claude', {})
        for vid in v.get('villes_prouvees', []):
            conf[vid] = {'roles': 'usage', 'lecture': "capture de la page déposée par Ether (cycle 3), lue par Claude", 'date': '2026-10-04', 'verification': VERIF}
    images = ', '.join(i['fichier'] for i in s['complement_ether_cycle3']['images'])
    x['notes'] += (f" Réponse d'Ether (cycle 3, 03/10/2026, Q15-03) : captures {images} (dossier d'échange, 01_lots/villes_1-5/, hors dépôt)."
                   f" Relecture Claude 04/10/2026 sur ces captures : {v['commentaire']} (statut : {avant} -> {statut}"
                   + (" ; seul le passage du lot 1.5 est relu, villes prouvées dans confirmations_claude" if statut != v['statut'] else '') + ").")
reg['metadata']['version'] = '1.20'
R.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(delta), 'compléments ;', {s['source_id']: par_id[s['source_id']]['verification_claude'] for s in delta})
