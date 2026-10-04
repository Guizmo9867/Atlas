"""Fusion au registre des sources du lot villes 1.8 (Balkans, Grèce et Italie, Ether, remise du 04/10/2026). À lancer UNE fois,
après fusion_sources_1_6_1_7_cycle3.py (v1.24 -> v1.25).
Delta : data/sources/deltas_ether/2026-10-04_villes_1-8_delta.json (67 fiches : 66 ajouts, 1 complément src-wikidata).
Statut : relecture de Claude (data/sources/verifications_claude/2026-10-04_villes_1-8.json ; WebFetch seul ; les 5 cartes OSS
lues par Claude sur les images déposées par Ether : villes relues -> confirmations_claude).
Une source « ok » qui ne nomme pas toutes ses villes est ramenée à « limite » : seules les villes nommées comptent (confirmations_claude).
"""
import json, pathlib
RACINE = pathlib.Path(__file__).resolve().parents[2]
R = RACINE / 'data/sources/atlas_registre_sources.json'
reg = json.load(open(R, encoding='utf-8'))
assert reg['metadata']['version'] == '1.24', 'ordre des fusions ?'
VERIF = 'data/sources/verifications_claude/2026-10-04_villes_1-8.json'
delta = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-04_villes_1-8_delta.json', encoding='utf-8'))['sources']
V = json.load(open(RACINE / VERIF, encoding='utf-8'))
verif = {r['id']: r for r in V['resultats']}
lot = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-04_villes_1-8_proposition_ether.json', encoding='utf-8'))['proposition_ether']
proposees = {e['entite_id'] for e in lot['entites']}
par_id = {s['source_id']: s for s in reg['sources']}
urls = {s['url'] for s in reg['sources']}
relues = {}
for r in V['relations']:
    if r['roles_confirmes'] and r['entite_id'] in proposees:
        relues.setdefault(r['source_id'], {})[r['entite_id']] = r
CONNUS = {'source_id', 'operation_registre', 'niveau', 'type_source', 'titre', 'institution', 'url', 'date_consultation',
          'cibles', 'usage', 'usages_atlas', 'locator', 'note', 'verification_ether', 'verification_claude', 'resume_passage', 'resume_francais'}
ajouts, conf_n = 0, 0
for s in delta:
    sid = s['source_id']
    if s['operation_registre'] == 'completer':
        assert sid == 'src-wikidata'
        x = par_id[sid]
        x['cibles'] = list(dict.fromkeys([*x.get('cibles', []), *s['cibles']]))
        x['usages_atlas'] = list(dict.fromkeys([*x.get('usages_atlas', []), *s.get('usages_atlas', [])]))
        x['notes'] += (" Villes 1.8 (04/10/2026) : 361 positions proposées par Ether (QID et P625) et recoupées par Claude par SPARQL"
                       " (aucun écart > 1 km, aucun doublon avec les villes déjà intégrées ; outils/villes/wikidata_ratissage_1_8.json).")
        continue
    assert sid not in par_id, sid
    v = verif[sid]
    usage = ' ; '.join(s['usage']) if isinstance(s['usage'], list) else s['usage']
    fiche = {
        'source_id': sid, 'niveau': s['niveau'], 'type_source': s['type_source'], 'titre': s['titre'],
        'institution': s['institution'], 'url': s['url'], 'date_consultation': s['date_consultation'], 'periode_couverte': [], 'zones': [],
        'usages_atlas': s.get('usages_atlas', []), 'cibles': s['cibles'], 'locator': s['locator'],
        'resume_passage': v['citation'] if v['statut'] in ('ok', 'limite') else '', 'archive_locale': None,
        'verification_claude': v['statut'], 'verification_ether': s.get('verification_ether'),
        'notes': (f"Proposée par Ether (villes 1.8, 04/10/2026). Ce que la source prouve selon Ether : {usage}. "
                  f"Limite annoncée par Ether : {s.get('note', '')} Relecture Claude 04/10/2026 : {v['commentaire']}"
                  + ('' if set(s['cibles']) & proposees else " Cibles : candidats différés par Ether (contexte de recherche, aucune ville créée).")
                  + (" URL déjà présente au registre sous un autre identifiant." if s['url'] in urls else '')),
    }
    if s.get('resume_francais'): fiche['resume_francais_ether'] = s['resume_francais']
    for k, val in s.items():
        if k not in CONNUS: fiche[k] = val
    rel = relues.get(sid, {})
    if rel:
        conf = fiche.setdefault('confirmations_claude', {})
        for vid, r in rel.items():
            conf[vid] = {'roles': r['roles_confirmes'], 'lecture': f"{r['image']}, lue par Claude : {r['citation'][:300]}", 'date': '2026-10-04', 'verification': VERIF}
            conf_n += 1
    reg['sources'].append(fiche); ajouts += 1
reg['metadata']['version'] = '1.25'
R.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(ajouts, 'ajouts ;', conf_n, 'confirmations ville par ville ;', len(reg['sources']), 'sources (v1.25)')
