"""Villes 1.9, cycle 3 d'Ether (06/10/2026) : réponse à Q19-03 (sources de l'audit transversal 1.x).

Remise : 8 compléments de sources existantes (data/sources/deltas_ether/2026-10-06_villes_1-9_sources_reponses_cycle3_delta_ether.json)
et 19 relations déjà présentes sur 17 villes (…_corrections_cycle3_ether.json), avec 15 captures lues par Claude
(relecture : data/sources/verifications_claude/2026-10-06_villes_1-9_cycle3.json ; captures hors dépôt, dossier d'échange).

1. Registre v1.30 -> v1.31 (une seule fois) : cibles en union, localisateur d'Ether, statut selon la relecture
   (« ok » si toutes les villes citantes sont prouvées ; sinon « limite » + confirmations_claude pour les villes relues).
   Jeumont : aucune pièce, statut inchangé. Hendaye : rail seul (frontalier non prouvé, R19-C3-01).
2. Villes (lot 1.0 et compléments de l'audit) : pour chaque relation, localisateur et usage d'Ether repris, mention de preuve
   selon le registre ; rôles prouvés retirés de « À renforcer » (rien d'autre retiré, aucun rôle ajouté) ;
   note de Namur : pont ferroviaire sur la Meuse hors service au Snapshot.
Idempotent pour l'étape 2. À relancer après appliquer_audit_1x.py (lot 1.0) et construire_villes_audit_1x.py si ces lots
sont reconstruits, puis appliquer_validations_guizmo.py.
"""
import json, pathlib, re
RACINE = pathlib.Path(__file__).resolve().parents[2]
D = 'data/sources/deltas_ether/2026-10-06_villes_1-9_'
VERIF = 'data/sources/verifications_claude/2026-10-06_villes_1-9_cycle3.json'
delta = json.load(open(RACINE / (D + 'sources_reponses_cycle3_delta_ether.json'), encoding='utf-8'))['sources']
ops = json.load(open(RACINE / (D + 'corrections_cycle3_ether.json'), encoding='utf-8'))['corrections']
verif = {r['id']: r for r in json.load(open(RACINE / VERIF, encoding='utf-8'))['resultats']}
R = RACINE / 'data/sources/atlas_registre_sources.json'
reg = json.load(open(R, encoding='utf-8'))
P = {s['source_id']: s for s in reg['sources']}
ETIQ = "Villes 1.9 cycle 3 d'Ether (06/10/2026)"

if reg['metadata']['version'] == '1.30':
    for s in delta:
        sid = s['source_id']; x = P[sid]; avant = x['verification_claude']
        x['cibles'] = list(dict.fromkeys([*x.get('cibles', []), *s.get('cibles', [])]))
        x['usages_atlas'] = list(dict.fromkeys([*x.get('usages_atlas', []), *s.get('usages_atlas', [])]))
        comp = {k: v for k, v in s.items() if k.startswith('complement_')}
        x['complement_ether_cycle3_2026_10_06'] = {'locator': s.get('locator'), 'note': s.get('note'), **{k: v for c in comp.values() for k, v in (c.items() if isinstance(c, dict) else [('texte', c)])}}
        x['notes'] = (x.get('notes') or '') + f" Complément d'Ether ({ETIQ}) : localisateur « {s.get('locator')} »."
        v = verif.get(sid)
        if not v:
            x['notes'] += ' Aucune pièce lisible remise : statut inchangé.'; print(' ', sid, avant, '(inchangé)'); continue
        if s.get('locator'): x['locator'] = s['locator']
        conf = x.setdefault('confirmations_claude', {})
        for vid, roles in v['villes_prouvees'].items():
            anc = conf.get(vid)
            if anc and anc['roles'] == 'usage': continue
            conf[vid] = {'roles': sorted(set(roles) | set(anc['roles'] if anc else [])),
                         'lecture': f"relu par Claude sur capture d'Ether ({ETIQ}) : {v['citation'][:300]}", 'date': '2026-10-06', 'verification': VERIF}
        if not conf: del x['confirmations_claude']
        statut = v['statut'] if v['statut'] == 'ok' or avant == 'ok' else 'limite'
        if statut == 'ok' and avant != 'ok': x['resume_passage'] = v['citation'][:1500]
        x['verification_claude'] = statut
        x['notes'] += f" Relecture Claude 06/10/2026 (captures d'Ether, hors dépôt) : {v['commentaire'][:1200]} (statut : {avant} -> {statut})."
        print(' ', sid, avant, '->', statut)
    reg['metadata']['version'] = '1.31'
    R.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(len(reg['sources']), 'sources (v1.31)')

