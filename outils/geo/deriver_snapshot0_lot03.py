"""
Atlas — dérivation des géométries du Snapshot 0 (1945-01-01), lot 03 : Nord et Ouest européen.

1. Territoires souverains : relations datées d'OpenHistoricalMap (lecture juridique alliée), découpées au trait de côte
   Natural Earth 1:10m, comme les lots 01 et 02.
     - France = frontières de 1918-1940 (Alsace-Moselle comprise), métropole + Corse (l'Algérie est retirée) ;
     - Belgique = frontières de 1920 (Eupen-Malmedy compris) ; Luxembourg = frontières d'avant l'annexion ;
     - Norvège sans Svalbard ni Jan Mayen (statut militaire différent, à traiter à part) ;
     - Îles Anglo-Normandes (Jersey, Guernesey) séparées du Royaume-Uni ; Féroé séparées du Danemark.
2. Zones de contrôle, dérivées de la ligne de front (cartes géoréférencées par outils/geo/lot03/).
   RÈGLE DU SNAPSHOT 0 : dernière situation connue AVANT le 01/01/1945 à 00:00 (ce qui vient après = ratissage de janvier) :
     - carte LOC du 12e groupe d'armées, situation du 31/12/1944 à midi (front des Pays-Bas à l'Alsace) ;
     - carte West Point n° 70, front du 15/12/1944 (sud de la poche de Colmar, hors de la carte LOC) ;
     - carte West Point n° 71, situation du 15/12/1944 (poches de l'Atlantique et de Dunkerque).
   « Côté allemand » = polygone fermé par la ligne de front, puis intersecté avec chaque pays ; ouverture
   morphologique de 1,5 km pour supprimer les liserés parasites le long des frontières que suit le front.
3. Est-Finnmark : Norvège à l'est de la Tana (Store norske leksikon : les Soviétiques s'arrêtent à la Tana).

Usage : python deriver_snapshot0_lot03.py <racine_du_depot> <dossier_cache>
(les fichiers lot03/*.json produits par le géoréférencement doivent être dans outils/geo/lot03/)
"""
import json, sys, os, itertools
from shapely.geometry import box, mapping, Point, Polygon, LineString, MultiLineString, shape
from shapely.ops import unary_union, split, transform
import pyproj
import ohm_outils as O
from ohm_outils import *

RACINE, CACHE = sys.argv[1], sys.argv[2]
os.makedirs(CACHE, exist_ok=True)
O.CACHE = CACHE
ICI = os.path.dirname(os.path.abspath(__file__))
L3 = lambda f: json.load(open(os.path.join(ICI, 'lot03', f)))

REL = {
    'danemark': 2851793,     # Danmark 1944-06-17 →
    'feroe': 2828341,        # Føroyar (niveau 4, sous le Danemark) 1035 → 1999
    'norvege': 2851798,      # Norge 1925-08-14 → 2004
    'suede': 2870046,        # Sverige 1932-01-30 → 1979
    'islande': 2801982,      # Ísland 1944-06-17 →
    'royaume_uni': 2693292,  # United Kingdom 1922-12-05 → 1987
    'jersey': 2828299,       # Jersey 1290 → 1987
    'guernesey': 2828270,    # Guernsey 1290 → 1987
    'irlande': 2692985,      # Éire / Ireland 1937-12-29 → 2006
    'france': 2696299,       # French Republic 1918-11-22 → 1940-06-22 (lecture alliée : Alsace-Moselle française)
    'belgique': 2800293,     # Belgium 1920-01-10 → 1940-06-25 (avec Eupen-Malmedy)
    'luxembourg': 2748545,   # Luxembourg 1840-09-12 → 1940-07-29
    'pays_bas': 2883430,     # Koninkrijk der Nederlanden 1848-10-14 → 1949
}
CADRE = {  # on ne garde que la partie européenne / métropolitaine
    'norvege': box(3.0, 57.5, 32.5, 71.6), 'royaume_uni': box(-9.0, 49.7, 2.2, 61.0), 'france': box(-6.0, 41.0, 10.0, 51.3),
    'pays_bas': box(3.0, 50.5, 7.5, 54.0), 'danemark': box(7.5, 54.4, 15.5, 58.0),
}
G = {}
for k, v in REL.items():
    g = relation_ohm(v)[1]
    G[k] = g.intersection(CADRE[k]) if k in CADRE else g
