"""Ratissage villes 1.0 (France, Benelux, îles Britanniques) — v0.2 avec les ajouts de l'audit d'Ether -> data/snapshot0/villes_1-0_france_benelux_iles_britanniques.json

Liste, rôles et priorités : proposition d'Ether (30/09/2026), intégrée par Claude.
Coordonnées : Wikidata (CC0), une entité par ville (QID dans les sources) ; Charleroi : Natural Earth (domaine public).
Les coordonnées candidates ont été tirées par requête SPARQL (wikidata_ratissage_1_0.json) ; le QID retenu est fixé ici à la main.
Relancer : python outils/villes/construire_villes_1_0.py (depuis la racine du dépôt).
"""
import json, unicodedata, re, pathlib

RACINE = pathlib.Path(__file__).resolve().parents[2]
CAND = json.load(open(pathlib.Path(__file__).with_name('wikidata_ratissage_1_0.json'), encoding='utf-8'))

# (pays, nom affiché, nom local si différent, requête, QID retenu, priorité, capitale, rôles, rôle selon Ether)
V = [
 ('fr','Paris',None,'Paris','Q90','A','nationale',['capitale','rail','port_fluvial','administration','aviation'],"capitale, rail national, Seine, administration, aviation"),
 ('fr','Marseille',None,'Marseille','Q23482','B',None,['port_maritime','rail'],"premier grand port méditerranéen français, Afrique/Méditerranée, rail Rhône"),
 ('fr','Lyon',None,'Lyon','Q456','B',None,['rail','port_fluvial','industrie'],"carrefour Rhône-Saône, rail, industrie, axe Paris-Méditerranée"),
 ('fr','Lille',None,'Lille','Q648','B',None,['rail','industrie','frontalier','charbon'],"rail, industrie, Belgique, bassin minier, grands axes nord-européens"),
 ('fr','Strasbourg',None,'Strasbourg','Q6602','B',None,['port_fluvial','rail','frontalier'],"Rhin, Allemagne, rail, frontière mouvante, port fluvial"),
 ('fr','Le Havre',None,'Le Havre','Q42810','B',None,['port_maritime','transatlantique','port_fluvial'],"port océanique, Seine, transatlantique"),
 ('fr','Bordeaux',None,'Bordeaux','Q1479','B',None,['port_maritime','rail'],"grand port atlantique, Garonne, rail vers Espagne et Paris"),
 ('fr','Nantes',None,'Nantes','Q12191','B',None,['port_maritime','port_fluvial','industrie'],"Loire, port, industrie, axe atlantique"),
 ('fr','Saint-Nazaire',None,'Saint-Nazaire','Q152027','B',None,['port_maritime','construction_navale'],"port en eau profonde, construction navale, embouchure de Loire"),
 ('fr','Dunkerque',None,'Dunkerque','Q45797','B',None,['port_maritime','industrie','frontalier'],"port, Belgique, mer du Nord, industrie"),
 ('fr','Calais',None,'Calais','Q6454','B',None,['port_maritime','ferry','detroit'],"détroit, ferries, Royaume-Uni, frontière maritime"),
 ('fr','Rouen',None,'Rouen','Q30974','C',None,['port_fluvial','port_maritime'],"port fluvial-maritime de la Seine, axe Paris-Manche"),
 ('fr','Cherbourg',None,'Cherbourg','Q3667188','C',None,['base_navale','port_maritime','transatlantique'],"port militaire et transatlantique, Manche"),
 ('fr','Brest',None,'Brest','Q12193','C',None,['base_navale','port_maritime'],"arsenal, Atlantique, marine"),
 ('fr','Metz',None,'Metz','Q22690','C',None,['rail','industrie','frontalier'],"rail, Lorraine industrielle, Allemagne/Luxembourg"),
 ('fr','Mulhouse',None,'Mulhouse','Q79815','C',None,['industrie','rail','frontalier'],"industrie, rail, Rhin, Allemagne/Suisse"),
 ('fr','Toulouse',None,'Toulouse','Q7880','C',None,['aviation','industrie'],"aviation, industrie, axe sud-ouest"),
 ('be','Bruxelles','Brussel','Bruxelles','Q239','A','nationale',['capitale','rail'],"capitale, nœud ferroviaire national"),
 ('be','Anvers','Antwerpen','Anvers','Q12892','B',None,['port_maritime','industrie'],"port majeur européen, Escaut, industrie, hinterland allemand"),
 ('be','Liège','Luik','Liège','Q3992','B',None,['port_fluvial','siderurgie','rail','frontalier'],"Meuse, sidérurgie, rail, Allemagne/Pays-Bas"),
 ('be','Gand','Gent','Gand','Q1296','B',None,['port_maritime','industrie'],"port et industrie, canal Gand-Terneuzen"),
 ('be','Charleroi',None,None,None,'B',None,['industrie','charbon','rail'],"industrie lourde, bassin charbonnier, rail"),
 ('be','Ostende','Oostende','Ostende','Q12996','C',None,['port_maritime','ferry'],"port et liaisons maritimes vers le Royaume-Uni"),
 ('be','Zeebruges','Zeebrugge','Zeebruges','Q184383','C',None,['port_maritime'],"port maritime, mer du Nord"),
 ('be','Namur',None,'Namur','Q134121','C',None,['rail','port_fluvial'],"confluence Sambre-Meuse, rail"),
 ('lu','Luxembourg','Lëtzebuerg',None,'Q1842','A','nationale',['capitale','rail','frontalier'],"capitale, rail, carrefour France-Belgique-Allemagne"),
 ('lu','Esch-sur-Alzette',None,'Esch-sur-Alzette','Q16010','B',None,['siderurgie','industrie','frontalier'],"sidérurgie et bassin industriel transfrontalier"),
 ('nl','Amsterdam',None,'Amsterdam','Q727','A','nationale',['capitale','port_maritime','rail'],"capitale, port, canaux, rail"),
 ('nl','Rotterdam',None,'Rotterdam','Q34370','B',None,['port_maritime','port_fluvial'],"port du Rhin-Meuse, immense rôle continental (Ether : « B, presque A »)"),
 ('nl','La Haye',"'s-Gravenhage",'La Haye','Q36600','B',None,['administration'],"siège du gouvernement, administration, côte"),
 ('nl','Utrecht',None,'Utrecht','Q803','B',None,['rail'],"principal nœud ferroviaire intérieur"),
 ('nl','Eindhoven',None,'Eindhoven','Q9832','B',None,['industrie'],"industrie et axe sud"),
 ('nl','Arnhem',None,'Arnhem','Q1310','C',None,['port_fluvial','rail','frontalier'],"Rhin, Allemagne, rail"),
 ('nl','Nimègue','Nijmegen','Nimègue','Q47887','C',None,['port_fluvial','rail','frontalier'],"Waal/Rhin, Allemagne, rail"),
 ('nl','Maastricht',None,'Maastricht','Q1309','C',None,['port_fluvial','frontalier','industrie'],"Meuse, Belgique/Allemagne, industrie"),
 ('nl','Flessingue','Vlissingen','Flessingue','Q10084','C',None,['port_maritime'],"Escaut, port maritime"),
 ('nl','IJmuiden',None,'IJmuiden','Q282461','C',None,['port_maritime','siderurgie'],"accès maritime d'Amsterdam, port, sidérurgie"),
 ('gb','Londres','London',None,'Q84','A','nationale',['capitale','port_maritime','rail','aviation'],"capitale, Tamise, rail, port, aviation, centre impérial"),
 ('gb','Liverpool',None,'Liverpool','Q24826','B',None,['port_maritime','industrie','transatlantique'],"grand port atlantique, industrie, migrations"),
 ('gb','Manchester',None,None,'Q18125','B',None,['industrie','rail'],"industrie, canal maritime, rail"),
 ('gb','Birmingham',None,None,'Q2256','B',None,['industrie','rail'],"industrie et immense nœud ferroviaire intérieur"),
 ('gb','Glasgow',None,'Glasgow','Q4093','B',None,['port_maritime','construction_navale','industrie'],"Clyde, construction navale, industrie"),
 ('gb','Édimbourg','Edinburgh','Édimbourg','Q23436','B','regionale',['rail','administration'],"capitale écossaise, rail, Firth of Forth"),
 ('gb','Newcastle','Newcastle upon Tyne',None,'Q1425428','B',None,['port_maritime','charbon','industrie'],"Tyne, charbon, industrie, port"),
 ('gb','Hull','Kingston upon Hull',None,'Q128147','B',None,['port_maritime'],"mer du Nord, commerce avec l'Europe du Nord"),
 ('gb','Southampton',None,'Southampton','Q79848','B',None,['port_maritime','transatlantique'],"grand port, transatlantique"),
 ('gb','Portsmouth',None,'Portsmouth','Q72259','B',None,['base_navale'],"grande base navale"),
 ('gb','Douvres','Dover','Douvres','Q179224','B',None,['port_maritime','ferry','detroit'],"détroit et liaisons continentales"),
 ('gb','Bristol',None,'Bristol','Q23154','B',None,['port_maritime','industrie','aviation'],"port, industrie, aviation"),
 ('gb','Cardiff',None,None,'Q10690','B',None,['port_maritime','charbon'],"charbon gallois et port"),
 ('gb','Belfast',None,'Belfast','Q10686','B',None,['port_maritime','construction_navale','industrie'],"port, construction navale, industrie"),
 ('gb','Plymouth',None,'Plymouth','Q43382','C',None,['base_navale','port_maritime'],"base navale et Atlantique"),
 ('gb','Harwich',None,'Harwich','Q990616','C',None,['ferry','port_maritime'],"ferries et mer du Nord"),
 ('ie','Dublin','Baile Átha Cliath','Dublin','Q1761','A','nationale',['capitale','port_maritime','rail'],"capitale, principal port et rail national"),
 ('ie','Cork','Corcaigh','Cork','Q36647','B',None,['port_maritime'],"grand port naturel, Atlantique"),
 ('ie','Limerick',None,'Limerick','Q133315','C',None,['port_fluvial','rail'],"Shannon, rail, ouest irlandais"),
 ('ie','Waterford',None,'Waterford','Q183551','C',None,['port_maritime','rail'],"port et réseau ferroviaire"),
 ('ie','Galway',None,'Galway','Q129610','C',None,['port_maritime'],"port occidental, Atlantique"),
 ('ie','Rosslare','Rosslare Harbour','Rosslare Harbour','Q2167772','C',None,['ferry','port_maritime'],"ferry vers la Grande-Bretagne et le continent"),
 ('je','Saint-Hélier','Saint Helier','Saint-Hélier','Q147738','C','territoire',['port_maritime'],"capitale/port, liaisons de la Manche"),
 ('gg','Saint-Pierre-Port','St Peter Port','Saint-Pierre-Port','Q174262','C','territoire',['port_maritime'],"capitale/port, liaisons de la Manche"),
 ('be','Bruges','Brugge','Bruges','Q12994','C',None,['port_maritime','rail'],"la ville et son arrière-pays, reliée à son port de Zeebruges par le canal (ajout d'Ether, 30/09)"),
 ('fr','Lorient',None,'Lorient','Q71724','C',None,['base_navale','base_sous_marine','port_maritime'],"poche allemande et base sous-marine (ajout d'Ether, 30/09 ; « C/B »)"),
 ('fr','La Rochelle',None,'La Rochelle','Q82185','C',None,['port_maritime','base_sous_marine'],"poche allemande ; La Pallice sera plus tard une entité port, pas une deuxième ville (ajout d'Ether, 30/09 ; « C/B »)"),
 ('fr','Royan',None,'Royan','Q81909','C',None,['port_maritime'],"poche allemande et accès à la Gironde (ajout d'Ether, 30/09)"),
 ('fr','Toulon',None,'Toulon','Q44160','B',None,['base_navale','port_maritime'],"énorme rôle naval méditerranéen (ajout d'Ether, 30/09)"),
 ('fr','Versailles',None,'Versailles','Q621','C',None,['quartier_general'],"quartier général allié (SHAEF) d'août 1944 à mai 1945 (ajout d'Ether, 30/09)"),
 ('nl','Den Helder',None,'Den Helder','Q33432868','C',None,['base_navale','port_maritime'],"port et base navale néerlandaise historique (ajout d'Ether, 30/09 ; « C/B »)"),
 ('nl','Groningue','Groningen','Groningue','Q749','C',None,['rail'],"nœud régional du nord (ajout d'Ether, 30/09)"),
 ('gb','Londonderry','Londonderry',None,'Q163584','B',None,['port_maritime','base_navale'],"très pertinent pour l'Atlantique : escorte des convois (ajout d'Ether, 30/09 ; « B ou C »)"),
 ('gb','Leeds',None,'Leeds','Q39121','B',None,['industrie','rail'],"industrie et rail (ajout d'Ether, 30/09)"),
 ('gb','Sheffield',None,None,'Q42448','B',None,['industrie','siderurgie','rail'],"industrie et rail (ajout d'Ether, 30/09)"),
 ('gb','Aberdeen',None,'Aberdeen','Q36405','C',None,['port_maritime'],"port de mer du Nord (ajout d'Ether, 30/09)"),
]
# coordonnées fixées à la main quand la requête par nom ne suffit pas (QID vérifié par SPARQL le 30/09/2026)
FIXE = {'Q239': (4.3517, 50.8467), 'Q1842': (6.13, 49.6114), 'Q84': (-0.1275, 51.5072), 'Q18125': (-2.2453, 53.4794),
        'Q2256': (-1.9025, 52.48), 'Q10690': (-3.1792, 51.4817), 'Q1425428': (-1.6133, 54.9778), 'Q128147': (-0.3325, 53.7444),
        'Q163584': (-7.3417, 54.9917), 'Q42448': (-1.4703, 53.3808)}
