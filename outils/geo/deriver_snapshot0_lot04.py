"""
Atlas — dérivation des géométries du Snapshot 0 (1945-01-01 00:00), lot 04 : Sud, Centre, Balkans, Turquie.

Règle du Snapshot 0 : dernière situation connue AVANT le 01/01/1945 à 00:00 (rien de postérieur n'est appliqué).

1. États : relations datées d'OpenHistoricalMap, lecture juridique alliée au 01/01/1945, découpées au trait de côte
   Natural Earth 1:10m (comme les lots 01 à 03) :
     - Tchécoslovaquie = frontières d'avant Munich (1936-1938) ; Ruthénie subcarpatique et Zaolzie en sous-zones ;
     - Hongrie = frontières du Trianon (1921-1938) : les arbitrages de Vienne sont tenus pour nuls ;
     - Roumanie = frontières de septembre 1940 (sans Bessarabie, Bucovine du Nord ni Dobroudja du Sud) ; la
       Transylvanie du Nord est une zone à part (l'armistice du 12/09/1944 annule l'arbitrage de Vienne mais son
       retour n'intervient que le 09/03/1945) ;
     - Yougoslavie et Grèce = frontières d'avant-guerre ; Italie = frontières de 1929-1940 + îles de l'Égée (Dodécanèse) ;
     - Espagne et Portugal : parties européennes + îles (Baléares, Canaries, Açores, Madère), sans le Maroc espagnol,
       Ceuta, Melilla ni les colonies africaines.
2. Fronts (cartes datées d'avant le Snapshot) :
     - Italie : carte West Point n° 51, ligne du 31/12/1944 (lot04/italie_wp51.py) ;
     - Hongrie, Tchécoslovaquie : carte West Point n° 31, trait du 31/12/1944 (front_est_31dec_lonlat.json, produit par
       deriver_snapshot0_fronts.py) ; anneau de Budapest encerclée (26/12/1944).

Usage : python deriver_snapshot0_lot04.py <racine_du_depot> <dossier_cache>
"""
import json, sys, os, itertools
from shapely.geometry import box, mapping, Point, Polygon, LineString, MultiLineString, shape
from shapely.ops import unary_union, transform
import pyproj
import ohm_outils as O
from ohm_outils import *

RACINE, CACHE = sys.argv[1], sys.argv[2]
os.makedirs(CACHE, exist_ok=True)
O.CACHE = CACHE
ICI = os.path.dirname(os.path.abspath(__file__))

REL = {
    'espagne': 2862761,        # Spain 1939-04-01 → 1956
    'portugal': 2807009,       # Portugal 1910 → 1951
    'andorre': 2739874,        # Andorra
    'gibraltar': 2692855,      # Gibraltar 1713 →
    'suisse': 2798802,         # Switzerland 1874 → 1967
    'monaco': 2956942,         # Monaco 1944-09-03 → (libéré)
    'vatican': 2751259,        # Vatican City 1929-02-11 →
    'italie': 2851104,         # Italy 1929-06-07 → 1940-06-24 (frontières d'avant-guerre)
    'egee': 2920371,           # Italian Islands of the Aegean 1921 → 1943-09-11 (souveraineté italienne)
    'dodecanese_de': 2920370,  # German occupation of the Dodecanese 1943-09-11 → 1945-05-08
    'tchecoslovaquie': 2692764,  # Czechoslovakia 1936-07-03 → 1938-09-30 (avant Munich)
    'cs_apres_munich': 2747874,  # Czechoslovakia 1938-09-30 → 1938-11-02 (sert à isoler Zaolzie)
    'ruthenie': 2857483,       # Podkarpatská Rus 1920 → 1938
    'hongrie': 2695633,        # Kingdom of Hungary 1921-11-10 → 1938-11-02 (Trianon)
    'roumanie': 2693256,       # Kingdom of Romania 1940-09-07 → 1941-08-19
    'roumanie_1945': 2877966,  # Kingdom of Romania 1945-03-09 → 1947 (sert à isoler la Transylvanie du Nord)
    'bulgarie': 2848877,       # Tsardom of Bulgaria 1944-08-26 → 1946
    'yougoslavie': 2747831,    # Kingdom of Yugoslavia 1929-10-03 → 1941-04-06
    'albanie': 2878108,        # Democratic Government of Albania 1944-11-29 → 1946
    'grece': 2920399,          # Greece 1944-08-26 → 1947
    'turquie': 2864004,        # Turkey 1939-06-29 → 1964
    'malte': 2801185,          # Crown Colony of Malta
    'chypre': 2801349,         # British Cyprus 1925 → 1960
    'slovaquie': 2747847,      # Slovak Republic 1939-11-21 → 1945-04-04
    'hongrie_1938': 2747873,   # Kingdom of Hungary 1938-11-02 → 1939-03-14 (après le 1er arbitrage de Vienne)
    'ozak': 2961565,           # Operationszone Adriatisches Küstenland 1943-09-10 → 1945-05
    'ozav': 2879989,           # Operationszone Alpenvorland 1943-09-10 → 1945-05
}
G = {k: relation_ohm(v)[1] for k, v in REL.items()}
TERRES = terres(unary_union(list(G.values())).buffer(0.3))
PETITS = {'vatican', 'monaco', 'gibraltar'}   # plus petits que la résolution de Natural Earth : pas de découpage côtier
T = {k: (g if k in PETITS else g.intersection(TERRES)).buffer(0) for k, g in G.items()}

