"""Fusion au registre des sources du lot villes 1.7 (Caucase et Turquie, Ether, remise du 03/10/2026). À lancer UNE fois,
après fusion_sources_1_6_reponses.py (v1.21 -> v1.22).
Delta : data/sources/deltas_ether/2026-10-03_villes_1-7_delta.json (54 fiches : 49 ajouts, 5 compléments).
Statut : relecture de Claude (data/sources/verifications_claude/2026-10-04_villes_1-7.json ; WebFetch seul ; répertoires
administratifs relus sur les 18 images de pages déposées par Ether).
Compléments : union des cibles et usages ; la note d'Ether est gardée dans complement_ether_1_7 ; verification_claude inchangé
(les passages Caucase de ces sources ne sont pas relus : texte tronqué, 404) sauf villes relues sur image -> confirmations_claude.
src-wikidata : cibles complétées des 166 villes (positions recoupées par Claude, outils/villes/wikidata_ratissage_1_7.json).
"""
import json, pathlib
RACINE = pathlib.Path(__file__).resolve().parents[2]
R = RACINE / 'data/sources/atlas_registre_sources.json'
reg = json.load(open(R, encoding='utf-8'))
assert reg['metadata']['version'] == '1.21', 'ordre des fusions ?'
VERIF = 'data/sources/verifications_claude/2026-10-04_villes_1-7.json'
delta = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-03_villes_1-7_delta.json', encoding='utf-8'))['sources']
V = json.load(open(RACINE / VERIF, encoding='utf-8'))
verif = {r['id']: r for r in V['resultats']}
lot = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-03_villes_1-7_proposition_ether.json', encoding='utf-8'))['proposition_ether']
proposees = {e['entite_id'] for e in lot['entites']}
par_id = {s['source_id']: s for s in reg['sources']}
urls = {s['url'] for s in reg['sources']}
ROLES = {'capitale', 'administration', 'rail', 'port_maritime', 'port_fluvial', 'industrie', 'charbon', 'minerai', 'militaire', 'ferry', 'base_navale'}
relues = {}
for r in V['relations']:
    roles = [x for x in r.get('roles_confirmes', []) if x in ROLES]
    if roles and r['entite_id'] in proposees:
        relues.setdefault(r['source_id'], {})[r['entite_id']] = (roles, r.get('image', ''), r.get('citation', ''))
CONNUS = {'source_id', 'operation_registre', 'niveau', 'type_source', 'titre', 'institution', 'url', 'date_consultation',
          'cibles', 'usage', 'usages_atlas', 'locator', 'note', 'verification_ether'}
ajouts, conf_n = 0, 0
for s in delta:
    sid = s['source_id']
    if s['operation_registre'] == 'completer':
        x = par_id[sid]
        x['cibles'] = list(dict.fromkeys([*x.get('cibles', []), *s['cibles']]))
        x['usages_atlas'] = list(dict.fromkeys([*x.get('usages_atlas', []), *s.get('usages_atlas', [])]))
        x['complement_ether_1_7'] = s['complement_ether_1_7']
        rel = relues.get(sid, {})
        if rel:
            conf = x.setdefault('confirmations_claude', {})
            for vid, (roles, img, cit) in rel.items():
                conf[vid] = {'roles': roles, 'lecture': f"image de page {img} déposée par Ether (lot 1.7), lue par Claude : {cit[:300]}", 'date': '2026-10-04', 'verification': VERIF}
                conf_n += 1
            if x['verification_claude'] in ('non_verifiee', 'faible', 'lien_casse'): x['verification_claude'] = 'limite'
        v = verif.get(sid)
        x['notes'] += (" Complément d'Ether (villes 1.7, 03/10/2026, Caucase/Turquie) : nouvelles cibles et usages (complement_ether_1_7)."
                       + (f" Relecture Claude 04/10/2026 (passages 1.7) : {v['commentaire']}" if v else '')
                       + (f" {len(rel)} villes du Caucase relues par Claude sur les images de pages (confirmations_claude)." if rel else ''))
        continue
    assert sid not in par_id, sid
    v = verif[sid]
    usage = '; '.join(s['usage']) if isinstance(s['usage'], list) else s['usage']
    fiche = {
        'source_id': sid, 'niveau': s['niveau'], 'type_source': s['type_source'], 'titre': s['titre'],
        'institution': s['institution'], 'url': s['url'], 'date_consultation': s['date_consultation'], 'periode_couverte': [], 'zones': [],
        'usages_atlas': s.get('usages_atlas', []), 'cibles': s['cibles'], 'locator': s['locator'],
        'resume_passage': v['citation'] if v['statut'] in ('ok', 'limite') else '', 'archive_locale': None,
        'verification_claude': v['statut'], 'verification_ether': s.get('verification_ether'),
        'notes': (f"Proposée par Ether (villes 1.7, 03/10/2026). Ce que la source prouve selon Ether : {usage}. "
                  f"Limite annoncée par Ether : {s.get('note', '')} Relecture Claude 04/10/2026 : {v['commentaire']}"
                  + ('' if set(s['cibles']) & proposees else " Cibles : candidats différés par Ether (contexte de recherche, aucune ville créée).")
                  + (" URL déjà présente au registre sous un autre identifiant." if s['url'] in urls else '')),
    }
    for k, val in s.items():
        if k not in CONNUS: fiche[k] = val
    reg['sources'].append(fiche); ajouts += 1
w = par_id['src-wikidata']
w['cibles'] = list(dict.fromkeys([*w.get('cibles', []), *sorted(proposees)]))
w['notes'] += (" Villes 1.7 (04/10/2026) : 166 positions prises dans Wikidata par Claude (élément relié à l'identifiant GeoNames proposé par Ether,"
               " QID principal choisi à la main pour 22 villes ; outils/villes/wikidata_ratissage_1_7.json).")
reg['metadata']['version'] = '1.22'
R.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(ajouts, 'ajouts ;', conf_n, 'confirmations ville par ville ;', len(reg['sources']), 'sources (v1.22)')