# Reims : retirée du Snapshot 0 (Guizmo, 30/09) — elle entre dans l'Atlas au ratissage de février 1945,
# quand le QG avancé du SHAEF s'y installe (source : src-defense-reims-shaef-1945).

# sources des rôles (delta de sources d'Ether, vérifié par Claude le 30/09/2026)
SOURCES_ROLES = {
  'Versailles': [('src-nara-rg331-shaef', 'présentation du RG 331', "rôle : QG du SHAEF (août 1944 - mai 1945)")],
  'Den Helder': [('src-port-den-helder-history', "page d'histoire du port", 'rôle : port et base navale')],
  'Zeebruges': [('src-port-antwerp-bruges-zeebrugge-history', "page d'histoire du port", 'rôle : port maritime')],
  'Bruges': [('src-port-antwerp-bruges-zeebrugge-history', "page d'histoire du port", 'lien avec son port de Zeebruges')],
  **{v: [('src-shd-poches-atlantique-1945', 'dossiers 1 à 3', 'poche allemande encore active en 1945')] for v in ('Lorient', 'La Rochelle', 'Royan', 'Saint-Nazaire')},
}
# autres noms sous lesquels on doit pouvoir trouver la ville (en plus du nom local et du nom anglais)
ALIAS = {'Londonderry': ['Derry'], 'Bruxelles': ['Brussels'], 'La Haye': ['Den Haag', 'The Hague']}
NE = {'Charleroi': (4.45, 50.4104)}  # Natural Earth 10m populated places