# Espagne / Portugal : Europe + îles atlantiques et méditerranéennes, sans l'Afrique continentale
EUROPE_IB = box(-10.0, 36.0, 4.5, 44.0)
CANARIES, ACORES_MADERE = box(-18.5, 27.4, -13.0, 29.5), box(-31.5, 32.3, -16.0, 40.0)
T['espagne'] = T['espagne'].intersection(unary_union([EUROPE_IB, CANARIES])).difference(G['gibraltar']).buffer(0)
T['portugal'] = T['portugal'].intersection(unary_union([EUROPE_IB, ACORES_MADERE])).buffer(0)
# Italie : sans les enclaves (Vatican, Saint-Marin restent hors d'Italie), + Dodécanèse
T['italie'] = unary_union([T['italie'], T['egee']]).difference(G['vatican']).buffer(0)
# Saseno / Sazan : italienne de 1920 à 1947 → hors d'Albanie au 01/01/1945
T['albanie'] = T['albanie'].difference(T['italie']).buffer(0)
# Zaolzie : partie de la Tchécoslovaquie d'avant Munich perdue vers la Pologne en octobre 1938 (secteur de Teschen)
perdu_1938 = T['tchecoslovaquie'].difference(G['cs_apres_munich']).intersection(box(18.2, 49.55, 19.0, 50.05))
zaolzie = unary_union([p for p in getattr(perdu_1938, 'geoms', [perdu_1938]) if km2(p) > 50]).buffer(0)
ruthenie = T['ruthenie'].intersection(T['tchecoslovaquie']).buffer(0)
# Transylvanie du Nord : Roumanie de 1945 moins Roumanie de 1940
tn = T['roumanie_1945'].difference(G['roumanie'])
transylvanie_nord = unary_union([p for p in getattr(tn, 'geoms', [tn]) if km2(p) > 1000]).buffer(0)

# ---------- Fronts ----------
EST = json.load(open(os.path.join(ICI, 'front_est_31dec_lonlat.json')))
IT = json.load(open(os.path.join(ICI, 'lot04', 'front_italie_31dec_lonlat.json')))
EQ = pyproj.Transformer.from_crs(4326, 3035, always_xy=True).transform
QE = pyproj.Transformer.from_crs(3035, 4326, always_xy=True).transform
def ouverture(g, m=2000):
    return transform(QE, transform(EQ, g).buffer(-m).buffer(m)).intersection(g).buffer(0)
