"""Outils communs à l'intégration de la remise d'Ether du 05/10/2026 (villes 1.8 cycle 3, villes 1.9 cycle 2, audit 1.x).

- roles_usage(usage) : rôles cités en tête d'un usage (« rail ; ... », « port_maritime/industrie en 1936 », « rail; frontalier — ... ») ;
- appliquer_corrections(entite, operations, registre) : applique à UNE ville les opérations additives d'Ether
  (completer_sources_sans_remplacer, completer_localisateur / corriger_localisateur, remplacement_textuel_cible) :
  * une source n'est ajoutée que si la ville ne la cite pas déjà (sinon la relecture agit par le registre) ;
  * la phrase « note_a_ajouter » d'Ether n'est ajoutée à la note que si la source est confirmée par Claude pour cette ville ;
  * un remplacement de texte n'est fait que si l'ancien texte est trouvé tel quel ;
  * rien n'est retiré (sources, rôles, noms, positions) ;
- fusionner(...) : fusion au registre des fiches nouvelles et des compléments, avec les relectures de Claude.
Règles de statut (comme fusion_sources_1_7_1_8_reponses.py) : « ok » seulement si la relecture prouve tous les rôles attendus
par chaque ville qui cite la source ; sinon « limite » et villes/rôles relus dans confirmations_claude (union avec les anciennes) ;
relecture sans preuve : statut inchangé pour une fiche existante, statut de la relecture pour une fiche nouvelle.
"""
import json, re, glob, pathlib
RACINE = pathlib.Path(__file__).resolve().parents[2]
ROLES = set()
for _f in glob.glob(str(RACINE / 'data/snapshot0/villes_1-*.json')):
    for _e in json.load(open(_f, encoding='utf-8')).get('entites', []):
        ROLES |= set(_e['etats'][0]['proprietes'].get('roles', []))
ROLES |= {'rail', 'port_maritime', 'port_fluvial', 'industrie', 'capitale', 'administration', 'frontalier', 'ferry', 'base_navale',
          'construction_navale', 'siderurgie', 'mines', 'aviation', 'militaire', 'charbon', 'transatlantique'}

def roles_usage(usage):
    tete = re.split(r' — | \(', usage or '')[0]
    return [t for t in dict.fromkeys(x.strip().split(' ')[0] for x in re.split(r'[,;/]', tete)) if t in ROLES]

def confirmee(fiche, vid):
    if not fiche: return set()
    if fiche.get('verification_claude') == 'ok': return {'*'}
    c = fiche.get('confirmations_claude', {}).get(vid)
    if not c: return set()
    return {'*'} if c['roles'] == 'usage' else set(c['roles'])

def appliquer_corrections(e, operations, registre, etiquette):
    et = e['etats'][0]; p = et['proprietes']; faits = []
    for op in operations:
        if op.get('entite_id') != e['entite_id']: continue
        o = op['operation']
        if o == 'completer_sources_sans_remplacer':
            for a in op['sources_a_ajouter']:
                sid = a['source_id']
                if any(s['source_id'] == sid for s in et['sources']):
                    faits.append(f'{sid} déjà citée'); continue
                roles = [r for r in roles_usage(a['usage']) if r in p['roles']]
                et['sources'].append({'source_id': sid, 'locator': a['locator'], 'usage': (', '.join(roles) + ' ; ' if roles else '') + a['usage']})
                faits.append(f'+{sid}')
                n = op.get('note_a_ajouter')
                if n and confirmee(registre.get(sid), e['entite_id']):
                    p['note'] = p['note'].rstrip() + f' {etiquette} : {n}'
        elif o in ('completer_localisateur', 'corriger_localisateur'):
            nouveau = op.get('locator_a_ajouter') or op.get('nouveau')
            for s in et['sources']:
                if s['source_id'] == op['source_id'] and s.get('locator') != nouveau:
                    s['locator'] = nouveau; faits.append(f"localisateur {op['source_id']}")
        elif o == 'remplacement_textuel_cible':
            if op['ancien'] in p['note']:
                p['note'] = p['note'].replace(op['ancien'], op['nouveau']); faits.append('note corrigée')
            else:
                faits.append('remplacement non fait (ancien texte introuvable)')
    return faits

def attendus_par_source(lots, operations=()):
    """(source, ville) -> rôles attendus, d'après les usages des villes (et les ajouts proposés)."""
    att = {}
    for L in lots:
        for e in L['entites']:
            p = e['etats'][0]['proprietes']
            for s in e['etats'][0]['sources']:
                att.setdefault((s['source_id'], e['entite_id']), set()).update(set(roles_usage(s['usage'])) & set(p['roles']))
    return att

