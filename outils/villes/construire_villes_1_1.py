"""Ratissage villes 1.1 (Nordiques) -> data/snapshot0/villes_1-1_nordiques.json

Liste, rôles, priorités et sources : proposition d'Ether (30/09/2026,
data/sources/deltas_ether/2026-09-30_villes_1-1_nordiques_proposition_ether.json), intégrée par Claude.
Positions : Wikidata (CC0), QID retenu dans outils/villes/wikidata_ratissage_1_1.json (tiré par SPARQL,
vérifié contre Natural Earth le 30/09/2026).
Relancer : python outils/villes/construire_villes_1_1.py (depuis la racine du dépôt).
"""
import json, pathlib

RACINE = pathlib.Path(__file__).resolve().parents[2]
ICI = pathlib.Path(__file__).parent
PROPOSITION = json.load(open(RACINE / 'data/sources/deltas_ether/2026-09-30_villes_1-1_nordiques_proposition_ether.json', encoding='utf-8'))
QID = json.load(open(ICI / 'wikidata_ratissage_1_1.json', encoding='utf-8'))
# Retour d'audit d'Ether (30/09/2026) : priorités modifiées + 9 villes ajoutées
PATCH = json.load(open(RACINE / 'data/sources/deltas_ether/2026-09-30_villes_1-1_audit_patch.json', encoding='utf-8'))

# Vocabulaire des rôles : on ramène les mots-clés d'Ether aux rôles de l'Atlas (LEXIQUE_ID.md).
# None = information géographique ou d'état, pas un rôle (elle reste dans la note).
ROLES = {
    'frontiere': 'frontalier', 'frontiere_est': 'frontalier',
    'corridor_interieur': 'rail', 'corridor_international': 'rail', 'corridor_finlande': 'rail', 'corridor_suede': 'rail',
    'corridor_est': 'rail', 'corridor_danemark': 'ferry', 'corridor_continent': 'ferry', 'noeud_interieur': 'rail', 'liaison_suede': 'ferry',
    'port_fluvial_maritime': ['port_fluvial', 'port_maritime'], 'port_lacustre': 'port_fluvial',
    'port_militaire': 'base_navale', 'industrie_navale': 'construction_navale',
    'capitale_territoriale': 'capitale', 'administration_guerre': 'administration',
    'hurtigruten': 'navigation_cotiere', 'navigation': 'navigation_cotiere', 'navigation_cotiere': 'navigation_cotiere',
    'fret': 'rail', 'mine': 'minerai', 'minerai': 'minerai', 'peche': 'peche', 'bois_papier': 'industrie',
    'militaire': 'militaire', 'logistique_militaire': 'militaire',
    'commerce': None, 'commerce_international': None, 'arctique': None, 'nord': None, 'atlantique_nord': None,
    'archipel': None, 'strategique': None, 'port_hiver': None,
    'liberation': None, 'evacuation': None, 'destruction_guerre': None, 'lapland_war': None,
}
# Situation au 01/01/1945 qui coupe ou perturbe les flux (déduite des rôles d'Ether)
SITUATION = {'destruction_guerre': 'detruite', 'evacuation': 'evacuee'}
CAPITALES = {'ville-dk-copenhague': 'nationale', 'ville-no-oslo': 'nationale', 'ville-se-stockholm': 'nationale',
             'ville-fi-helsinki': 'nationale', 'ville-is-reykjavik': 'nationale',
             'ville-fo-torshavn': 'territoire', 'ville-fi-mariehamn': 'territoire'}
# Sources dont l'URL existait déjà au registre : on garde l'ID canonique
CANON = {'src-govfo-political-status': 'src-govfo-faroe-status-wwii', 'src-snl-east-finnmark': 'src-snl-east-finnmark-1944',
         'src-snl-nordlandsbanen-historical': 'src-snl-nordlandsbanen'}

# Le patch d'audit : ajouts mis au même format que la proposition, décisions appliquées
VILLES = list(PROPOSITION['villes'])
for a in PATCH['ajouts']:
    VILLES.append({**{k: a[k] for k in ('entite_id', 'type_entite', 'nom', 'nom_local', 'aliases')},
                   'etats': [{'importance_atlas': a['importance_atlas'], 'roles': a['roles'], 'note': a['note'] + " (ajout après l'audit, 30/09)",
                              'sources': [{'source_id': x, 'locator': ''} for x in a['sources']]}]})