p = EST['principal']
# Côté soviétique : à l'est du trait du 31/12 (fermé par la Baltique au nord et par le sud de la carte)
cote_sovietique = Polygon(p + [(p[-1][0], 40.0), (45.0, 40.0), (45.0, 60.0), (p[0][0], 60.0)]).buffer(0)
anneau_budapest = Polygon(EST['budapest']).buffer(0)
hu_sov = ouverture(T['hongrie'].intersection(cote_sovietique).difference(anneau_budapest))
budapest = T['hongrie'].intersection(anneau_budapest).buffer(0)
cs_sov = ouverture(T['tchecoslovaquie'].intersection(cote_sovietique).difference(ruthenie))
cs_sov = unary_union([q for q in getattr(cs_sov, 'geoms', [cs_sov]) if km2(q) > 100]).buffer(0)
# Italie : au nord du trait du 31/12 (fermé par les Alpes)
f = IT['front_31dec']
# fermé à l'ouest par la mer Ligure (au sud de la côte de Gênes à Vintimille) puis par les Alpes
cote_nord_italie = Polygon([(9.8, 43.6), (6.0, 43.6), (6.0, 48.0), (f[-1][0] + 3.0, 48.0), (f[-1][0] + 3.0, f[-1][1])] + f[::-1]).buffer(0)
italie_continent = T['italie'].difference(T['egee'])
it_nord = ouverture(italie_continent.intersection(cote_nord_italie))
it_sud = ouverture(italie_continent.difference(cote_nord_italie))
dodecanese = T['dodecanese_de'].intersection(T['egee']).buffer(0)
# Zones d'opérations administrées directement par l'Allemagne (partie italienne d'avant-guerre seulement)
ozak = ouverture(G['ozak'].intersection(it_nord))
ozav = ouverture(G['ozav'].intersection(it_nord))
# Tchécoslovaquie : État slovaque (Tiso) et sud annexé par la Hongrie (1er arbitrage de Vienne, 02/11/1938)
cs = T['tchecoslovaquie']
slovaquie = ouverture(G['slovaquie'].intersection(cs).difference(cs_sov).difference(ruthenie))
sud_annexe = ouverture(G['hongrie_1938'].difference(G['hongrie']).intersection(cs).difference(ruthenie).difference(cs_sov))
sud_annexe = unary_union([q for q in getattr(sud_annexe, 'geoms', [sud_annexe]) if km2(q) > 100]).buffer(0)
# Yougoslavie : côté allemand du front du 31/12 (carte 31), dans l'emprise de la carte (au nord de son bord sud)
BORD_SUD_CARTE31 = p[-1][1]
yu = T['yougoslavie']
yu_allemande = ouverture(yu.difference(cote_sovietique).intersection(box(10, BORD_SUD_CARTE31, 30, 50)))
yu_allemande = unary_union([q for q in getattr(yu_allemande, 'geoms', [yu_allemande]) if km2(q) > 100]).buffer(0)
yu_partisane = ouverture(yu.difference(yu_allemande))
# Milos : garnison allemande jusqu'au 09/05/1945 (Musée de la guerre de Milos) — l'île entière
milos = unary_union([q for q in getattr(T['grece'], 'geoms', [T['grece']]) if q.distance(Point(24.43, 36.70)) < 0.05 and km2(q) > 50]).buffer(0)

