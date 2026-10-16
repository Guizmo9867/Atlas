"""Ratissage villes 1.10 (complément France : chefs-lieux départementaux de 1945 sans fiche ville)
-> data/snapshot0/villes_1-10_complement_france.json

Données : proposition JSON d'Ether du 16/10/2026 (data/sources/deltas_ether/2026-10-16_villes_1-10_proposition_ether.json ;
note : villes_1-10_complement_france_brief_ether.md ; réserves R110-01 à R110-04 et 6 reports : villes_1-10_complement_france_reserves_ether.md ;
grille des 72 candidats : villes_1-10_complement_france_grille_couverture_ether.md).
Positions : points TRF-GIS (Victor Gay, CC BY 4.0, mairies modernes) livrés par Ether, recoupés par Claude avec Wikidata par le code INSEE
(outils/villes/wikidata_ratissage_1_10.json : 65 points, écart maximal 1,1 km). Mézières sans point (R110-01).
Relancer : python outils/villes/construire_villes_1_10.py (depuis la racine), après fusion_sources_1_10.py.
"""
import json, pathlib, copy
RACINE = pathlib.Path(__file__).resolve().parents[2]
PROPOSITION = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-16_villes_1-10_proposition_ether.json', encoding='utf-8'))['proposition_ether']
REGISTRE = {x['source_id']: x for x in json.load(open(RACINE / 'data/sources/atlas_registre_sources.json', encoding='utf-8'))['sources']}
VERIF = json.load(open(RACINE / 'data/sources/verifications_claude/2026-10-16_villes_1-10.json', encoding='utf-8'))
PAR_VILLE = VERIF.get('par_ville', {})
# Fiche au nom actuel, état au nom de 1945 (nomenclature 1940, renommages postérieurs : 1955, 1988, 1988, 1998) ; ancien nom en alias.
RENOMMAGE = {'ville-fr-bourg': ('ville-fr-bourg-en-bresse', 'Bourg-en-Bresse'), 'ville-fr-digne': ('ville-fr-digne-les-bains', 'Digne-les-Bains'),
             'ville-fr-le-puy': ('ville-fr-le-puy-en-velay', 'Le Puy-en-Velay'), 'ville-fr-chalons-sur-marne': ('ville-fr-chalons-en-champagne', 'Châlons-en-Champagne')}
NON_PREUVE = ('src-trfgis-departements-1940',)
MENTION = {'limite': ' (lecture partielle)', 'faible': ' (non confirmée par la relecture de Claude)',
           'non_verifiee': ' (non vérifiée par Claude)', 'lien_casse': ' (non vérifiée par Claude : lien cassé)'}
entites, renommees = [], []
for v in PROPOSITION['entites']:
    e = copy.deepcopy(v); et = e['etats'][0]; p = et['proprietes']
    if e['entite_id'] in RENOMMAGE:
        ancien = e['nom']; nid, actuel = RENOMMAGE[e['entite_id']]
        renommees.append(f"{e['entite_id']} -> {nid}")
        e['entite_id'], e['nom'], e['nom_court'] = nid, actuel, actuel
        e['aliases'] = list(dict.fromkeys([*e.get('aliases', []), ancien]))
        p['nom'] = ancien
    prouve = set()
    for s in et['sources']:
        if s['source_id'] in NON_PREUVE: continue
        st = PAR_VILLE.get(s['source_id'], {}).get(e['entite_id'], REGISTRE[s['source_id']]['verification_claude'])
        if st == 'ok':
            if s['usage'].startswith('administration'): prouve.add('administration')
        else:
            s['usage'] += MENTION.get(st, ' (non vérifiée par Claude)')
    note = p['note']
    if p.get('nom'): note += f" Nom à la date : {p['nom']} (aujourd'hui {e['nom']})."
    a_renforcer = [r for r in p['roles'] if r not in prouve]
    if a_renforcer: note += f" À renforcer : {', '.join(a_renforcer)}."
    p['note'] = note
    entites.append(e)

lot = {
  'metadata_lot': {
    'nom': 'snapshot0_villes_1-10_complement_france', 'date_reference': '1945-01-01', 'heure_reference': '00:00',
    'version': '0.1', 'statut': 'integre_par_claude', 'gabarit_source': 'gabarits/gabarit_entite_temporelle_atlas.json',
    'zone': PROPOSITION['metadata_lot']['zone'], 'limites_ether': PROPOSITION['metadata_lot']['limites_ether'],
    'reserves_ether': 'R110-01 à R110-04 et R110-REPORT-11/50/64/66/68/74 (data/snapshot0/villes_1-10_complement_france_reserves_ether.md), revue finale 1.x',
    'credits': 'Points : Victor Gay (TSE/IAST), TRF-GIS, DOI 10.7910/DVN/ULQYM5, CC BY 4.0 (mairies modernes, centre de 1945 non certifié).',
    'integration': {'date': '2026-10-16', 'par': 'Claude (boucle automatique)', 'corrections': [
      "Données : JSON d'Ether, 66 villes françaises (chefs-lieux départementaux de 1945 sans fiche) ; 6 candidats reportés par Ether non importés (Carcassonne, Saint-Lô, Pau, Perpignan, Colmar, Annecy) ; aucun doublon avec les 34 villes françaises déjà intégrées. Rôle « administration » seul, importance C.",
      "IDs et noms : 4 fiches mises au nom actuel (Bourg-en-Bresse, Digne-les-Bains, Le Puy-en-Velay, Châlons-en-Champagne), nom de 1945 dans l'état (Bourg, Digne, Le Puy, Châlons-sur-Marne, nomenclature 1940) et en alias ; Mézières reste une ville distincte, sans point.",
      "Positions : 65 points TRF-GIS d'Ether (CC BY 4.0) recoupés avec Wikidata par code INSEE : écart maximal 1,1 km.",
      "Preuves : 63 sources relues par WebFetch (11 ok, 25 limite, 1 faible, 26 non vérifiées : la plupart des pages des préfectures refusent l'outil) ; réponse AN 1981 (déjà « ok ») pour Nancy, Orléans, Poitiers. « À renforcer : administration » pour chaque ville sans preuve confirmée."]},
  },
  'entites': entites,
}
out = RACINE / 'data/snapshot0/villes_1-10_complement_france.json'
out.write_text(json.dumps(lot, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(renommees)
print(len(entites), 'villes ->', out.relative_to(RACINE), '; à renforcer :', sum('À renforcer' in e['etats'][0]['proprietes']['note'] for e in entites),
      '; sans point :', [e['entite_id'] for e in entites if not e['etats'][0].get('geometrie')])