TERRES = terres(unary_union(list(G.values())).buffer(0.5))
T = {k: g.intersection(TERRES).buffer(0) for k, g in G.items()}
# Un seul propriétaire par morceau de terre : le Danemark ne garde pas les Féroé si la relation les contient
T['danemark'] = T['danemark'].difference(T['feroe'])

# ---------- Est-Finnmark : à l'est de la Tana ----------
TANA = [(28.014, 70.071), (28.05, 70.12), (28.19, 70.20), (28.25, 70.33), (28.33, 70.45), (28.28, 70.65), (28.22, 70.90), (28.2, 71.4)]
est_tana = Polygon(TANA + [(32.5, 71.4), (32.5, 68.8), (28.0, 68.8)])
est_finnmark = T['norvege'].intersection(est_tana).buffer(0)

# ---------- Front occidental ----------
# RÈGLE DU SNAPSHOT 0 (Guizmo, 28/09/2026) : on part de la DERNIÈRE situation connue AVANT le 01/01/1945 à 00:00.
# Tout ce qui est observé après (même la carte du 01/01 à 12:00) entre au ratissage de janvier comme nouvel état.
F = L3('front_loc_12ag_1944-12-31_lonlat.json')   # carte LOC « Situation 1200 hrs 31 December 1944 »
S = L3('alsace_sud_wp70_lonlat.json')              # sud de la poche de Colmar au 15/12/1944 (West Point 70), hors carte LOC
fin = F['principal'][-1]
sud = [p for p in S['front_15dec'] if p[1] < fin[1] - 0.02]     # partie au sud de la carte LOC
principal = F['principal'] + sud                                 # raccord LOC → West Point : segment droit court
front = MultiLineString([F['walcheren'], F['beveland'], F['tholen'], principal])
# Côté allemand : fermé par la mer du Nord à l'ouest/nord, par l'Allemagne à l'est
cote_allemand = Polygon(F['walcheren'] + F['beveland'] + F['tholen'] + principal +
                        [(7.62, 47.585), (13.0, 47.585), (13.0, 55.5), (2.8, 55.5), (2.8, 51.62), (3.30, 51.62)]).buffer(0)
EQ = pyproj.Transformer.from_crs(4326, 3035, always_xy=True).transform
QE = pyproj.Transformer.from_crs(3035, 4326, always_xy=True).transform
def ouverture(g, m=1500):
    return transform(QE, transform(EQ, g).buffer(-m).buffer(m)).intersection(g).buffer(0)
def morceaux(g, mini=5):
    ps = list(g.geoms) if g.geom_type == 'MultiPolygon' else ([g] if not g.is_empty else [])
    return [p for p in ps if km2(p) >= mini]
zone = {k: ouverture(T[k].intersection(cote_allemand)) for k in ['belgique', 'luxembourg', 'pays_bas']}
# France : là où le front suit le Rhin ou la frontière (Lauter, Sarre), le trait de la carte laisse des liserés de 2 à 5 km
# qui ne sont pas des zones tenues : ouverture plus forte (3 km). La poche de Colmar (≈ 40 km de large) n'est pas touchée.
zone['france'] = ouverture(T['france'].intersection(cote_allemand), 3000)
zone_de_alliee = ouverture(relation_ohm(2693085)[1].intersection(TERRES).intersection(box(5.5, 47.7, 9.0, 52.5)).difference(cote_allemand), 3000)  # Allemagne 1937 côté allié
colmar = unary_union([p for p in morceaux(zone['france'], 30) if p.centroid.y < 48.45])
fr_nord = unary_union([p for p in morceaux(zone['france'], 30) if p.centroid.y >= 48.45])

