"""Ratissage villes 1.3 (Tchéquie, Slovaquie, Hongrie) -> data/snapshot0/villes_1-3_tchequie_slovaquie_hongrie.json

Villes, rangs, rôles, sources et corrections : document d'Ether du 01/10/2026
(data/snapshot0/villes_1-3_tchequie_slovaquie_hongrie_brief_ether.md), extrait par Claude dans
data/sources/deltas_ether/2026-10-01_villes_1-3_extrait_du_brief.json (le JSON d'Ether n'avait pas été transmis).
Positions : Wikidata (CC0), outils/villes/wikidata_ratissage_1_3.json.
Relancer : python outils/villes/construire_villes_1_3.py (depuis la racine du dépôt).
"""
import json, pathlib

RACINE = pathlib.Path(__file__).resolve().parents[2]
ICI = pathlib.Path(__file__).parent
EXTRAIT = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-01_villes_1-3_extrait_du_brief.json', encoding='utf-8'))
QID = json.load(open(ICI / 'wikidata_ratissage_1_3.json', encoding='utf-8'))
REGISTRE = {x['source_id']: x for x in json.load(open(RACINE / 'data/sources/atlas_registre_sources.json', encoding='utf-8'))['sources']}
S = {s['S']: s['source_id'] for s in EXTRAIT['sources']}

