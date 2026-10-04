"""Fusion au registre des réponses d'Ether au lot 1.6 (cycle 3) et au lot 1.7 (cycle 2), remise commune du 04/10/2026.
À lancer UNE fois, après fusion_sources_1_3_guizmo_decin.py (v1.23 -> v1.24).
Deltas : data/sources/deltas_ether/2026-10-04_villes_1-6_reponses_cycle3_delta.json (8 compléments)
         data/sources/deltas_ether/2026-10-04_villes_1-7_reponses_cycle2_delta.json (6 compléments ; src-shpl-admin1940 commun : union).
Relectures : data/sources/verifications_claude/2026-10-04_villes_1-6_cycle3.json et 2026-10-04_villes_1-7_cycle2.json
(captures et images de pages déposées par Ether, lues par Claude avec l'outil Read ; elles restent dans le dossier d'échange, hors dépôt).
Règles :
- cibles/usages par union ; complément d'Ether conservé sous son nom de champ ; localisateur d'Ether repris pour les sources
  d'une seule ville (l'ancien gardé dans les notes), jamais pour les répertoires partagés entre lots ;
- captures : statut « ok » seulement si la capture prouve tous les rôles que chaque ville attend de la source ; sinon
  « limite » et villes/rôles relus dans confirmations_claude ; « faible » ou rien de prouvé : statut inchangé ;
- pages de répertoires (Q16-02, Q17-02) : rôles relus ville par ville -> confirmations_claude (union avec les anciennes) ;
  une gare à plus de 0 km ne confirme pas le rail.
"""
import json, pathlib
RACINE = pathlib.Path(__file__).resolve().parents[2]
R = RACINE / 'data/sources/atlas_registre_sources.json'
reg = json.load(open(R, encoding='utf-8'))
assert reg['metadata']['version'] == '1.23', 'ordre des fusions ?'
par_id = {s['source_id']: s for s in reg['sources']}
LOTS = [json.load(open(RACINE / f'data/snapshot0/{n}.json', encoding='utf-8')) for n in ('villes_1-6_asie_sovietique_mongolie', 'villes_1-7_caucase_turquie')]
ROLES = {'capitale', 'administration', 'rail', 'port_maritime', 'port_fluvial', 'industrie', 'charbon', 'aviation', 'militaire', 'mines', 'peche'}
usages_ville = {}  # (source, ville) -> rôles attendus
for L in LOTS:
    for e in L['entites']:
        for s in e['etats'][0]['sources']:
            usages_ville.setdefault((s['source_id'], e['entite_id']), set()).update(t.strip() for t in s['usage'].split(' (')[0].split(','))
TRAVAUX = [('1-6', 'cycle3', 'complement_ether_cycle3_2026_10_04', 'Q16-01/Q16-02'), ('1-7', 'cycle2', 'complement_ether_cycle2_2026_10_04', 'Q17-01/Q17-02')]
PARTAGEES = {'src-shpl-admin1940', 'src-neb-admin1944-supplement'}
bilan = {}
for lot, cyc, champ, q in TRAVAUX:
    VERIF = f'data/sources/verifications_claude/2026-10-04_villes_{lot}_{cyc}.json'
    V = json.load(open(RACINE / VERIF, encoding='utf-8'))
    delta = json.load(open(RACINE / f'data/sources/deltas_ether/2026-10-04_villes_{lot}_reponses_{cyc}_delta.json', encoding='utf-8'))['sources']
    verif = {r['id']: r for r in V['resultats']}
    for s in delta:
        sid = s['source_id']; x = par_id[sid]; avant = x['verification_claude']
        x['cibles'] = list(dict.fromkeys([*x.get('cibles', []), *s['cibles']]))
        x['usages_atlas'] = list(dict.fromkeys([*x.get('usages_atlas', []), *s['usages_atlas']]))
        c = s[champ]
        if sid not in PARTAGEES and c.get('locator') and c['locator'] != x.get('locator'):
            x['notes'] += f" Ancien localisateur : {x.get('locator')}."
            x['locator'] = c['locator']
        x[champ] = c
        images = ', '.join(i['fichier'] for i in c.get('images_locales', c.get('images', []))) or 'voir index'
        x['notes'] += f" Réponse d'Ether (lot {lot.replace('-', '.')}, {cyc.replace('cycle', 'cycle ')}, 04/10/2026, {q}) : captures {images} (dossier d'échange, 01_lots/villes_{lot}/, hors dépôt)."
        if sid in verif:
            v = verif[sid]; prouvees = {k: set(r) for k, r in v.get('villes_prouvees', {}).items() if r}
            if v['statut'] in ('ok', 'limite') and prouvees:
                complet = all(usages_ville.get((sid, vid), set()) & ROLES <= prouvees.get(vid, set()) for vid in x['cibles'] if (sid, vid) in usages_ville)
                statut = 'ok' if v['statut'] == 'ok' and complet else 'limite'
                if statut == 'limite':
                    conf = x.setdefault('confirmations_claude', {})
                    for vid, roles in prouvees.items():
                        conf[vid] = {'roles': sorted(roles), 'lecture': f"capture déposée par Ether (lot {lot.replace('-', '.')}, {cyc}), lue par Claude", 'date': '2026-10-04', 'verification': VERIF}
                if v.get('citation'): x['resume_passage'] = v['citation'][:1500]
            else:
                statut = avant
            x['verification_claude'] = statut
            x['notes'] += f" Relecture Claude 04/10/2026 sur ces captures : {v['commentaire'][:1200]} (statut : {avant} -> {statut})."
            bilan[sid] = f'{avant} -> {statut}'
    # pages de répertoires relues ville par ville
    rel = {}
    for r in V['relations']:
        roles = [t for t in r['roles_confirmes'] if t in ROLES]
        k = (r['source_id'], r['entite_id'])
        a = rel.setdefault(k, {'roles': set(), 'pages': set(), 'cit': []})
        a['roles'] |= set(roles); a['pages'].add(str(r.get('page_imprimee'))); a['cit'].append(r.get('citation', ''))
    n = 0
    for (sid, vid), a in rel.items():
        if not a['roles']: continue
        conf = par_id[sid].setdefault('confirmations_claude', {})
        anc = conf.get(vid)
        roles = set(a['roles']) | (set(anc['roles']) if anc and anc['roles'] != 'usage' else set())
        if anc and anc['roles'] == 'usage': continue
        conf[vid] = {'roles': sorted(roles), 'lecture': f"page imprimée {'; '.join(sorted(a['pages']))}, image déposée par Ether, lue par Claude : {' | '.join(a['cit'])[:300]}", 'date': '2026-10-04', 'verification': VERIF}
        n += 1
    print(f'lot {lot} {cyc} : {n} villes relues sur pages de répertoire')
reg['metadata']['version'] = '1.24'
R.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for k, b in bilan.items(): print(' ', k, b, len(par_id[k].get('confirmations_claude', {})))