# ---------- Poches de l'Atlantique et de Dunkerque (carte West Point 71) ----------
A = L3('poches_wp71_lonlat.json')
VILLE = {'dunkerque': [(2.37, 51.03)], 'lorient': [(-3.37, 47.75)], 'saint_nazaire': [(-2.21, 47.27), (-2.17, 47.23)],
         'la_rochelle': [(-1.15, 46.16)], 'royan': [(-1.03, 45.62)], 'pointe_de_grave': [(-1.07, 45.56)]}
def prolonger(c, km=6):
    """Prolonge l'arc à ses deux bouts (tangente) pour qu'il coupe franchement la terre malgré l'imprécision de la carte."""
    import math
    def bout(a, b):
        dx, dy = a[0] - b[0], a[1] - b[1]; n = math.hypot(dx, dy) or 1
        return (a[0] + dx / n * km / 75, a[1] + dy / n * km / 111)
    return [bout(c[0], c[3])] + c + [bout(c[-1], c[-4])]
poches = []
for k, arc in A.items():
    # Chaque arc entoure un port : on ferme l'arc par un point lointain, en mer, dans l'axe « milieu de l'arc → port »,
    # et on garde la terre française comprise dans ce cône (plus robuste que de couper la terre : l'arc, stylisé,
    # n'atteint pas toujours exactement la côte).
    ax, ay = sum(p[0] for p in arc) / len(arc), sum(p[1] for p in arc) / len(arc)
    vx, vy = VILLE[k][0]
    loin = (vx + (vx - ax) * 4, vy + (vy - ay) * 4)
    cone = Polygon(prolonger(arc, 3) + [loin]).buffer(0)
    local = T['france'].intersection(cone)
    garde = [p for p in (local.geoms if local.geom_type == 'MultiPolygon' else [local]) if any(p.distance(Point(v)) < 0.03 for v in VILLE[k])]
    poches += garde
    print(f"poche {k:16} {sum(km2(p) for p in garde):7.0f} km²")
# Îles (Groix, Belle-Île, Ré, Oléron, Noirmoutier) : PAS rattachées tant qu'une source ne fixe pas leur statut au 01/01/1945
# (décision Ether, 28/09/2026 : pas de remplissage automatique).
poches_atl = unary_union(poches).buffer(0)

resultat = {
    'geom-territoire-dk-danemark-1945-01-01': T['danemark'],
    'geom-territoire-dk-feroe-1945-01-01': T['feroe'],
    'geom-territoire-no-norvege-1945-01-01': T['norvege'],
    'geom-territoire-no-est-finnmark-1945-01-01': est_finnmark,
    'geom-territoire-se-suede-1945-01-01': T['suede'],
    'geom-territoire-is-islande-1945-01-01': T['islande'],
    'geom-territoire-gb-royaume-uni-1945-01-01': T['royaume_uni'],
    'geom-territoire-je-jersey-1945-01-01': T['jersey'],
    'geom-territoire-gg-guernesey-1945-01-01': T['guernesey'],
    'geom-territoire-ie-irlande-1945-01-01': T['irlande'],
    'geom-territoire-fr-france-1945-01-01': T['france'],
    'geom-territoire-fr-poches-atlantiques-1945-01-01': poches_atl,
    'geom-territoire-fr-poche-colmar-1945-01-01': colmar,
    'geom-territoire-be-belgique-1945-01-01': T['belgique'],
    'geom-territoire-be-zone-allemande-ardennes-1945-01-01': zone['belgique'],
    'geom-territoire-lu-luxembourg-1945-01-01': T['luxembourg'],
    'geom-territoire-lu-zone-allemande-ardennes-1945-01-01': zone['luxembourg'],
    'geom-territoire-nl-pays-bas-1945-01-01': T['pays_bas'],
    'geom-territoire-nl-zone-liberee-sud-1945-01-01': ouverture(T['pays_bas'].difference(zone['pays_bas'])),
    'geom-territoire-de-zone-alliee-ouest-1945-01-01': unary_union(morceaux(zone_de_alliee, 30)),
    'geom-ligne_front-de-ouest-europe-1945-01-01': front,
}
if not fr_nord.is_empty: resultat['geom-territoire-fr-zone-allemande-nord-est-1945-01-01'] = fr_nord
resultat = {k: (arrondir(v) if v.geom_type.endswith('LineString') else arrondir(v.buffer(0)).buffer(0)) for k, v in resultat.items()}  # re-valider après l'arrondi