def mention(fiche, vid):
    if fiche['verification_claude'] == 'ok': return ''
    c = fiche.get('confirmations_claude', {}).get(vid)
    if c: return ' (page relue par Claude pour cette ville)' if c['roles'] == 'usage' else f" (page relue par Claude pour cette ville : {', '.join(c['roles'])})"
    return ' (non vérifiée par Claude)' if fiche['verification_claude'] in ('non_verifiee', 'lien_casse') else ' (lecture partielle)'

NAMUR = (" Pont ferroviaire sur la Meuse à Namur détruit le 24/12/1944, rouvert le 05/01/1945 : hors service au Snapshot "
         "(un pont, pas tout le trafic de la ville ; Ruppenthal II-5, p.155–156).")
MENTION = (f"{ETIQ} : 19 relations de l'audit 1.x précisées (localisateur et usage d'Ether) après lecture par Claude de 15 captures "
           "(Ruppenthal I-3, II-4, II-5 ; SNCF Patrimoine ; port de Bastia ; CAUE Dijon ; Hendaye) ; rôles prouvés retirés de « À renforcer » ; "
           "rien d'autre retiré, aucun rôle ajouté (outils/villes/integrer_1_9_cycle3.py).")
RENF = re.compile(r' À renforcer : ([^.]*)\.')
faits = []
for nom in ('villes_1-0_france_benelux_iles_britanniques.json', 'villes_1-x_audit_complements.json'):
    F = RACINE / 'data/snapshot0' / nom
    brut = F.read_text(encoding='utf-8'); L = json.loads(brut)
    retrait = len(brut.split('\n')[1]) - len(brut.split('\n')[1].lstrip(' ')) or 1
    touche = False
    for e in L['entites']:
        vid = e['entite_id']; mes = [o for o in ops if o['entite_id'] == vid]
        if not mes: continue
        touche = True; et = e['etats'][0]; p = et['proprietes']; prouves = set()
        for o in mes:
            rel = [s for s in et['sources'] if s['source_id'] == o['source_id']]
            assert len(rel) == 1, (vid, o['source_id'], len(rel))
            fiche = P[o['source_id']]
            tete, _, reste = o['usage_propose_apres_relecture'].partition(' — ')
            roles = [r for r in o['roles_concernes']]
            rel[0]['locator'] = o['locator']
            rel[0]['usage'] = ', '.join(roles) + ' — ' + reste + mention(fiche, vid)
            c = fiche.get('confirmations_claude', {}).get(vid)
            if fiche['verification_claude'] == 'ok' or (c and c['roles'] == 'usage'): prouves |= set(roles)
            elif c: prouves |= set(c['roles']) & set(roles)
            faits.append(f"{vid} {o['source_id']}")
        m = RENF.search(p['note'])
        if m and prouves:
            r2 = [r.strip() for r in m.group(1).split(',') if r.strip() not in prouves]
            p['note'] = p['note'].replace(m.group(0), f" À renforcer : {', '.join(r2)}." if r2 else '')
        if vid == 'ville-be-namur' and NAMUR.strip() not in p['note']:
            p['note'] = p['note'].rstrip() + NAMUR
    if touche:
        corr = L['metadata_lot'].setdefault('integration', {}).setdefault('corrections', [])
        if MENTION not in corr: corr.append(MENTION)
        F.write_text(json.dumps(L, ensure_ascii=False, indent=retrait) + ('\n' if brut.endswith('\n') else ''), encoding='utf-8')
print(len(faits), 'relations mises à jour')
assert len(faits) == len(ops) == 19