ROLES = {'port fluvial': 'port_fluvial'}
# Prague : siège du Protectorat -> régionale, par cohérence avec Vienne (point laissé ouvert par Ether, à confirmer par Guizmo)
CAPITALES = {'ville-cz-prague': 'regionale', 'ville-sk-bratislava': 'nationale', 'ville-hu-budapest': 'nationale'}
NOM_LOCAL = {'ville-cz-prague': 'Praha', 'ville-cz-plzen': 'Plzeň'}
NOMS = {'ville-cz-bohumin': 'Nový Bohumín', 'ville-sk-komarno-komarom': 'Komárom', 'ville-sk-sturovo': 'Párkány', 'ville-hu-csepel': 'Csepel'}
# Autres noms (allemand, hongrois, slovaque, nom plus récent) : pour la recherche seulement, jamais un nom actif en 1945
ALIASES = {
    'ville-cz-prague': ['Praha', 'Prag'], 'ville-cz-brno': ['Brünn'], 'ville-cz-plzen': ['Plzeň'], 'ville-cz-ostrava': ['Ostrava', 'Mährisch Ostrau'],
    'ville-cz-usti-nad-labem': ['Aussig'], 'ville-cz-pardubice': ['Pardubitz'], 'ville-cz-olomouc': ['Olmütz'], 'ville-cz-prerov': ['Prerau'],
    'ville-cz-breclav': ['Lundenburg'], 'ville-cz-decin': ['Děčín', 'Podmokly', 'Bodenbach-Tetschen', 'Tetschen'], 'ville-cz-cheb': ['Eger'],
    'ville-cz-liberec': ['Reichenberg'], 'ville-cz-zlin': ['Gottwaldov'], 'ville-cz-mlada-boleslav': ['Jungbunzlau'],
    'ville-cz-ceske-budejovice': ['Budweis'], 'ville-cz-ceska-trebova': ['Böhmisch Trübau'], 'ville-cz-most': ['Brüx'],
    'ville-cz-bohumin': ['Bohumín', 'Neu Oderberg'],
    'ville-sk-bratislava': ['Pressburg', 'Pozsony'], 'ville-sk-kosice': ['Kassa', 'Kaschau'], 'ville-sk-zilina': ['Zsolna', 'Sillein'],
    'ville-sk-zvolen': ['Zólyom', 'Altsohl'], 'ville-sk-banska-bystrica': ['Besztercebánya', 'Neusohl'], 'ville-sk-presov': ['Eperjes'],
    'ville-sk-trnava': ['Nagyszombat', 'Tyrnau'], 'ville-sk-nove-zamky': ['Érsekújvár'], 'ville-sk-komarno-komarom': ['Komárno'],
    'ville-sk-sturovo': ['Parkan', 'Štúrovo'], 'ville-sk-trencin': ['Trencsén', 'Trentschin'],
    'ville-hu-gyor': ['Raab'], 'ville-hu-pecs': ['Fünfkirchen'], 'ville-hu-szekesfehervar': ['Stuhlweißenburg'], 'ville-hu-sopron': ['Ödenburg'],
    'ville-hu-ujdombovar': ['Dombóvár'], 'ville-hu-vac': ['Waitzen'], 'ville-hu-szombathely': ['Steinamanger'],
}
# Corrections et repères d'Ether (section 2 du document), en clair dans la note
NOTES = {
    'ville-cz-ostrava': "Nom au Snapshot 0 : Moravská Ostrava ; Ostrava à partir du 28/06/1946 (futur état). Raid du 29/08/1944 sur usines, mine et transports.",
    'ville-cz-decin': "Ville réunie le 01/10/1942 (Děčín, Podmokly, Staré Město) ; forme administrative allemande de 1944 à confirmer (Bodenbach-Tetschen selon un article des ČD). Le port de Loubí est d'après-guerre.",
    'ville-cz-zlin': "Dégâts de novembre 1944 ; Gottwaldov à partir du 01/01/1949 (futur état).",
    'ville-cz-most': "Point à placer sur le vieux Most de 1945 : la position actuelle (Wikidata) est celle de la ville reconstruite, à corriger.",
    'ville-cz-bohumin': "Point = gare de Nový Bohumín ; nom administratif et périmètre de guerre à vérifier (regroupement de 1943 ?, fusion de 1949).",
    'ville-cz-prague': "Siège du Protectorat de Bohême-Moravie ; gouvernement tchécoslovaque en exil en Angleterre. Capitale « régionale » au Snapshot 0, par cohérence avec Vienne (à confirmer).",
    'ville-sk-bratislava': "Capitale de l'État slovaque depuis le 14/03/1939 ; extension « Grande Bratislava » de 1946 non anticipée.",
    'ville-sk-komarno-komarom': "Les deux rives forment une seule ville en 1939–1945 : une seule entité (date de séparation à préciser).",
    'ville-sk-sturovo': "Nom en 1945 : Párkány / Parkan ; Štúrovo à partir du 26/06/1948.",
    'ville-sk-poprad': "Veľká et Spišská Sobota ne sont rattachées qu'au 01/01/1946 ; Svit n'en fait pas partie.",
    'ville-sk-nove-zamky': "Attaque du 14/10/1944 incluse ; celle du 14/03/1945 est postérieure.",
    'ville-hu-miskolc': "Fusion avec Diósgyőr datée du 01/01/1945 : au Snapshot 0 (dernier état avant 0 h), deux points distincts ; fusion à appliquer au ratissage du temps.",
    'ville-hu-diosgyor': "Distincte de Miskolc au Snapshot 0 ; fusion datée du 01/01/1945, à appliquer au ratissage du temps.",
    'ville-hu-ujdombovar': "Gare et cité ferroviaire d'Újdombóvár, distinctes de Dombóvár jusqu'à la fusion de 1946.",
    'ville-hu-csepel': "Commune distincte de Budapest jusqu'en 1950 ; le port franc de Budapest (1928, sur l'île) relève du système budapestois, pas automatiquement de Csepel. Point retenu provisoirement (source C).",
    'ville-hu-debrecen': "Assemblée nationale provisoire réunie le 21/12/1944, gouvernement provisoire le 22/12 : siège administratif provisoire. Gare bombardée en 1944.",
    'ville-hu-budapest': "Encerclée depuis le 26/12/1944 ; reste capitale nationale (le siège provisoire de Debrecen ne la remplace pas automatiquement).",
    'ville-hu-szeged': "Pont détruit en 1944 ; franchissement ferroviaire provisoire rétabli le 12/11/1944 (capacité inconnue).",
}
A_RENFORCER = {'ville-hu-csepel': ['industrie']}  # seule source C (Ether)

