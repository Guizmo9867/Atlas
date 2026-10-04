"""Fusion au registre des réponses d'Ether au lot villes 1.6 (cycle 2, remise du 03/10/2026). À lancer UNE fois, après
fusion_sources_1_5_cycle3.py (v1.20 -> v1.21).
Delta : data/sources/deltas_ether/2026-10-03_villes_1-6_reponses_cycle2_delta.json (17 compléments : 12 pour Q16-01, 5 répertoires pour Q16-02).
Relecture : data/sources/verifications_claude/2026-10-04_villes_1-6_cycle2.json (WebFetch seul pour les adresses ; images de pages
déposées par Ether lues par Claude pour les répertoires et le livre LOC).
Règles : cibles/usages par union ; localisateur d'Ether repris (l'ancien gardé dans les notes) ; complement_ether_cycle2_documentaire conservé.
- « faible » devient « non_verifiee » quand la relecture montre que l'outil n'atteint pas le passage (texte tronqué, page d'accueil).
- Liens toujours en erreur 404 pour l'outil : « lien_casse » gardé (Ether les lit dans son navigateur : Guizmo peut trancher sur la page des sources).
- Répertoires administratifs et LOC : relations relues ville par ville -> confirmations_claude (rôles relus) ; statut au plus « limite ».
"""
import json, pathlib
RACINE = pathlib.Path(__file__).resolve().parents[2]
R = RACINE / 'data/sources/atlas_registre_sources.json'
reg = json.load(open(R, encoding='utf-8'))
assert reg['metadata']['version'] == '1.20', 'ordre des fusions ?'
VERIF = 'data/sources/verifications_claude/2026-10-04_villes_1-6_cycle2.json'
delta = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-03_villes_1-6_reponses_cycle2_delta.json', encoding='utf-8'))['sources']
V = json.load(open(RACINE / VERIF, encoding='utf-8'))
verif = {r['id']: r for r in V['resultats']}
par_id = {s['source_id']: s for s in reg['sources']}
ROLES = {'capitale', 'administration', 'rail', 'port_maritime', 'port_fluvial', 'industrie', 'charbon', 'aviation', 'militaire'}
# Livre LOC (3 pages lues sur images) : rôles relus par ville.
LOC = {'ville-mn-nalaikh': ['charbon', 'rail'], 'ville-mn-oulan-bator': ['industrie'], 'ville-mn-tchoibalsan': ['rail'], 'ville-ru-borzia': ['rail']}
relues = {}
for r in V['relations']:
    roles = [x for x in r['roles_confirmes'] if x in ROLES]
    if roles: relues.setdefault(r['source_id'], {})[r['entite_id']] = (roles, r.get('page_imprimee'), r.get('citation', ''))
bilan = {}
for s in delta:
    sid = s['source_id']; x = par_id[sid]; avant = x['verification_claude']; c = s['complement_ether_cycle2_documentaire']
    x['cibles'] = list(dict.fromkeys([*x.get('cibles', []), *s['cibles']]))
    x['usages_atlas'] = list(dict.fromkeys([*x.get('usages_atlas', []), *s['usages_atlas']]))
    loc = c.get('locator') or s['locator']
    if loc != x.get('locator'):
        x['notes'] += f" Ancien localisateur : {x.get('locator')}."
        x['locator'] = loc
    x['complement_ether_cycle2_documentaire'] = c
    note = ''
    if sid in verif:
        v = verif[sid]
        if sid == 'src-loc-mongolie-1991':
            statut = 'limite'
            conf = x.setdefault('confirmations_claude', {})
            for vid, roles in LOC.items():
                conf[vid] = {'roles': roles, 'lecture': 'pages imprimées 137 et 164 (PDF 183 et 210), images déposées par Ether, lues par Claude', 'date': '2026-10-04', 'verification': VERIF}
        elif avant == 'lien_casse':
            statut = 'lien_casse'
        elif v['statut'] == 'non_verifiee' and avant == 'faible':
            statut = 'non_verifiee'
        else:
            statut = v['statut'] if v['statut'] in ('ok', 'limite') else avant
        if v.get('citation') and statut in ('ok', 'limite'): x['resume_passage'] = v['citation']
        note = f" Relecture Claude 04/10/2026 (Q16-01) : {v['commentaire']}"
    else:  # répertoires (Q16-02)
        rel = relues.get(sid, {})
        statut = 'limite' if rel else avant
        conf = x.setdefault('confirmations_claude', {})
        for vid, (roles, page, cit) in rel.items():
            conf[vid] = {'roles': roles, 'lecture': f"page imprimée {page}, image déposée par Ether, lue par Claude : {cit[:300]}", 'date': '2026-10-04', 'verification': VERIF}
        note = f" Relecture Claude 04/10/2026 (Q16-02) : {len(rel)} villes relues sur les images de pages déposées par Ether (rôles par ville dans confirmations_claude) ; les autres villes de la source restent en lecture partielle."
    x['verification_claude'] = statut; bilan[sid] = f'{avant} -> {statut}'
    x['notes'] += f" Réponse d'Ether (cycle 2, 03/10/2026) : localisateur précisé (complement_ether_cycle2_documentaire).{note} (statut : {avant} -> {statut})."
reg['metadata']['version'] = '1.21'
R.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(delta), 'compléments'); [print(' ', k, b, len(par_id[k].get('confirmations_claude', {}))) for k, b in bilan.items()]