def ohm(cle, quoi): return {'source_id': 'src-openhistoricalmap', 'locator': f'relation {REL[cle]} — {quoi}', 'usage': 'tracé de la frontière'}
NE = {'source_id': 'src-natural-earth-10m', 'locator': 'ne_10m_land + ne_10m_minor_islands', 'usage': 'trait de côte'}
LOC = {'source_id': 'src-loc-12ag-1944-12-31', 'locator': 'situation 1200 hrs, 31 December 1944 ; trait noir épais « front line »', 'usage': 'dernière position du front connue avant le Snapshot, géoréférencée'}
WP70 = {'source_id': 'src-westpoint-6-12ag-1944-11-12', 'locator': 'carte 70, trait rouge plein « 8 Nov.-15 Dec. »', 'usage': 'sud de la poche de Colmar au 15/12/1944'}
WP71 = {'source_id': 'src-westpoint-general-situation-1944-12-15', 'locator': 'carte 71, arcs rouges des poches', 'usage': 'limites des poches'}
SNL = {'source_id': 'src-snl-east-finnmark-1944', 'locator': 'Tana', 'usage': 'limite ouest de la zone soviétique'}
NE_R = {'source_id': 'src-natural-earth-10m', 'locator': 'ne_10m_rivers_europe « Tana River »', 'usage': 'cours de la Tana'}
GEOREF_LOC = "Carte LOC géoréférencée par ajustement automatique de ~9 900 points des fleuves Natural Earth sur les fleuves bleus de la carte (Lambert + polynôme d'ordre 2) : écart ≈ 1 à 2 km ; trait du front ≈ 1 km de large. Incertitude retenue : 3 km."
SIMPLE = lambda cle, quoi, *pts: ([ohm(cle, quoi), NE], [f'OHM r{REL[cle]}', '∩ terres Natural Earth'], list(pts))
META = {
    'geom-territoire-dk-danemark-1945-01-01': SIMPLE('danemark', 'Danmark 1944-06-17 →', "Frontière germano-danoise de 1920. Bornholm compris."),
    'geom-territoire-dk-feroe-1945-01-01': SIMPLE('feroe', 'Føroyar 1035 → 1999'),
    'geom-territoire-no-norvege-1945-01-01': SIMPLE('norvege', 'Norge 1925-08-14 → 2004',
        "Svalbard, Jan Mayen et l'île aux Ours NON inclus : garnison norvégienne au Spitzberg depuis 1942 et stations météo allemandes isolées, donc pas « sous contrôle allemand ». Entité séparée à créer si une source le permet.",
        "Frontière norvégo-soviétique : celle d'OHM ; à comparer avec Petsamo (lot 01)."),
    'geom-territoire-no-est-finnmark-1945-01-01': ([ohm('norvege', 'Norge'), NE_R, SNL],
        ['Norvège ∩ zone à l’est de la Tana', 'Tana : Natural Earth jusqu’à Polmak, puis tracé approché jusqu’au Tanafjord'],
        ["Limite ouest = la Tana (arrêt soviétique). Cours aval de la Tana (Polmak → fjord) approché à ~3 km près.",
         "À l'ouest de la Tana, zone évacuée et incendiée par les Allemands : laissée dans la Norvège sous contrôle allemand, sans frontière inventée (consigne d'Ether)."]),
    'geom-territoire-se-suede-1945-01-01': SIMPLE('suede', 'Sverige 1932-01-30 → 1979'),
    'geom-territoire-is-islande-1945-01-01': SIMPLE('islande', 'Ísland 1944-06-17 →'),
    'geom-territoire-gb-royaume-uni-1945-01-01': SIMPLE('royaume_uni', 'United Kingdom 1922-12-05 → 1987',
        "Île de Man NON incluse (dépendance de la Couronne, comme Jersey et Guernesey) : entité à ajouter avec une source."),
    'geom-territoire-je-jersey-1945-01-01': SIMPLE('jersey', 'Jersey 1290 → 1987'),
    'geom-territoire-gg-guernesey-1945-01-01': SIMPLE('guernesey', 'Guernsey 1290 → 1987', "Bailliage : Guernesey, Aurigny, Sercq, Herm."),
    'geom-territoire-ie-irlande-1945-01-01': SIMPLE('irlande', 'Éire / Ireland 1937-12-29 → 2006'),
    'geom-territoire-fr-france-1945-01-01': SIMPLE('france', 'French Republic 1918-11-22 → 1940-06-22',
        "Frontières de 1918-1940, Alsace-Moselle comprise (lecture juridique alliée). Monaco exclu (enclave). Frontière franco-italienne d'avant 1947 (Tende et La Brigue italiens)."),
    'geom-territoire-fr-poches-atlantiques-1945-01-01': ([WP71, ohm('france', 'French Republic'), NE, {'source_id': 'src-chemins-poches-atlantique-1945', 'locator': '', 'usage': 'liste des poches, île de Ré'}],
        ['arcs rouges de la carte West Point 71 (15/12/1944), géoréférencée sur les côtes et fleuves Natural Earth (écart ≈ 3 km)',
         'terre française coupée par chaque arc ; on garde le côté du port', 'îles non incluses (attente de source par île)'],
        ["Carte au 1:5 000 000 environ : incertitude ≈ 5 km. Situation du 15/12/1944, inchangée au 01/01/1945 pour ces poches (fronts figés de l'automne 1944 au printemps 1945).",
         "Dunkerque, Lorient, Saint-Nazaire (deux rives de la Loire), La Rochelle/La Pallice, Royan et pointe de Grave.",
         "Îles NON rattachées (Groix, Belle-Île, Ré, Oléron, Noirmoutier) : chacune attend une source qui établit son statut au 01/01/1945."]),
    'geom-territoire-fr-poche-colmar-1945-01-01': ([LOC, WP70, ohm('france', 'French Republic'), NE],
        ['France ∩ côté allemand du front', 'nord et ouest : carte LOC du 31/12/1944 ; sud (Vosges → Mulhouse → Rhin) : trait du 15/12/1944 de la carte West Point 70'],
        [GEOREF_LOC, "Partie sud tirée du front du 15/12/1944 (West Point 70, carte stylisée, calée sur 11 villes, écart moyen 1,7 km) : incertitude ≈ 5 km dans ce secteur.",
         "Raccord LOC → West Point au bord sud de la carte LOC par un segment droit court."]),
    'geom-territoire-be-belgique-1945-01-01': SIMPLE('belgique', 'Belgium 1920-01-10 → 1940-06-25', "Frontière de 1920, Eupen-Malmedy compris (lecture alliée)."),
    'geom-territoire-be-zone-allemande-ardennes-1945-01-01': ([LOC, ohm('belgique', 'Belgium 1920-1940'), NE], ['Belgique ∩ côté allemand du front LOC du 31/12/1944'], [GEOREF_LOC, "Situation du 31/12 à midi (dernière connue avant le Snapshot), pas l'extension maximale de l'offensive (24-26/12)."]),
    'geom-territoire-lu-luxembourg-1945-01-01': SIMPLE('luxembourg', 'Luxembourg 1840-09-12 → 1940-07-29'),
    'geom-territoire-lu-zone-allemande-ardennes-1945-01-01': ([LOC, ohm('luxembourg', 'Luxembourg'), NE], ['Luxembourg ∩ côté allemand du front LOC du 31/12/1944'], [GEOREF_LOC]),
    'geom-territoire-nl-pays-bas-1945-01-01': SIMPLE('pays_bas', 'Koninkrijk der Nederlanden 1848-10-14 → 1949', "Partie européenne seulement."),
    'geom-territoire-nl-zone-liberee-sud-1945-01-01': ([LOC, ohm('pays_bas', 'Nederland'), NE], ['Pays-Bas moins le côté allemand du front LOC du 31/12/1944'],
        [GEOREF_LOC, "Walcheren, Nord- et Zuid-Beveland libérés ; Schouwen-Duiveland, Tholen-nord et Goeree-Overflakkee encore allemands (arcs de front de la carte)."]),
    'geom-territoire-de-zone-alliee-ouest-1945-01-01': ([LOC, {'source_id': 'src-openhistoricalmap', 'locator': 'relation 2693085 — German Reich 1936-1938', 'usage': 'frontières de 1937'}, NE],
        ['Allemagne (1937) ∩ côté allié du front LOC du 31/12/1944', 'ouverture 3 km, morceaux de moins de 30 km² retirés'], [GEOREF_LOC, "Région d'Aix-la-Chapelle et bordures de la Sarre et du Palatinat tenues par les Alliés. PROPOSITION de Claude, à valider par Ether."]),
    'geom-ligne_front-de-ouest-europe-1945-01-01': ([LOC, WP70], ['trait du front extrait automatiquement (seuil de noir + ouverture morphologique + squelette)', '+ trait du 15/12/1944 au sud de Colmar (West Point 70)'],
        [GEOREF_LOC, "Les arcs de Zélande (Walcheren, Beveland) sont des morceaux séparés, comme sur la carte.", "Poches de l'Atlantique et Dunkerque : voir la géométrie des poches (limites propres)."]),
    'geom-territoire-fr-zone-allemande-nord-est-1945-01-01': ([LOC, ohm('france', 'French Republic'), NE], ['France ∩ côté allemand du front, au nord de 48,45° N'], [GEOREF_LOC, "Secteur de Bitche / nord de l'Alsace tenu par les Allemands au 01/01 (avant l'opération Nordwind, lancée vers 23:00 le 31/12). PROPOSITION de Claude, à valider."]),
}
# ---------- Référence temporelle (règle du Snapshot 0) ----------
# Snapshot 0 = état au 01/01/1945 à 00:00, construit avec la DERNIÈRE situation connue AVANT ce moment.
SUIVANT = ("État suivant connu (ratissage de janvier) : carte LOC du 01/01/1945 à 12:00 (item 2004630304) ; écart médian 0,7 km avec celle du 31/12, "
           "secteurs changés ≈ 31 km² à l'ouest de Bastogne et ≈ 20 km² vers Monschau (outils/geo/lot03/comparer_31dec_01jan.py).")