def fusionner(reg, ajouts, completes, verif_path, etiquette, champ_complement, attendus, version_avant, version_apres):
    assert reg['metadata']['version'] == version_avant, 'ordre des fusions ?'
    V = json.load(open(RACINE / verif_path, encoding='utf-8'))
    verif = {r['id']: r for r in V['resultats']}
    par_id = {s['source_id']: s for s in reg['sources']}
    bilan = {}
    def confirmer(x, prouvees, v):
        conf = x.setdefault('confirmations_claude', {})
        for vid, roles in prouvees.items():
            anc = conf.get(vid)
            if anc and anc['roles'] == 'usage': continue
            r2 = set(roles) | (set(anc['roles']) if anc else set())
            conf[vid] = {'roles': sorted(r2), 'lecture': f"relu par Claude ({etiquette}) : {(v.get('preuves_par_ville') or {}).get(vid, v.get('citation', ''))[:300]}",
                         'date': '2026-10-05', 'verification': verif_path}
    def statut_de(sid, v, avant, nouvelle):
        prouvees = {k: set(r) for k, r in (v.get('villes_prouvees') or {}).items() if r}
        if v['statut'] not in ('ok', 'limite'): return (v['statut'] if nouvelle else avant), prouvees
        if not prouvees and v['statut'] == 'ok' and all(not r for (s, _), r in attendus.items() if s == sid):
            return 'ok', prouvees
        if not prouvees: return (v['statut'] if nouvelle else avant), prouvees
        complet = all(r <= prouvees.get(vid, set()) for (s, vid), r in attendus.items() if s == sid)
        if v['statut'] == 'ok' and complet and (nouvelle or avant != 'limite' or True): return 'ok', prouvees
        return ('limite' if avant != 'ok' or nouvelle else 'ok'), prouvees
    for s in ajouts:
        sid = s['source_id']; assert sid not in par_id, sid
        v = verif[sid]
        statut, prouvees = statut_de(sid, v, None, True)
        CONNUS = {'source_id', 'operation_registre', 'niveau', 'type_source', 'titre', 'institution', 'url', 'date_consultation',
                  'cibles', 'usages_atlas', 'locator', 'verification_claude', 'resume_passage', 'notes'}
        fiche = {'source_id': sid, 'niveau': s.get('niveau'), 'type_source': s.get('type_source'), 'titre': s['titre'],
                 'institution': s.get('institution'), 'url': s['url'], 'date_consultation': s.get('date_consultation'),
                 'periode_couverte': s.get('periode_couverte', []), 'zones': s.get('zones', []), 'usages_atlas': s.get('usages_atlas', []),
                 'cibles': s['cibles'], 'locator': s.get('locator'),
                 'resume_passage': v['citation'][:1500] if v['statut'] in ('ok', 'limite') else '', 'archive_locale': None,
                 'verification_claude': statut,
                 'notes': f"Proposée par Ether ({etiquette}, 05/10/2026). {s.get('notes') or s.get('note') or ''} Relecture Claude 05/10/2026 : {v['commentaire'][:1500]}"}
        if s.get('verification_claude'): fiche['verification_claude_ether'] = s['verification_claude']
        for k, val in s.items():
            if k not in CONNUS and k not in fiche: fiche[k] = val
        if statut == 'limite' and prouvees: confirmer(fiche, prouvees, v)
        reg['sources'].append(fiche); par_id[sid] = fiche; bilan[sid] = f"nouvelle : {statut}"
    for s in completes:
        sid = s['source_id']; x = par_id[sid]; avant = x['verification_claude']
        x['cibles'] = list(dict.fromkeys([*x.get('cibles', []), *s.get('cibles', [])]))
        if s.get('usages_atlas'): x['usages_atlas'] = list(dict.fromkeys([*x.get('usages_atlas', []), *s['usages_atlas']]))
        c = s.get(champ_complement)
        if c: x[champ_complement] = c
        x['notes'] = (x.get('notes') or '') + f" Complément d'Ether ({etiquette}, 05/10/2026)" + (f" : localisateur proposé « {c.get('locator')} »" if c and c.get('locator') else '') + '.'
        v = verif.get(sid)
        if not v: bilan[sid] = f'{avant} (complément sans relecture)'; continue
        statut, prouvees = statut_de(sid, v, avant, False)
        if statut == 'limite' and prouvees: confirmer(x, prouvees, v)
        if statut == 'ok' and avant != 'ok' and v.get('citation'): x['resume_passage'] = v['citation'][:1500]
        x['verification_claude'] = statut
        x['notes'] += f" Relecture Claude 05/10/2026 : {v['commentaire'][:1200]} (statut : {avant} -> {statut})."
        bilan[sid] = f'{avant} -> {statut}'
    reg['metadata']['version'] = version_apres
    return bilan
