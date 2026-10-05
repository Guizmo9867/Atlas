"""Fusion au registre des réponses d'Ether au lot 1.7 (cycle 3) et au lot 1.8 (cycle 2), remise commune du 05/10/2026.
À lancer UNE fois, après fusion_sources_1_8.py (v1.25 -> v1.26).
Deltas : data/sources/deltas_ether/2026-10-05_villes_1-7_reponses_cycle3_delta.json (4 compléments)
         data/sources/deltas_ether/2026-10-05_villes_1-8_reponses_cycle2_delta.json (16 compléments).
Relectures : data/sources/verifications_claude/2026-10-05_villes_1-7_cycle3.json et 2026-10-05_villes_1-8_cycle2.json
(captures déposées par Ether, lues par Claude avec l'outil Read ; pages en ligne relues par WebFetch ; captures hors dépôt).
Règles (mêmes que fusion_sources_1_6_1_7_cycle3.py) :
- cibles/usages par union ; complément d'Ether conservé sous son nom de champ ; localisateur d'Ether repris pour les sources
  d'une seule ville (l'ancien gardé dans les notes), jamais pour les répertoires partagés ;
- statut « ok » seulement si la relecture prouve tous les rôles attendus par chaque ville citée ; sinon « limite » et
  villes/rôles relus dans confirmations_claude (union avec les anciennes) ; « faible » ou rien de prouvé : statut inchangé.
"""
import json, pathlib, re
RACINE = pathlib.Path(__file__).resolve().parents[2]
R = RACINE / 'data/sources/atlas_registre_sources.json'
reg = json.load(open(R, encoding='utf-8'))
assert reg['metadata']['version'] == '1.25', 'ordre des fusions ?'
par_id = {s['source_id']: s for s in reg['sources']}
LOTS = [json.load(open(RACINE / f'data/snapshot0/{n}.json', encoding='utf-8')) for n in ('villes_1-7_caucase_turquie', 'villes_1-8_balkans_grece_italie')]
ROLES = {'capitale', 'administration', 'rail', 'port_maritime', 'port_fluvial', 'industrie', 'charbon', 'aviation', 'militaire', 'mines', 'peche', 'base_navale'}
usages_ville = {}
for L in LOTS:
    for e in L['entites']:
        for s in e['etats'][0]['sources']:
            usages_ville.setdefault((s['source_id'], e['entite_id']), set()).update(t.strip() for t in re.split(r'[,;]', s['usage'].split(' (')[0]))
TRAVAUX = [('1-7', 'cycle3', 'complement_ether_cycle3_2026_10_05', 'Q17-01/Q17-02'), ('1-8', 'cycle2', 'complement_ether_cycle2_2026_10_05', 'Q18-01/Q18-02')]
PARTAGEES = {'src-shpl-admin1940', 'src-neb-admin1944-supplement'}
bilan = {}
for lot, cyc, champ, q in TRAVAUX:
    VERIF = f'data/sources/verifications_claude/2026-10-05_villes_{lot}_{cyc}.json'
    V = json.load(open(RACINE / VERIF, encoding='utf-8'))
    delta = json.load(open(RACINE / f'data/sources/deltas_ether/2026-10-05_villes_{lot}_reponses_{cyc}_delta.json', encoding='utf-8'))['sources']
    verif = {r['id']: r for r in V['resultats']}
    for s in delta:
        sid = s['source_id']; x = par_id[sid]; avant = x['verification_claude']
        x['cibles'] = list(dict.fromkeys([*x.get('cibles', []), *s['cibles']]))
        x['usages_atlas'] = list(dict.fromkeys([*x.get('usages_atlas', []), *s['usages_atlas']])) if s.get('usages_atlas') else x.get('usages_atlas', [])
        c = s[champ]
        if sid not in PARTAGEES and c.get('locator') and c['locator'] != x.get('locator'):
            x['notes'] = x.get('notes', '') + f" Ancien localisateur : {x.get('locator')}."
            x['locator'] = c['locator']
        x[champ] = c
        images = ', '.join(i['fichier'] for i in c.get('images_locales', [])) or 'aucune (lecture en ligne)'
        x['notes'] = x.get('notes', '') + f" Réponse d'Ether (lot {lot.replace('-', '.')}, {cyc.replace('cycle', 'cycle ')}, 05/10/2026, {q}) : captures {images} (dossier d'échange, 01_lots/villes_{lot}/, hors dépôt)."
        v = verif.get(sid)
        if not v: continue
        prouvees = {k: set(r) for k, r in v.get('villes_prouvees', {}).items() if r}
        if v['statut'] in ('ok', 'limite') and prouvees:
            complet = avant != 'limite' or sid not in PARTAGEES
            complet = complet and all(usages_ville.get((sid, vid), set()) & ROLES <= prouvees.get(vid, set()) for vid in x['cibles'] if (sid, vid) in usages_ville)
            statut = 'ok' if v['statut'] == 'ok' and complet else 'limite'
            if statut == 'limite':
                conf = x.setdefault('confirmations_claude', {})
                for vid, roles in prouvees.items():
                    anc = conf.get(vid)
                    if anc and anc['roles'] == 'usage': continue
                    r2 = set(roles) | (set(anc['roles']) if anc else set())
                    conf[vid] = {'roles': sorted(r2), 'lecture': f"capture ou page relue par Claude (lot {lot.replace('-', '.')}, {cyc}) : {v.get('preuves_par_ville', {}).get(vid, '')[:300]}", 'date': '2026-10-05', 'verification': VERIF}
            if v.get('citation') and statut == 'ok': x['resume_passage'] = v['citation'][:1500]
        else:
            statut = avant
        x['verification_claude'] = statut
        x['notes'] += f" Relecture Claude 05/10/2026 : {v['commentaire'][:1200]} (statut : {avant} -> {statut})."
        bilan[sid] = f'{avant} -> {statut}'
reg['metadata']['version'] = '1.26'
R.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for k, b in bilan.items(): print(' ', k, b, len(par_id[k].get('confirmations_claude', {})))