LOC_T = {'snapshot': '1945-01-01T00:00', 'observation_source': '1944-12-31T12:00', 'ecart': '12 h avant',
         'statut': 'derniere_situation_connue_avant_snapshot', 'etat_suivant': SUIVANT}
TEMPS = {k: LOC_T for k in ['geom-ligne_front-de-ouest-europe-1945-01-01', 'geom-territoire-be-zone-allemande-ardennes-1945-01-01',
         'geom-territoire-lu-zone-allemande-ardennes-1945-01-01', 'geom-territoire-nl-zone-liberee-sud-1945-01-01',
         'geom-territoire-de-zone-alliee-ouest-1945-01-01', 'geom-territoire-fr-zone-allemande-nord-est-1945-01-01']}
TEMPS['geom-territoire-fr-zone-allemande-nord-est-1945-01-01'] = dict(LOC_T, note="Situation antérieure à l'offensive Nordwind (lancée vers 23:00 le 31/12) : ses gains entrent au ratissage de janvier.")
TEMPS['geom-ligne_front-de-ouest-europe-1945-01-01'] = dict(LOC_T, observation_source='1944-12-31T12:00 (sud de Colmar : 1944-12-15)')
TEMPS['geom-territoire-fr-poche-colmar-1945-01-01'] = {'snapshot': '1945-01-01T00:00', 'observation_source': 'nord et ouest : 1944-12-31T12:00 (LOC) ; sud : 1944-12-15 (West Point 70)',
    'ecart': '12 h avant (nord et ouest) ; 17 jours avant (sud)', 'statut': 'derniere_situation_connue_avant_snapshot',
    'etat_suivant': "Janvier : offensive Sonnenwende (7-13/01) au nord de la poche, puis réduction de la poche à partir du 20/01 (West Point 75a). " + SUIVANT}