resultat = {
    'geom-territoire-es-espagne-1945-01-01': T['espagne'],
    'geom-territoire-pt-portugal-1945-01-01': T['portugal'],
    'geom-territoire-ad-andorre-1945-01-01': T['andorre'],
    'geom-territoire-gi-gibraltar-1945-01-01': T['gibraltar'],
    'geom-territoire-ch-suisse-1945-01-01': T['suisse'],
    'geom-territoire-mc-monaco-1945-01-01': T['monaco'],
    'geom-territoire-va-vatican-1945-01-01': T['vatican'],
    'geom-territoire-it-italie-1945-01-01': T['italie'],
    'geom-territoire-it-zone-allemande-nord-1945-01-01': it_nord,
    'geom-territoire-it-zone-alliee-sud-1945-01-01': it_sud,
    'geom-territoire-it-dodecanese-1945-01-01': dodecanese,
    'geom-territoire-cs-tchecoslovaquie-1945-01-01': T['tchecoslovaquie'],
    'geom-territoire-cs-ruthenie-subcarpatique-1945-01-01': ruthenie,
    'geom-territoire-cs-zaolzie-1945-01-01': zaolzie,
    'geom-territoire-cs-zone-sovietique-est-1945-01-01': cs_sov,
    'geom-territoire-hu-hongrie-1945-01-01': T['hongrie'],
    'geom-territoire-hu-zone-sovietique-1945-01-01': hu_sov,
    'geom-territoire-hu-budapest-encerclee-1945-01-01': budapest,
    'geom-territoire-ro-roumanie-1945-01-01': T['roumanie'],
    'geom-territoire-ro-transylvanie-nord-1945-01-01': transylvanie_nord,
    'geom-territoire-bg-bulgarie-1945-01-01': T['bulgarie'],
    'geom-territoire-yu-yougoslavie-1945-01-01': T['yougoslavie'],
    'geom-territoire-al-albanie-1945-01-01': T['albanie'],
    'geom-territoire-gr-grece-1945-01-01': T['grece'],
    'geom-territoire-tr-turquie-1945-01-01': T['turquie'],
    'geom-territoire-mt-malte-1945-01-01': T['malte'],
    'geom-territoire-cy-chypre-1945-01-01': T['chypre'],
    'geom-ligne_front-it-italie-1945-01-01': LineString(f),
    'geom-territoire-it-ozak-1945-01-01': ozak,
    'geom-territoire-it-ozav-1945-01-01': ozav,
    'geom-territoire-cs-slovaquie-1945-01-01': slovaquie,
    'geom-territoire-cs-sud-annexe-hongrie-1945-01-01': sud_annexe,
    'geom-territoire-yu-zone-allemande-1945-01-01': yu_allemande,
    'geom-territoire-yu-zone-partisane-1945-01-01': yu_partisane,
    'geom-territoire-gr-milos-1945-01-01': milos,
}
resultat = {k: (arrondir(v) if v.geom_type.endswith('LineString') else arrondir(v.buffer(0)).buffer(0)) for k, v in resultat.items()}  # re-valider après l'arrondi