entites = []
for v in EXTRAIT['villes']:
    eid = v['id']
    q = QID[eid]
    nom = NOMS.get(eid, v['nom'])
    roles = list(dict.fromkeys(ROLES.get(r, r) for r in v['roles']))
    sids = [S[n] for n in v['S']]
    prop = {}
    if eid in NOM_LOCAL: prop['nom_local'] = NOM_LOCAL[eid]
    prop['importance_atlas'] = v['rang']
    if eid in CAPITALES: prop['capitale'] = CAPITALES[eid]
    prop['roles'] = roles
    a_renforcer = list(A_RENFORCER.get(eid, []))
    if not any(REGISTRE[s]['verification_claude'] == 'ok' for s in sids):
        a_renforcer += [r for r in roles if r not in a_renforcer]  # aucune source confirmée par Claude
    note = f"Rôle dans l'Atlas (Ether, ratissage villes 1.3) : {v['pourquoi']}"
    if eid in NOTES: note += ' ' + NOTES[eid]
    if a_renforcer: note += f" À renforcer : {', '.join(a_renforcer)}."
    prop['note'] = note
    aliases = [a for a in dict.fromkeys([*ALIASES.get(eid, []), q.get('label_en')]) if a and a != nom]
    statut = lambda s: REGISTRE[s]['verification_claude']
    sources = [{'source_id': 'src-wikidata', 'locator': q['qid'], 'usage': 'position (coordonnées)'}]
    sources += [{'source_id': s, 'locator': REGISTRE[s].get('locator', ''),
                 'usage': 'preuve locale : ' + ', '.join(roles) + ('' if statut(s) == 'ok' else ' (non vérifiée par Claude)' if statut(s) in ('non_verifiee', 'lien_casse') else ' (lecture partielle)')}
                for s in sids]
    entites.append({
        'entite_id': eid, 'type_entite': 'ville', 'nom': nom, 'nom_court': nom, **({'aliases': aliases} if aliases else {}),
        'etats': [{
            'etat_id': 'etat-01',
            'valid_from': {'date': '', 'precision': 'inconnue'},
            'valid_to': {'date': '', 'precision': 'inconnue'},
            'statut': 'ville_au_snapshot0',
            'proprietes': prop,
            'geometrie': {'type': 'Point', 'coordinates': [q['lon'], q['lat']]},
            'sources': sources,
        }],
        'relations': [],
    })

lot = {
  'metadata_lot': {
    'nom': 'snapshot0_villes_1-3_tchequie_slovaquie_hongrie', 'date_reference': '1945-01-01', 'heure_reference': '00:00',
    'version': '0.1', 'statut': 'integre_par_claude', 'gabarit_source': 'gabarits/gabarit_entite_temporelle_atlas.json',
    'zone': ['Tchéquie actuelle', 'Slovaquie actuelle', 'Hongrie actuelle'],
    'differes_par_ether': ['Dunapentele (argument industriel de 1950 exclu)', 'Esztergom (pont à traiter à part)', 'Tatabánya', 'Kazincbarcika', 'Otrokovice / Baťov', 'Karlovy Vary'],
    'integration': {'date': '2026-10-01', 'par': 'Claude', 'corrections': [
      "Données tirées du document d'Ether (le JSON n'avait pas été transmis) : rangs, rôles, sources et corrections de la section 2.",
      "Noms au Snapshot 0 : Moravská Ostrava, Děčín–Podmokly, Nový Bohumín, Komárom (les deux rives), Párkány ; noms allemands, hongrois et plus récents en alias (recherche seulement).",
      "Capitales : Bratislava et Budapest nationales ; Prague régionale par cohérence avec Vienne (à confirmer).",
      "Miskolc et Diósgyőr : deux points (fusion du 01/01/1945 à appliquer au ratissage du temps).",
      "Positions : Wikidata ; Nový Bohumín = gare ; Most à déplacer sur le vieux Most ; Komárom = rive nord (Komárno).",
      "« À renforcer » : Csepel (source C) et les villes dont aucune source n'a été confirmée par la relecture de Claude.",
    ]},
  },
  'entites': entites,
}
out = RACINE / 'data/snapshot0/villes_1-3_tchequie_slovaquie_hongrie.json'
out.write_text(json.dumps(lot, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(len(entites), 'villes ->', out.relative_to(RACINE))
