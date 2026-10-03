"""Fusion au registre des sources du lot villes 1.6 (Ether, 03/10/2026). À lancer UNE fois, après fusion_sources_1_5_reponses.py (v1.18 -> v1.19).
Delta : data/sources/deltas_ether/2026-10-03_villes_1-6_delta.json (114 fiches : 113 ajouts, 1 complément de src-wikidata).
Statut : relecture de Claude (data/sources/verifications_claude/2026-10-03_villes_1-6.json).
src-wikidata : union des cibles, usages et consultations ; verification_claude et champs existants conservés.
Les sources qui ne visent que des candidats différés entrent comme contexte : elles ne créent aucune ville.
"""
import json, pathlib
RACINE = pathlib.Path(__file__).resolve().parents[2]
R = RACINE / 'data/sources/atlas_registre_sources.json'
reg = json.load(open(R, encoding='utf-8'))
assert reg['metadata']['version'] == '1.18', 'ordre des fusions ?'
delta = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-03_villes_1-6_delta.json', encoding='utf-8'))['sources']
verif = {r['id']: r for r in json.load(open(RACINE / 'data/sources/verifications_claude/2026-10-03_villes_1-6.json', encoding='utf-8'))['resultats']}
lot = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-03_villes_1-6_proposition_ether.json', encoding='utf-8'))['proposition_ether']
proposees = {e['entite_id'] for e in lot['entites']}
par_id = {s['source_id']: s for s in reg['sources']}
urls = {s['url'] for s in reg['sources']}
CONNUS = {'source_id', 'operation_registre', 'niveau', 'type_source', 'titre', 'institution', 'url', 'date_consultation',
          'cibles', 'usage', 'usages_atlas', 'locator', 'note', 'verification_ether'}
ajouts = 0
for s in delta:
    sid = s['source_id']
    if s['operation_registre'] == 'completer':
        x = par_id[sid]
        x['cibles'] = list(dict.fromkeys([*x.get('cibles', []), *s['cibles']]))
        x['usages_atlas'] = list(dict.fromkeys([*x.get('usages_atlas', []), *s['usages_atlas']]))
        x['consultations_ether'] = [*x.get('consultations_ether', []), *s.get('consultations_ether', [])]
        x['notes'] += (" Complément d'Ether (villes 1.6, 03/10/2026) : " + s['note'] + " Lectures P625 du 03/10/2026 pour 254 villes, "
                       "recoupées par Claude le même jour par requête SPARQL (QID et coordonnées identiques, pays actuel concordant).")
        continue
    assert sid not in par_id, sid
    v = verif[sid]
    usage = '; '.join(s['usage']) if isinstance(s['usage'], list) else s['usage']
    fiche = {
        'source_id': sid, 'niveau': s['niveau'], 'type_source': s['type_source'], 'titre': s['titre'],
        'institution': s['institution'], 'url': s['url'], 'date_consultation': s['date_consultation'], 'periode_couverte': [], 'zones': [],
        'usages_atlas': s['usages_atlas'], 'cibles': s['cibles'], 'locator': s['locator'],
        'resume_passage': v['citation'] if v['statut'] in ('ok', 'limite') else '', 'archive_locale': None,
        'verification_claude': v['statut'], 'verification_ether': s.get('verification_ether'),
        'notes': (f"Proposée par Ether (villes 1.6, 03/10/2026). Ce que la source prouve selon Ether : {usage}. "
                  f"Limite annoncée par Ether : {s.get('note', '')} Relecture Claude 03/10/2026 : {v['commentaire']}"
                  + ('' if set(s['cibles']) & proposees else " Cibles : candidats différés par Ether (contexte de recherche, aucune ville créée).")
                  + (" URL déjà présente au registre sous un autre identifiant." if s['url'] in urls else '')),
    }
    for k, val in s.items():
        if k not in CONNUS: fiche[k] = val
    reg['sources'].append(fiche); ajouts += 1
reg['metadata']['version'] = '1.19'
R.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(ajouts, 'ajouts ;', len(reg['sources']), 'sources (v1.19)')