def ohm(cle, quoi): return {'source_id': 'src-openhistoricalmap', 'locator': f'relation {REL[cle]} — {quoi}', 'usage': 'tracé de la frontière'}
NE = {'source_id': 'src-natural-earth-10m', 'locator': 'ne_10m_land + ne_10m_minor_islands', 'usage': 'trait de côte'}
WP51 = {'source_id': 'src-westpoint-italy-jun-dec1944', 'locator': 'carte 51, tireté rouge « 31 Dec. »', 'usage': 'front d’Italie au 31/12/1944'}
WP31 = {'source_id': 'src-westpoint-russian-balkan-baltic-1944', 'locator': 'carte 31, trait rouge plein « 31 Dec. » et anneau de Budapest', 'usage': 'front de l’Est au 31/12/1944'}
T_WP31 = {'snapshot': '1945-01-01T00:00', 'observation_source': '1944-12-31', 'ecart': 'le 31/12 (heure non précisée), avant le Snapshot', 'statut': 'derniere_situation_connue_avant_snapshot'}
T_WP51 = dict(T_WP31)
GEOREF31 = "Carte West Point 31 géoréférencée (23 points d'appui, plaque mince) : erreur ≈ 9 km en moyenne ; incertitude affichée 15 km."
GEOREF51 = "Carte West Point 51 (stylisée) calée sur 26 villes (affine + plaque mince lissée) : validation croisée ≈ 7 km en moyenne, 20 km au pire ; incertitude affichée 10 km."
SIMPLE = lambda cle, quoi, *pts: ([ohm(cle, quoi), NE], [f'OHM r{REL[cle]}', '∩ terres Natural Earth'], list(pts))
META = {
    'geom-territoire-es-espagne-1945-01-01': SIMPLE('espagne', 'Spain 1939-04-01 → 1956', "Espagne européenne, Baléares et Canaries. Maroc espagnol, Ceuta, Melilla, Ifni et Sahara espagnol NON inclus (hors du périmètre eurasien)."),
    'geom-territoire-pt-portugal-1945-01-01': SIMPLE('portugal', 'Portugal 1910 → 1951', "Portugal continental, Açores et Madère ; colonies non incluses."),
    'geom-territoire-ad-andorre-1945-01-01': SIMPLE('andorre', 'Andorra'),
    'geom-territoire-gi-gibraltar-1945-01-01': ([ohm('gibraltar', 'Gibraltar 1713 →')], ['OHM r2692855 (non découpé : plus petit que la résolution de Natural Earth)'], []),
    'geom-territoire-ch-suisse-1945-01-01': SIMPLE('suisse', 'Switzerland 1874 → 1967', "Liechtenstein NON inclus (entité différée, à sourcer)."),
    'geom-territoire-mc-monaco-1945-01-01': ([ohm('monaco', 'Monaco 1944-09-03 →')], ['OHM r2956942 (non découpé)'], []),
    'geom-territoire-va-vatican-1945-01-01': ([ohm('vatican', 'Vatican City 1929 →')], ['OHM r2751259 (non découpé)'], []),
    'geom-territoire-it-italie-1945-01-01': ([ohm('italie', 'Italy 1929-1940'), ohm('egee', 'Italian Islands of the Aegean 1921-1943'), NE],
        ['OHM r2851104 (frontières d’avant-guerre) ∪ Dodécanèse', '− Vatican', '∩ terres Natural Earth'],
        ["Frontières de 1929-1940 : Istrie, Fiume/Rijeka et Zara/Zadar italiennes ; annexions de 1941 (Ljubljana, Dalmatie) nulles.",
         "Saint-Marin : trou volontaire (entité différée, à sourcer)."]),
    'geom-territoire-it-zone-allemande-nord-1945-01-01': ([WP51, ohm('italie', 'Italy 1929-1940'), NE], ['Italie continentale ∩ côté nord du front du 31/12/1944'], [GEOREF51, "Comprend la zone d'opérations du littoral adriatique (Istrie, Trieste) et les Préalpes, administrées directement par l'Allemagne : à distinguer plus tard de la RSI si une source le permet."]),
    'geom-territoire-it-zone-alliee-sud-1945-01-01': ([WP51, ohm('italie', 'Italy 1929-1940'), NE], ['Italie continentale, Sicile, Sardaigne ∩ côté sud du front du 31/12/1944'], [GEOREF51]),
    'geom-territoire-it-dodecanese-1945-01-01': ([ohm('dodecanese_de', 'German occupation of the Dodecanese 1943-09-11 → 1945-05-08'), NE], ['OHM r2920370 ∩ terres Natural Earth'], ["Occupation allemande datée par OHM (1943-09-11 → 1945-05-08) : à doubler par une source A/B."]),
    'geom-territoire-cs-tchecoslovaquie-1945-01-01': SIMPLE('tchecoslovaquie', 'Czechoslovakia 1936-07-03 → 1938-09-30', "Frontières d'avant Munich (lecture alliée) : Sudètes, Zaolzie, sud de la Slovaquie et Ruthénie inclus."),
    'geom-territoire-cs-ruthenie-subcarpatique-1945-01-01': SIMPLE('ruthenie', 'Podkarpatská Rus 1920 → 1938'),
    'geom-territoire-cs-zaolzie-1945-01-01': ([ohm('tchecoslovaquie', 'Czechoslovakia 1936-1938'), ohm('cs_apres_munich', 'Czechoslovakia 1938-09-30 → 1938-11-02'), NE],
        ['Tchécoslovaquie d’avant Munich − Tchécoslovaquie d’octobre 1938, secteur de Teschen'], ["Même tracé que celui qui manque à la Pologne du lot 02 : pas de chevauchement."]),
    'geom-territoire-cs-zone-sovietique-est-1945-01-01': ([WP31, ohm('tchecoslovaquie', 'Czechoslovakia 1936-1938'), NE], ['Tchécoslovaquie ∩ côté soviétique du front du 31/12/1944, hors Ruthénie'], [GEOREF31, "PROPOSITION de Claude : est de la Slovaquie (et sud annexé par la Hongrie en 1938) déjà derrière le front soviétique."]),
    'geom-territoire-hu-hongrie-1945-01-01': SIMPLE('hongrie', 'Kingdom of Hungary 1921-1938 (Trianon)', "Arbitrages de Vienne (1938, 1940) et annexions de 1939-1941 tenus pour nuls (lecture alliée) : sud de la Slovaquie, Ruthénie, Transylvanie du Nord et Bačka hors de la Hongrie."),
    'geom-territoire-hu-zone-sovietique-1945-01-01': ([WP31, ohm('hongrie', 'Hungary 1921-1938'), NE], ['Hongrie ∩ côté soviétique du front du 31/12/1944, moins Budapest encerclée'], [GEOREF31, "PROPOSITION de Claude, dérivée du front."]),
    'geom-territoire-hu-budapest-encerclee-1945-01-01': ([WP31, ohm('hongrie', 'Hungary 1921-1938')], ['Hongrie ∩ anneau d’encerclement de Budapest (carte 31)'], [GEOREF31, "PROPOSITION de Claude : encerclement du 26/12/1944 ; anneau stylisé sur la carte."]),
    'geom-territoire-ro-roumanie-1945-01-01': SIMPLE('roumanie', 'Kingdom of Romania 1940-09-07 → 1941-08-19', "Frontières de septembre 1940 : Bessarabie et Bucovine du Nord soviétiques (confirmées par l'armistice), Dobroudja du Sud bulgare, Transylvanie du Nord à part."),
    'geom-territoire-ro-transylvanie-nord-1945-01-01': ([ohm('roumanie_1945', 'Kingdom of Romania 1945-03-09 → 1947'), ohm('roumanie', 'Kingdom of Romania 1940-1941'), NE],
        ['Roumanie de mars 1945 − Roumanie de septembre 1940', 'morceaux > 1 000 km²'], ["PROPOSITION de Claude : au 01/01/1945, arbitrage de Vienne annulé par l'armistice (art. 19) mais retour à l'administration roumaine seulement le 09/03/1945 ; administration militaire soviétique depuis novembre 1944 (à sourcer)."]),
    'geom-territoire-bg-bulgarie-1945-01-01': SIMPLE('bulgarie', 'Tsardom of Bulgaria 1944-08-26 → 1946', "Frontières de 1940 (Dobroudja du Sud comprise, traité de Craiova) ; territoires grecs et yougoslaves évacués (armistice du 28/10/1944)."),
    'geom-territoire-yu-yougoslavie-1945-01-01': SIMPLE('yougoslavie', 'Kingdom of Yugoslavia 1929-1941', "Frontières d'avant-guerre. Contrôle réel morcelé (Partisans, Allemands, État indépendant de Croatie) : seul le front de l'Est (carte 31) est tracé, pas de zones sans carte datée."),
    'geom-territoire-al-albanie-1945-01-01': SIMPLE('albanie', 'Democratic Government of Albania 1944-11-29 → 1946', "Île de Saseno (Sazan) exclue : italienne de 1920 à 1947."),
    'geom-territoire-gr-grece-1945-01-01': SIMPLE('grece', 'Greece 1944-08-26 → 1947', "Frontières d'avant-guerre, sans le Dodécanèse (italien jusqu'en 1947). Garnisons allemandes encore présentes (ouest de la Crète, Milos) et combats d'Athènes : non tracés faute de carte datée."),
    'geom-territoire-tr-turquie-1945-01-01': SIMPLE('turquie', 'Turkey 1939-06-29 → 1964', "Turquie entière (Hatay compris depuis 1939)."),
    'geom-territoire-mt-malte-1945-01-01': SIMPLE('malte', 'Crown Colony of Malta'),
    'geom-territoire-cy-chypre-1945-01-01': SIMPLE('chypre', 'British Cyprus 1925 → 1960'),
    'geom-territoire-it-ozak-1945-01-01': ([ohm('ozak', 'Operationszone Adriatisches Küstenland 1943-09-10 → 1945-05'), WP51], ['OHM r2961565 ∩ Italie du Nord (partie italienne d’avant-guerre)'], ["La partie slovène (province de Ljubljana) est dans la zone allemande de Yougoslavie."]),
    'geom-territoire-it-ozav-1945-01-01': ([ohm('ozav', 'Operationszone Alpenvorland 1943-09-10 → 1945-05'), WP51], ['OHM r2879989 ∩ Italie du Nord'], []),
    'geom-territoire-cs-slovaquie-1945-01-01': ([ohm('slovaquie', 'Slovak Republic 1939-11-21 → 1945-04-04'), ohm('tchecoslovaquie', 'Czechoslovakia 1936-1938'), WP31], ['OHM r2747847 ∩ Tchécoslovaquie', '− zone soviétique du 31/12 − Ruthénie'], ["Territoire effectivement tenu par l'État slovaque et l'armée allemande au 31/12/1944 (à l'ouest du front)."]),
    'geom-territoire-cs-sud-annexe-hongrie-1945-01-01': ([ohm('hongrie_1938', 'Kingdom of Hungary 1938-11-02 → 1939-03-14'), ohm('hongrie', 'Hungary 1921-1938'), WP31], ['(Hongrie de novembre 1938 − Hongrie du Trianon) ∩ Tchécoslovaquie', '− Ruthénie − zone soviétique du 31/12'], ["Sud de la Slovaquie annexé par la Hongrie (1er arbitrage de Vienne, 02/11/1938), partie encore à l'ouest du front."]),
    'geom-territoire-yu-zone-allemande-1945-01-01': ([WP31, ohm('yougoslavie', 'Kingdom of Yugoslavia 1929-1941'), NE], ['Yougoslavie ∩ côté allemand du front du 31/12/1944, au nord du bord sud de la carte 31'], [GEOREF31, "La carte 31 figure tout l'ouest yougoslave en zone allemande ; la côte dalmate (Split, Zadar, Šibenik) et d'autres régions étaient pourtant déjà aux mains des Partisans : carte à l'échelle des armées, à affiner avec une carte yougoslave datée."]),
    'geom-territoire-yu-zone-partisane-1945-01-01': ([WP31, ohm('yougoslavie', 'Kingdom of Yugoslavia 1929-1941'), NE], ['Yougoslavie − zone allemande'], [GEOREF31, "Au sud du bord de la carte 31 (Monténégro méridional, Kosovo, Macédoine), zone rattachée par défaut aux Partisans : régions libérées en novembre-décembre 1944, à sourcer."]),
    'geom-territoire-gr-milos-1945-01-01': ([ohm('grece', 'Greece 1944-1947'), NE, {'source_id': 'src-milos-war-museum', 'locator': 'World War II', 'usage': 'occupation allemande du 09/05/1941 au 09/05/1945'}], ['île de Milos (Natural Earth ∩ Grèce)'], ["L'île entière : la source décrit une garnison retranchée d'environ 500 hommes, pas ses limites exactes."]),
    'geom-ligne_front-it-italie-1945-01-01': ([WP51], ['relevé du tireté « 31 Dec. » (et du trait plein inchangé à l’ouest)', 'calage sur 26 villes'], [GEOREF51, "Ligne Gothique d'hiver : côte tyrrhénienne (Versilia) → Apennins au sud de Bologne → Adriatique au nord de Ravenne."]),
}
TEMPS = {k: T_WP31 for k in ['geom-territoire-cs-zone-sovietique-est-1945-01-01', 'geom-territoire-hu-zone-sovietique-1945-01-01', 'geom-territoire-hu-budapest-encerclee-1945-01-01',
         'geom-territoire-yu-zone-allemande-1945-01-01', 'geom-territoire-yu-zone-partisane-1945-01-01']}
