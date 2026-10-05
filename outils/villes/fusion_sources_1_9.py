"""Fusion au registre des sources du lot villes 1.9 (Ibérie et marges, Ether, remise du 05/10/2026). À lancer UNE fois,
après fusion_sources_1_7_1_8_reponses.py (v1.26 -> v1.27).
Delta : data/sources/deltas_ether/2026-10-05_villes_1-9_delta.json (36 fiches : 35 ajouts, 1 complément src-wikidata).
Relecture de Claude : data/sources/verifications_claude/2026-10-05_villes_1-9.json (WebFetch seul ; la carte Forcano 1942
lue par Claude sur les captures déposées par Ether, ville par ville).
Règles : statut « ok » seulement si la relecture prouve tous les rôles attendus par chaque ville proposée qui cite la source ;
sinon « limite » et villes/rôles relus dans confirmations_claude. Le champ verification_claude livré par Ether est ignoré
(gardé sous verification_claude_ether).
"""
import json, pathlib, re
RACINE = pathlib.Path(__file__).resolve().parents[2]
R = RACINE / 'data/sources/atlas_registre_sources.json'
reg = json.load(open(R, encoding='utf-8'))
assert reg['metadata']['version'] == '1.26', 'ordre des fusions ?'
VERIF = 'data/sources/verifications_claude/2026-10-05_villes_1-9.json'
delta = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-05_villes_1-9_delta.json', encoding='utf-8'))['sources']
V = json.load(open(RACINE / VERIF, encoding='utf-8'))
verif = {r['id']: r for r in V['resultats']}
lot = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-05_villes_1-9_proposition_ether.json', encoding='utf-8'))['proposition_ether']
proposees = {e['entite_id'] for e in lot['entites']}
ROLES = {'capitale', 'administration', 'rail', 'port_maritime', 'port_fluvial', 'industrie', 'charbon', 'aviation', 'militaire', 'mines', 'peche', 'base_navale'}
usages_ville = {}
for e in lot['entites']:
    for s in e['etats'][0]['sources']:
        usages_ville.setdefault((s['source_id'], e['entite_id']), set()).update(t.strip() for t in re.split(r'[,;]', s['usage']))
par_id = {s['source_id']: s for s in reg['sources']}
urls = {s['url'] for s in reg['sources']}
CONNUS = {'source_id', 'operation_registre', 'niveau', 'type_source', 'titre', 'institution', 'url', 'date_consultation',
          'cibles', 'usage', 'usages_atlas', 'locator', 'note', 'verification_ether', 'verification_claude', 'resume_passage', 'resume_francais'}
ajouts, conf_n, bilan = 0, 0, {}
for s in delta:
    sid = s['source_id']
    if s['operation_registre'] == 'completer':
        assert sid == 'src-wikidata'
        x = par_id[sid]
        x['cibles'] = list(dict.fromkeys([*x.get('cibles', []), *s['cibles']]))
        x['usages_atlas'] = list(dict.fromkeys([*x.get('usages_atlas', []), *s.get('usages_atlas', [])]))
        x['notes'] += (" Villes 1.9 (05/10/2026) : 238 positions proposées par Ether (QID et P625) et recoupées par Claude par SPARQL"
                       " (aucun écart > 1 km, pays cohérents, aucun doublon avec les villes déjà intégrées ; outils/villes/wikidata_ratissage_1_9.json).")
        continue
    assert sid not in par_id, sid
    v = verif[sid]
    prouvees = {k: set(r) for k, r in (v.get('villes_prouvees') or {}).items() if r}
    attendus = {vid: usages_ville[(sid, vid)] & ROLES for vid in proposees if (sid, vid) in usages_ville}
    statut = v['statut']
    if statut == 'ok' and prouvees and not all(r <= prouvees.get(vid, set()) for vid, r in attendus.items()):
        statut = 'limite'
    usage = ' ; '.join(s['usage']) if isinstance(s['usage'], list) else s['usage']
    fiche = {
        'source_id': sid, 'niveau': s['niveau'], 'type_source': s['type_source'], 'titre': s['titre'],
        'institution': s['institution'], 'url': s['url'], 'date_consultation': s['date_consultation'], 'periode_couverte': [], 'zones': [],
        'usages_atlas': s.get('usages_atlas', []), 'cibles': s['cibles'], 'locator': s['locator'],
        'resume_passage': v['citation'][:1500] if v['statut'] in ('ok', 'limite') else '', 'archive_locale': None,
        'verification_claude': statut, 'verification_ether': s.get('verification_ether'),
        'notes': (f"Proposée par Ether (villes 1.9, 05/10/2026). Ce que la source prouve selon Ether : {usage}. "
                  f"Limite annoncée par Ether : {s.get('note', '')} Relecture Claude 05/10/2026 : {v['commentaire'][:1500]}"
                  + (f" (relecture : {v['statut']} ; ramenée à « limite » : toutes les villes citées ne sont pas prouvées pour tous leurs rôles)" if statut != v['statut'] else '')
                  + ('' if set(s['cibles']) & proposees else " Cibles : candidats différés par Ether (contexte de recherche, aucune ville créée).")
                  + (" URL déjà présente au registre sous un autre identifiant." if s['url'] in urls else '')),
    }
    if s.get('resume_francais'): fiche['resume_francais_ether'] = s['resume_francais']
    if s.get('verification_claude'): fiche['verification_claude_ether'] = s['verification_claude']
    for k, val in s.items():
        if k not in CONNUS: fiche[k] = val
    if statut == 'limite' and prouvees:
        conf = fiche.setdefault('confirmations_claude', {})
        for vid, roles in prouvees.items():
            if vid not in proposees: continue
            conf[vid] = {'roles': sorted(roles), 'lecture': f"relu par Claude (villes 1.9) : {(v.get('preuves_par_ville') or {}).get(vid, '')[:300]}", 'date': '2026-10-05', 'verification': VERIF}
            conf_n += 1
    reg['sources'].append(fiche); ajouts += 1; bilan[sid] = (v['statut'], statut, len(attendus))
reg['metadata']['version'] = '1.27'
R.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for k, b in bilan.items(): print(' ', k, b)
print(ajouts, 'ajouts ;', conf_n, 'confirmations ville par ville ;', len(reg['sources']), 'sources (v1.27)')
