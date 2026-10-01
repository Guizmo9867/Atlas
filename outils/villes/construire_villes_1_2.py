"""Ratissage villes 1.2 (Allemagne + arc alpin) -> data/snapshot0/villes_1-2_allemagne_alpes.json

Liste, rôles, priorités et sources : proposition d'Ether (01/10/2026,
data/sources/deltas_ether/2026-10-01_villes_1-2_allemagne_alpes_proposition_ether.json), intégrée par Claude.
Positions : Wikidata (CC0), QID retenu dans outils/villes/wikidata_ratissage_1_2.json (tiré par SPARQL,
vérifié contre Natural Earth le 01/10/2026).
Retour d'audit d'Ether (01/10/2026) appliqué : voir IMPORTANCE, GENERALES, RETIREES, AJOUTS, SITUATION.
Relancer : python outils/villes/construire_villes_1_2.py (depuis la racine du dépôt).
"""
import json, pathlib

RACINE = pathlib.Path(__file__).resolve().parents[2]
ICI = pathlib.Path(__file__).parent
PROPOSITION = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-01_villes_1-2_allemagne_alpes_proposition_ether.json', encoding='utf-8'))
QID = json.load(open(ICI / 'wikidata_ratissage_1_2.json', encoding='utf-8'))
REGISTRE = {x['source_id']: x for x in json.load(open(RACINE / 'data/sources/atlas_registre_sources.json', encoding='utf-8'))['sources']}

# --- Retour d'audit d'Ether (01/10/2026, data/snapshot0/villes_1-2_allemagne_alpes_audit_ether.md) ---
# Type de capitale et importance Atlas sont indépendants : Vaduz = capitale nationale mais C.
IMPORTANCE = {'ville-li-vaduz': 'C'}
# Sources générales : contexte seulement, jamais seule preuve d'un rôle local
GENERALES = {'src-db-museum-history', 'src-sbb-history'}
# Sources retirées d'une ville (page hors sujet)
RETIREES = {'ville-at-graz': {'src-graz-rail-industry'}}
# Sources ajoutées par Claude
AJOUTS = {
    'ville-li-vaduz': [{'source_id': 'src-vaduz-portrait', 'locator': 'Portrait > Vaduz', 'usage': 'statut : capitale, siège des autorités et du Parlement (capitale depuis 1719 selon la commune)'}],
    'ville-de-aachen': [{'source_id': 'src-mwi-aachen-1944', 'locator': 'Urban Warfare Project Case Study #10', 'usage': 'situation au 01/01/1945 : évacuation ordonnée, plus de 80 % des bâtiments détruits, ville prise le 21/10/1944'}],
}
SITUATION = {'ville-de-aachen': 'evacuee et detruite'}
NOTES_EN_PLUS = {
    'ville-de-aachen': " Situation au 01/01/1945 (source MWI) : évacuation des civils ordonnée par les autorités allemandes à l'automne 1944, il ne restait qu'environ 5 000 à 20 000 des 165 000 habitants au début des combats ; plus de 80 % des bâtiments détruits ; ville prise par les Américains le 21/10/1944. Cela ne prouve pas l'arrêt total du réseau ferroviaire.",
    'ville-at-wien': " Capitale régionale (Reichsgau Wien) au 01/01/1945. Retour au statut de capitale nationale : futur état daté, repère du 27/04/1945 à instruire avec une source dédiée (rétablissement politique, statut de capitale et contrôle effectif à distinguer).",
    'ville-de-magdeburg': " Destruction du port le 16/01/1945 : à traiter au ratissage de janvier (préciser l'objet touché : port, équipements ou ville).",
}

def usage_source(sid):
    if sid in GENERALES: return 'contexte national seulement (ne prouve pas le rôle local)'
    v = REGISTRE[sid]['verification_claude']
    if v == 'ok': return 'rôle de la ville au 01/01/1945'
    if v == 'non_verifiee': return 'rôle de la ville au 01/01/1945 (non vérifiée lors de l\'audit)'
    return 'contexte (ne prouve pas seule le rôle au 01/01/1945)'