TEMPS['geom-territoire-fr-poches-atlantiques-1945-01-01'] = {'snapshot': '1945-01-01T00:00', 'observation_source': '1944-12-15', 'ecart': '17 jours avant',
    'statut': 'derniere_situation_connue_avant_snapshot', 'etat_suivant': "Pas de changement connu avant le printemps 1945 (fronts figés)."}
TEMPS['geom-territoire-no-est-finnmark-1945-01-01'] = {'snapshot': '1945-01-01T00:00', 'observation_source': 'arrêt soviétique sur la Tana, novembre 1944 (SNL)', 'ecart': 'environ 7 semaines avant',
    'statut': 'derniere_situation_connue_avant_snapshot'}
sortie = os.path.join(RACINE, 'data', 'geometries', 'snapshot0')
os.makedirs(sortie, exist_ok=True)
for gid, g in resultat.items():
    sources, ops, points = META[gid]
    rels = sorted({int(x['locator'].split()[1]) for x in sources if x['source_id'] == 'src-openhistoricalmap'})
    lic = [l for r in rels for l in licences_segments(r)]
    derive_carte = any(s['source_id'].startswith(('src-loc', 'src-westpoint')) for s in sources)
    feat = {'type': 'Feature', 'geometry': mapping(g), 'properties': {
        'geometry_id': gid, 'date_validite': DATE, 'statut': 'provisoire_carte_georeferencee' if derive_carte else 'provisoire_ohm',
        'sources': sources, 'method': 'carte_georeferencee_puis_intersection' if derive_carte else 'extraction_ohm_puis_decoupage_trait_de_cote',
        'operations': ops,
        'precision': 'voir points_a_verifier' if derive_carte else 'frontières terrestres : celles d’OHM ; côtes : Natural Earth 1:10m (~1 km)',
        'zone_incertitude_km': (5 if 'poches' in gid else 3) if derive_carte else None,
        'surface_km2': round(km2(g)) if not g.geom_type.endswith('LineString') else None,
        'logiciel': 'Python — Shapely/GEOS, scikit-image, SciPy', 'script': 'outils/geo/deriver_snapshot0_lot03.py',
        'date_creation': AUJOURDHUI, 'auteur': 'Claude',
        'licence': 'CC0 (OpenHistoricalMap) + segments sous licence d’origine listés dans licences_segments : à créditer' if lic else 'CC0 (OpenHistoricalMap) ; Natural Earth : domaine public',
        'licences_segments': lic, 'points_a_verifier': points,
    }}
    if gid in TEMPS: feat['properties']['reference_temporelle'] = TEMPS[gid]
    with open(os.path.join(sortie, gid + '.geojson'), 'w', encoding='utf-8') as f:
        json.dump(feat, f, ensure_ascii=False, separators=(',', ':'))
    print(f"{gid:58} {(str(round(km2(g)))+' km²') if not g.geom_type.endswith('LineString') else str(round(g.length,2))+' °':>12}  {g.geom_type}")

# ---------- Contrôles ----------
lu = lambda gid: shape(json.load(open(os.path.join(sortie, gid + '.geojson')))['geometry'])
tops = {k: resultat[f'geom-territoire-{k}-1945-01-01'] for k in ['dk-danemark', 'dk-feroe', 'no-norvege', 'se-suede', 'is-islande', 'gb-royaume-uni', 'je-jersey', 'gg-guernesey', 'ie-irlande', 'fr-france', 'be-belgique', 'lu-luxembourg', 'nl-pays-bas']}
for k in ['de-allemagne', 'fi-finlande', 'su-urss', 'su-petsamo', 'at-autriche']:
    tops[k] = lu(f'geom-territoire-{k}-1945-01-01')
for (a, ga), (b, gb) in itertools.combinations(tops.items(), 2):
    if {a, b} == {'su-urss', 'su-petsamo'}: continue  # Petsamo est un enfant de l'URSS
    o = km2(ga.intersection(gb))
    if o > 1: print(f'CHEVAUCHEMENT {a} / {b} : {o:,.0f} km²')