def slug(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9]+', '', s.replace("'", ''))

entites = []
for cc, nom, local, req, qid, prio, cap, roles, pourquoi in V:
    if qid in FIXE: lon, lat = FIXE[qid]; src = {'source_id': 'src-wikidata', 'locator': qid, 'usage': 'position (coordonnées)'}
    elif qid:
        c = [x for x in CAND[req] if x[1] == qid]; assert c, (nom, qid)
        lon, lat = round(c[0][2], 4), round(c[0][3], 4); src = {'source_id': 'src-wikidata', 'locator': qid, 'usage': 'position (coordonnées)'}
    else: lon, lat = NE[nom]; src = {'source_id': 'src-natural-earth-populated-places', 'locator': nom, 'usage': 'position (coordonnées)'}
    prop = {}
    if local: prop['nom_local'] = local
    prop['importance_atlas'] = prio
    if cap: prop['capitale'] = cap
    prop['roles'] = roles
    prop['note'] = f"Rôle dans l'Atlas (Ether, ratissage villes 1.0) : {pourquoi}. Rôles à sourcer."
    en = next((x[4] for x in CAND.get(req or '', []) if x[1] == qid), None)
    aliases = [a for a in dict.fromkeys([local, en, *ALIAS.get(nom, [])]) if a and a != nom]
    entites.append({
        'entite_id': f'ville-{cc}-{slug(nom)}', 'type_entite': 'ville', 'nom': nom, 'nom_court': nom, **({'aliases': aliases} if aliases else {}),
        'etats': [{
            'etat_id': 'etat-01',
            'valid_from': {'date': '', 'precision': 'inconnue'},
            'valid_to': {'date': '', 'precision': 'inconnue'},
            'statut': 'ville_au_snapshot0',
            'proprietes': prop,
            'geometrie': {'type': 'Point', 'coordinates': [lon, lat]},
            'sources': [src] + [{'source_id': i, 'locator': l, 'usage': u} for i, l, u in SOURCES_ROLES.get(nom, [])],
        }],
        'relations': [],
    })