def bien_sourcee(sources):
    return any(s['source_id'] not in GENERALES and REGISTRE[s['source_id']]['verification_claude'] == 'ok' for s in sources)

# Vocabulaire des rôles : mots-clés d'Ether -> rôles de l'Atlas (LEXIQUE_ID.md).
# None = information géographique, pas un rôle (elle reste dans la note).
ROLES = {
    'frontiere': 'frontalier',
    'danube': 'port_fluvial', 'elbe': 'port_fluvial', 'rhin': 'port_fluvial', 'confluence': 'port_fluvial',
    'port_lacustre': 'port_fluvial', 'industrie_navale': 'construction_navale',
    'automobile': 'industrie', 'mecanique': 'industrie', 'chimie': 'industrie',
    'fret': 'rail', 'noeud_interieur': 'rail', 'brenner': 'rail',
    'corridor_alpin': 'rail', 'corridor_simplon': 'rail', 'corridor_suisse': 'rail', 'corridor_italie': 'rail',
    'corridor_gothard': 'rail', 'corridor_autriche': 'rail', 'corridor_france': 'rail', 'corridor_autriche_suisse': 'rail',
    'commerce': None, 'lac': None, 'front': None,
}
# Exceptions ville par ville
ROLES_VILLE = {'ville-ch-schaffhausen': {'rhin': None}}  # chutes du Rhin : pas de navigation, la ville est un nœud ferroviaire/frontalier
CAPITALES = {'ville-de-berlin': 'nationale', 'ville-ch-bern': 'nationale', 'ville-li-vaduz': 'nationale',
             # Vienne au 01/01/1945 : l'Autriche est annexée (Reichsgau Wien) -> capitale régionale ; le détail juridique va dans la fiche
             'ville-at-wien': 'regionale'}
NOM_LOCAL = {
    'ville-de-hamburg': 'Hamburg', 'ville-de-bremen': 'Bremen', 'ville-de-hannover': 'Hannover', 'ville-de-duisburg': 'Duisburg',
    'ville-de-koeln': 'Köln', 'ville-de-frankfurt': 'Frankfurt am Main', 'ville-de-nuernberg': 'Nürnberg', 'ville-de-muenchen': 'München',
    'ville-de-dresden': 'Dresden', 'ville-de-magdeburg': 'Magdeburg', 'ville-de-saarbruecken': 'Saarbrücken', 'ville-de-kassel': 'Kassel',
    'ville-de-aachen': 'Aachen', 'ville-de-koblenz': 'Koblenz', 'ville-de-regensburg': 'Regensburg', 'ville-de-flensburg': 'Flensburg',
    'ville-at-wien': 'Wien', 'ville-at-salzburg': 'Salzburg', 'ville-ch-bern': 'Bern', 'ville-ch-zuerich': 'Zürich', 'ville-ch-basel': 'Basel',
    'ville-ch-luzern': 'Luzern', 'ville-ch-winterthur': 'Winterthur', 'ville-ch-st-gallen': 'St. Gallen', 'ville-ch-schaffhausen': 'Schaffhausen',
    'ville-ch-bellinzona': 'Bellinzona', 'ville-ch-brig': 'Brig',
}

def roles_atlas(eid, liste):
    table = {**ROLES, **ROLES_VILLE.get(eid, {})}
    out = []
    for r in liste:
        x = table.get(r, r)
        if x and x not in out: out.append(x)
    return out