DECISIONS = {d['entite_id']: d for d in PATCH['decisions']}

def roles_atlas(liste):
    out = []
    for r in liste:
        m = ROLES.get(r, r)
        for x in (m if isinstance(m, list) else [m]):
            if x and x not in out: out.append(x)
    return out

entites = []
for v in VILLES:
    e0 = v['etats'][0]
    q = QID[v['entite_id']]
    prop = {}
    if v.get('nom_local') and v['nom_local'] != v['nom']: prop['nom_local'] = v['nom_local']
    dec = DECISIONS.get(v['entite_id'])
    prop['importance_atlas'] = dec['importance_atlas'] if dec else e0['importance_atlas']
    if v['entite_id'] in CAPITALES: prop['capitale'] = CAPITALES[v['entite_id']]
    prop['roles'] = roles_atlas(e0['roles'])
    sit = [SITUATION[r] for r in e0['roles'] if r in SITUATION]
    if v['entite_id'] == 'ville-no-kirkenes': sit = ['detruite']  # « fortement détruite » (note d'Ether)
    if sit: prop['situation'] = ' et '.join(sit)
    prop['note'] = f"Rôle dans l'Atlas (Ether, ratissage villes 1.1) : {e0['note']}" + (f" Audit : {dec['raison']}" if dec and dec['action'] == 'modifier' else '')
    aliases = [a for a in dict.fromkeys([v.get('nom_local'), *v.get('aliases', []), q.get('label_en')]) if a and a != v['nom']]
    sources = [{'source_id': 'src-wikidata', 'locator': q['qid'], 'usage': 'position (coordonnées)'}]
    sources += [{'source_id': CANON.get(s['source_id'], s['source_id']), 'locator': s.get('locator', ''), 'usage': 'rôle de la ville au 01/01/1945'} for s in e0['sources']]
    if v['entite_id'] == 'ville-dk-fredericia':
        sources.append({'source_id': 'src-jernbanemuseet-lillebaelt-1935', 'locator': 'Historien om Det røde Lyntog', 'usage': 'pont du Petit Belt (1935) : priorité B'})
    entites.append({
        'entite_id': v['entite_id'], 'type_entite': 'ville', 'nom': v['nom'], 'nom_court': v['nom'], **({'aliases': aliases} if aliases else {}),
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
    'nom': 'snapshot0_villes_1-1_nordiques', 'date_reference': '1945-01-01', 'heure_reference': '00:00',
    'version': '0.2', 'statut': 'integre_par_claude', 'gabarit_source': 'gabarits/gabarit_entite_temporelle_atlas.json',
    'zone': PROPOSITION['metadata_lot']['zone'],
    'regles': PROPOSITION['metadata_lot']['regles'],
    'integration': {'date': '2026-09-30', 'par': 'Claude', 'corrections': [
      "Format : champs d'Ether ramenés au modèle du lot 1.0 (importance, rôles, note et nom local dans proprietes ; etat-01 ; valid_from inconnu = ville déjà en place avant l'Atlas).",
      "Rôles : mots-clés d'Ether ramenés au vocabulaire de l'Atlas (voir ROLES dans le script) ; nouveaux rôles : minerai, peche, navigation_cotiere, militaire. Les informations géographiques (arctique, nord…) restent dans la note.",
      "Villes détruites ou évacuées au 01/01/1945 (Hammerfest, Kirkenes, Rovaniemi) : propriété « situation ».",
      "Positions : Wikidata (CC0), QID en locator ; vérifiées contre Natural Earth.",
      "Sources : delta d'Ether vérifié lien par lien ; 2 URL déjà au registre → IDs canoniques (src-govfo-faroe-status-wwii, src-snl-east-finnmark-1944).",
      "v0.2 (30/09, audit d'Ether) : Fredericia C → B (pont du Petit Belt, 1935) ; 9 villes ajoutées : Boden B, Hallsberg B, Oxelösund C, Gällivare C, Harstad C, Mo i Rana C, Lahti C, Kuopio C, Joensuu C. Différés : Gedser, Malmberget (future entité mine), Örebro.",
    ]},
  },
  'entites': entites,
}
out = RACINE / 'data/snapshot0/villes_1-1_nordiques.json'
out.write_text(json.dumps(lot, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(len(entites), 'villes ->', out.relative_to(RACINE))