lot = {
  'metadata_lot': {
    'nom': 'snapshot0_villes_1-0_france_benelux_iles_britanniques', 'date_reference': '1945-01-01', 'heure_reference': '00:00',
    'version': '0.3', 'statut': 'integre_par_claude', 'gabarit_source': 'gabarits/gabarit_entite_temporelle_atlas.json',
    'regles': [
      "importance_atlas A/B/C/D = priorité d'affichage automatique selon le zoom, jamais un calque à cocher",
      "A : capitales (zoom continental) ; B : grandes villes structurantes (zoom national) ; C : nœuds régionaux ; D : micro-histoire",
      "une ville ne porte ni souveraineté ni contrôle : elle prend ceux du territoire où elle se trouve, à la date affichée",
      "valid_from inconnu = ville déjà en place avant le début de l'Atlas ; un changement d'importance, de nom ou de rôle = un nouvel état daté",
      "une ville n'entre dans l'Atlas qu'à partir du moment où elle compte pour les flux (Reims : février 1945) ; elle peut en sortir ou redescendre de priorité par un nouvel état (Guizmo, 30/09)",
      "nom = nom français traditionnel quand il existe réellement ; nom_local = nom sur place ; aliases = autres noms pour la recherche (validé par Ether le 30/09)",
      "sources des rôles : par famille et par pays quand une source couvre plusieurs villes ; source propre pour un rôle particulier ou contestable (QG SHAEF, principale base navale…)",
    ],
    'integration': {'date': '2026-09-30', 'par': 'Claude', 'corrections': [
      "Liste, rôles et priorités : proposition d'Ether (ratissage villes 1.0). Rôles notés en mots-clés (roles) + la phrase d'Ether en note ; rôles à sourcer.",
      "Coordonnées : Wikidata (CC0), QID en locator de la source ; Charleroi : Natural Earth.",
      "Noms français pour l'affichage (Douvres, Édimbourg, Flessingue, Nimègue, La Haye…), nom local conservé.",
      "« Zeebruges / Bruges » : les deux, séparés (Ether, 30/09). Zeebruges deviendra une entité port quand la couche infrastructures arrivera.",
      "v0.3 (30/09) : sources des rôles ajoutées (delta d'Ether vérifié) pour Versailles, Den Helder, Bruges, Zeebruges, Lorient, La Rochelle, Royan, Saint-Nazaire.",
      "v0.2 (30/09) : 12 villes ajoutées après l'audit d'Ether (Bruges, Lorient, La Rochelle, Royan, Toulon, Versailles, Den Helder, Groningue, Londonderry, Leeds, Sheffield, Aberdeen) ; Reims retirée : elle entre au ratissage de février 1945 (Guizmo). Quand Ether hésite (« C/B »), la première lettre est retenue.",
    ]},
  },
  'entites': entites,
}
out = RACINE / 'data/snapshot0/villes_1-0_france_benelux_iles_britanniques.json'
out.write_text(json.dumps(lot, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(len(entites), 'villes ->', out.relative_to(RACINE))