entites = []
for v in PROPOSITION['villes']:
    eid, e0 = v['entite_id'], v['etat_snapshot0']
    q = QID[eid]
    prop = {}
    if eid in NOM_LOCAL: prop['nom_local'] = NOM_LOCAL[eid]
    prop['importance_atlas'] = IMPORTANCE.get(eid, e0['importance_atlas'])
    if eid in CAPITALES: prop['capitale'] = CAPITALES[eid]
    prop['roles'] = roles_atlas(eid, e0['roles'])
    if eid in SITUATION: prop['situation'] = SITUATION[eid]
    sources_role = [{'source_id': s, 'locator': '', 'usage': usage_source(s)} for s in e0['sources'] if s not in RETIREES.get(eid, set())]
    note = f"Rôle dans l'Atlas (Ether, ratissage villes 1.2) : {e0['note']}" + NOTES_EN_PLUS.get(eid, '')
    if eid != 'ville-li-vaduz' and (e0.get('source_role_a_renforcer') or not bien_sourcee(sources_role)):
        note += ' Rôle à sourcer localement (aucune source lue ne le prouve encore).'
    prop['note'] = note
    aliases = [a for a in dict.fromkeys([NOM_LOCAL.get(eid), *v.get('aliases', []), q.get('label_en')]) if a and a != v['nom']]
    sources = [{'source_id': 'src-wikidata', 'locator': q['qid'], 'usage': 'position (coordonnées)' + (' ; capitale du Liechtenstein' if eid == 'ville-li-vaduz' else '')}]
    sources += sources_role + AJOUTS.get(eid, [])
    entites.append({
        'entite_id': eid, 'type_entite': 'ville', 'nom': v['nom'], 'nom_court': v['nom'], **({'aliases': aliases} if aliases else {}),
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

m = PROPOSITION['metadata_lot']
lot = {
  'metadata_lot': {
    'nom': 'snapshot0_villes_1-2_allemagne_alpes', 'date_reference': '1945-01-01', 'heure_reference': '00:00',
    'version': '0.2', 'statut': 'integre_par_claude', 'gabarit_source': 'gabarits/gabarit_entite_temporelle_atlas.json',
    'zone': m['perimetre'], 'note_perimetre': m['note_perimetre'],
    'exclusions_volontaires': PROPOSITION['exclusions_volontaires'],
    'audit_recommande': PROPOSITION['audit_recommande'],
    'integration': {'date': '2026-10-01', 'par': 'Claude', 'corrections': [
      "Format : champs d'Ether ramenés au modèle des lots 1.0/1.1 (etat-01 ; valid_from inconnu = ville déjà en place avant l'Atlas ; importance, rôles, note, nom local dans proprietes).",
      "Rôles : mots-clés d'Ether ramenés au vocabulaire de l'Atlas (voir ROLES dans le script) : fleuves (Danube, Elbe, Rhin) -> port_fluvial ; corridors, Brenner, nœud intérieur, fret -> rail ; automobile, mécanique, chimie -> industrie. Commerce, lac et front restent dans la note.",
      "Schaffhouse : le Rhin n'y est pas navigable (chutes) -> pas de rôle port_fluvial.",
      "Vienne : capitale « régionale » au 01/01/1945 (Autriche annexée) ; point soumis à Ether.",
      "Vaduz : aucune source fournie -> Wikidata (capitale du Liechtenstein) en attendant une source officielle.",
      "Villes marquées « à renforcer » par Ether : mention « Rôle à sourcer localement » dans la note.",
      "Positions : Wikidata (CC0), QID en locator ; vérifiées contre Natural Earth.",
      "v0.2 (01/10, retour d'audit d'Ether) : Vaduz A -> C (capitale nationale gardée : type de capitale et importance sont indépendants), source officielle de la commune ajoutée ; Vienne A et capitale régionale confirmées ; Aix-la-Chapelle « évacuée et détruite » (source MWI/West Point) ; Graz : page sur les pompiers retirée des preuves ; sources générales (DB Museum, CFF) et limitées = contexte seulement ; « Rôle à sourcer localement » sur chaque ville sans source lue qui prouve son rôle. Lot ouvert : 9 candidats à l'ajout et sources de remplacement attendus d'Ether.",
    ]},
  },
  'entites': entites,
}
out = RACINE / 'data/snapshot0/villes_1-2_allemagne_alpes.json'
out.write_text(json.dumps(lot, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(len(entites), 'villes ->', out.relative_to(RACINE))