TEMPS.update({k: T_WP51 for k in ['geom-territoire-it-zone-allemande-nord-1945-01-01', 'geom-territoire-it-zone-alliee-sud-1945-01-01', 'geom-ligne_front-it-italie-1945-01-01']})
INCERT = {k: 15 for k in TEMPS if 'it-' not in k}; INCERT.update({k: 10 for k in TEMPS if 'it-' in k})

sortie = os.path.join(RACINE, 'data', 'geometries', 'snapshot0')
for gid, g in resultat.items():
    sources, ops, points = META[gid]
    rels = sorted({int(x['locator'].split()[1]) for x in sources if x['source_id'] == 'src-openhistoricalmap'})
    lic = [l for r in rels for l in licences_segments(r)]
    carte = gid in TEMPS
    props = {'geometry_id': gid, 'date_validite': DATE, 'statut': 'provisoire_carte_georeferencee' if carte else 'provisoire_ohm',
             'sources': sources, 'method': 'carte_georeferencee_puis_intersection' if carte else 'extraction_ohm_puis_decoupage_trait_de_cote',
             'operations': ops, 'precision': 'voir points_a_verifier' if carte else 'frontières terrestres : celles d’OHM ; côtes : Natural Earth 1:10m (~1 km)',
             'zone_incertitude_km': INCERT.get(gid), 'surface_km2': round(km2(g)) if not g.geom_type.endswith('LineString') else None,
             'logiciel': 'Python — Shapely/GEOS, SciPy', 'script': 'outils/geo/deriver_snapshot0_lot04.py', 'date_creation': AUJOURDHUI, 'auteur': 'Claude',
             'licence': 'CC0 (OpenHistoricalMap) + segments sous licence d’origine listés dans licences_segments : à créditer' if lic else 'CC0 (OpenHistoricalMap) ; Natural Earth : domaine public',
             'licences_segments': lic, 'points_a_verifier': points}
    if gid in TEMPS: props['reference_temporelle'] = TEMPS[gid]
    with open(os.path.join(sortie, gid + '.geojson'), 'w', encoding='utf-8') as fh:
        json.dump({'type': 'Feature', 'geometry': mapping(g), 'properties': props}, fh, ensure_ascii=False, separators=(',', ':'))
    print(f"{gid:60} {(str(round(km2(g)))+' km²') if not g.geom_type.endswith('LineString') else str(round(g.length,2))+' °':>12}  {g.geom_type}")

# ---------- Contrôles : pas de chevauchement entre États (lots 01 à 04) ----------
lu = lambda gid: shape(json.load(open(os.path.join(sortie, gid + '.geojson')))['geometry'])
etats = ['es-espagne', 'pt-portugal', 'ad-andorre', 'gi-gibraltar', 'ch-suisse', 'mc-monaco', 'va-vatican', 'it-italie', 'cs-tchecoslovaquie', 'hu-hongrie',
         'ro-roumanie', 'ro-transylvanie-nord', 'bg-bulgarie', 'yu-yougoslavie', 'al-albanie', 'gr-grece', 'tr-turquie', 'mt-malte', 'cy-chypre',
         'de-allemagne', 'at-autriche', 'pl-pologne', 'su-urss', 'fr-france']
tops = {k: lu(f'geom-territoire-{k}-1945-01-01') for k in etats}
for (a, ga), (b, gb) in itertools.combinations(tops.items(), 2):
    if not ga.envelope.intersects(gb.envelope): continue
    o = km2(ga.intersection(gb))
    if o > 1: print(f'CHEVAUCHEMENT {a} / {b} : {o:,.0f} km²')
