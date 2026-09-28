"""
Atlas — dérivation des géométries du Snapshot 0 (1945-01-01), lot 02 : Pologne, Allemagne, Autriche, pays baltes.

Même méthode que le lot 01 (voir deriver_snapshot0_lot01.py) : relations datées d'OpenHistoricalMap,
découpées au trait de côte Natural Earth 1:10m. Les choix historiques viennent du lot 02 d'Ether :
  - Allemagne = frontières du 31/12/1937 (référence du protocole allié de 1944), annexions de guerre séparées ;
  - Autriche = frontières de 1937 (annexion de 1938 tenue pour nulle par les Alliés) ;
  - Pologne = frontière occidentale d'avant-guerre (pré-Munich) + frontière orientale de l'accord URSS–PKWN
    du 27/07/1944 (Białystok côté polonais). Tracé oriental repris du traité du 16/08/1945 (OHM Pologne 1945-1948),
    faute de carte vectorisée de l'accord de juillet 1944 ;
  - RSS d'Estonie et de Lettonie APRÈS les transferts de 1944 vers la RSFSR (Petseri/Pechory, rive est de la Narva, Abrene) ;
  - RSS de Lituanie SANS Memel/Klaipėda (allemand jusqu'au 28/01/1945) ;
  - Memel = Lituanie de 1923-1939 moins Lituanie après mars 1939 ;
  - Dantzig = Ville libre de Dantzig (1920-1939).
Pas encore tracés (carte militaire à géoréférencer) : poche de Courlande, ligne de front.

Usage : python deriver_snapshot0_lot02.py <racine_du_depot> <dossier_cache>
"""
import json, sys, os
from shapely.geometry import box, mapping, Point
from shapely.ops import unary_union, linemerge
import ohm_outils as O
from ohm_outils import *

RACINE, CACHE = sys.argv[1], sys.argv[2]
os.makedirs(CACHE, exist_ok=True)
O.CACHE = CACHE

REL = {
    'allemagne_1937': 2693085,  # German Reich, 1936-07-03 → 1938-03-13
    'autriche_1937': 2858751,   # Austria, 1922-10-01 → 1938-03-13
    'pologne_1938': 2692205,    # Poland, 1924-06-22 → 1938-11-01 (avant Munich)
    'pologne_1945': 2692206,    # Poland, 1945-08 → 1948 (sert pour la frontière orientale)
    'dantzig': 2691478,         # Free City of Danzig, 1920-12-24 → 1939-09-01
    'lituanie_1923': 2692218,   # Lithuania, 1923-01-19 → 1939-03-23 (avec Memel)
    'lituanie_1939': 2855606,   # Lithuania, 1939-03-23 → 1939-10-28 (sans Memel)
    'lituanie_rss': 2855607,    # Lithuanian SSR, 1940-08-05 → 1945-01-28 (sans Klaipėda)
    'lettonie_rss': 2959347,    # Latvian SSR, 1945-01-16 → (après transfert d'Abrene)
    'estonie_rss': 2959351,     # Estonia SSR, 1945-01 → (après transferts Petseri / Narva)
    'urss': 2957472,            # Soviet Union, 1944-10-11 → 1945-08-01
}
G = {k: relation_ohm(v)[1] for k, v in REL.items()}

pologne = G['pologne_1938'].intersection(G['pologne_1945'])
urss = G['urss'].difference(pologne)
memel = G['lituanie_1923'].difference(G['lituanie_1939'])
MONDE = unary_union(list(G.values()))
TERRES = terres(MONDE)

# Frontière Pologne–URSS : la limite commune des deux territoires
ligne = pologne.boundary.intersection(urss.buffer(0.0005))
ligne = linemerge(ligne) if ligne.geom_type == 'MultiLineString' else ligne

resultat = {
    'geom-territoire-de-allemagne-1945-01-01': G['allemagne_1937'].intersection(TERRES),
    'geom-territoire-at-autriche-1945-01-01': G['autriche_1937'].intersection(TERRES),
    'geom-territoire-pl-pologne-1945-01-01': pologne.intersection(TERRES),
    'geom-frontiere-pl-su-est-1945-01-01': ligne,
    'geom-territoire-su-estonie-1945-01-01': G['estonie_rss'].intersection(TERRES),
    'geom-territoire-su-lettonie-1945-01-01': G['lettonie_rss'].intersection(TERRES),
    'geom-territoire-su-lituanie-1945-01-01': G['lituanie_rss'].intersection(TERRES),
    'geom-territoire-de-memel-1945-01-01': memel.intersection(TERRES),
    'geom-territoire-de-dantzig-1945-01-01': G['dantzig'].intersection(TERRES),
}
resultat = {k: arrondir(v if v.geom_type.endswith('LineString') else v.buffer(0)) for k, v in resultat.items()}

def ohm(cle, quoi): return {'source_id': 'src-openhistoricalmap', 'locator': f'relation {REL[cle]} — {quoi}', 'usage': 'tracé de la frontière'}
NE = {'source_id': 'src-natural-earth-10m', 'locator': 'ne_10m_land + ne_10m_minor_islands', 'usage': 'trait de côte (on retire les eaux territoriales incluses par OHM)'}
META = {
    'geom-territoire-de-allemagne-1945-01-01': ([ohm('allemagne_1937', 'German Reich 1936-07-03 → 1938-03-13'), NE],
        ['OHM r2693085 (frontières du 31/12/1937)', '∩ terres Natural Earth'],
        ["Frontières du 31/12/1937, référence alliée : ce n'est PAS l'étendue du Reich au 01/01/1945 (annexions et territoires administrés représentés séparément).",
         "Le contrôle réel au 01/01/1945 diverge localement (Aix-la-Chapelle aux mains des Américains depuis octobre 1944, secteur de Goldap/Gumbinnen en Prusse-Orientale) : relève de la couche front / contrôle."]),
    'geom-territoire-at-autriche-1945-01-01': ([ohm('autriche_1937', 'Austria 1922-10-01 → 1938-03-13'), NE],
        ['OHM r2858751 (frontières de 1937)', '∩ terres Natural Earth'],
        ["Frontières autrichiennes de 1937. Le transfert d'environ 316 km² du Vorarlberg vers la Bavière après l'Anschluss (FRUS 1943, doc. 366) n'est volontairement PAS appliqué : l'Autriche est tracée selon la lecture alliée (annexion nulle)."]),
    'geom-territoire-pl-pologne-1945-01-01': ([ohm('pologne_1938', 'Poland 1924-06-22 → 1938-11-01'), ohm('pologne_1945', 'Poland 1945-08 → 1948'), NE],
        ['OHM r2692205 (Pologne d’avant Munich) ∩ OHM r2692206 (Pologne de 1945-1948)', '= frontière ouest d’avant-guerre + frontière est de 1945', '∩ terres Natural Earth'],
        ["Frontière orientale : celle du traité soviéto-polonais du 16/08/1945 (seul tracé vectorisé disponible), utilisée comme approximation de la ligne de l'accord URSS–PKWN du 27/07/1944. Écarts locaux possibles, à vérifier sur une carte de l'accord.",
         "Secteur de Białystok : côté polonais (décision du lot 02), mais statut administratif encore ambigu dans certaines sources soviétiques (Université de Białystok).",
         "Zaolzie (Teschen) hors de la Pologne : au 01/01/1945 la question polono-tchécoslovaque est contestée et la zone est sous contrôle allemand ; le mémorandum américain du 11/01/1945 (FRUS 1945 vol. IV doc. 432) préconise la frontière d'avant 1938. À traiter avec la Tchécoslovaquie.",
         "Contrôle militaire morcelé (front de la Vistule) : à représenter par la ligne de front, pas par cette géométrie."]),
    'geom-frontiere-pl-su-est-1945-01-01': ([ohm('pologne_1938', 'Poland 1924-06-22 → 1938-11-01'), ohm('pologne_1945', 'Poland 1945-08 → 1948'), ohm('urss', 'Soviet Union 1944-10-11 → 1945-08-01')],
        ['limite commune entre la Pologne du Snapshot 0 et l’URSS corrigée'],
        ["Même réserve que pour la Pologne : tracé du traité du 16/08/1945 utilisé comme approximation de la ligne du 27/07/1944."]),
    'geom-territoire-su-estonie-1945-01-01': ([ohm('estonie_rss', 'Estonia SSR 1945-01 →'), NE],
        ['OHM r2959351 (après transferts vers la RSFSR)', '∩ terres Natural Earth'],
        ["Transferts appliqués : Petserimaa (août 1944) et rive est de la Narva (24/11/1944) — TRAMES 2025. Transfert soviétique effectif, formalisation incomplète : acceptation par la RSS d'Estonie le 18/01/1945 → nouvel état juridique à cette date, sans changement de tracé. (OHM date le changement de janvier 1945.)"]),
    'geom-territoire-su-lettonie-1945-01-01': ([ohm('lettonie_rss', 'Latvian SSR 1945-01-16 →'), NE],
        ['OHM r2959347 (après transfert d’Abrene)', '∩ terres Natural Earth'],
        ["Transfert d'Abrene/Pytalovo appliqué (1944 selon le lot 02 ; OHM : 16/01/1945 ; Wikipédia : 1944, formalisé en 1946).",
         "La poche de Courlande (contrôle allemand) n'est pas découpée ici : elle sera une sous-zone séparée, tracée depuis la carte de West Point (map 31)."]),
    'geom-territoire-su-lituanie-1945-01-01': ([ohm('lituanie_rss', 'Lithuanian SSR 1940-08-05 → 1945-01-28'), NE],
        ['OHM r2855607 (sans Klaipėda)', '∩ terres Natural Earth'],
        ["Memel/Klaipėda exclu (allemand jusqu'au 28/01/1945, date à reprendre lors du ratissage de janvier)."]),
    'geom-territoire-de-memel-1945-01-01': ([ohm('lituanie_1923', 'Lithuania 1923-01-19 → 1939-03-23'), ohm('lituanie_1939', 'Lithuania 1939-03-23 → 1939-10-28'), NE],
        ['OHM r2692218 moins OHM r2855606 (ce que la Lituanie perd le 23/03/1939)', '∩ terres Natural Earth'],
        ["Surface à vérifier : 2 657 km² (définition courante de la région de Klaipėda) contre 2 828 km² (Columbia Encyclopedia) ; tracé ≈ 2 500 km² de terres. Écart probablement dû à la côte et à la lagune : on ne retouche pas le polygone pour atteindre un chiffre."]),
    'geom-territoire-de-dantzig-1945-01-01': ([ohm('dantzig', 'Free City of Danzig 1920-12-24 → 1939-09-01'), NE],
        ['OHM r2691478 (Ville libre de Dantzig)', '∩ terres Natural Earth'],
        ["Limites de la Ville libre ; après l'annexion de 1939, la ville est intégrée au Reichsgau Danzig-Westpreußen, dont les limites ne sont pas reprises ici (choix du lot 02)."]),
}
sortie = os.path.join(RACINE, 'data', 'geometries', 'snapshot0')
os.makedirs(sortie, exist_ok=True)
for gid, g in resultat.items():
    sources, ops, points = META[gid]
    rels = sorted({int(x['locator'].split()[1]) for x in sources if x['source_id'] == 'src-openhistoricalmap'})
    lic = [l for r in rels for l in licences_segments(r)]
    feat = {'type': 'Feature', 'geometry': mapping(g), 'properties': {
        'geometry_id': gid, 'date_validite': DATE, 'statut': 'provisoire_ohm',
        'sources': sources, 'method': 'extraction_ohm_puis_decoupage_trait_de_cote', 'operations': ops,
        'precision': 'frontières terrestres : celles d’OHM (souvent reprises de tracés officiels) ; côtes : Natural Earth 1:10m (~1 km)',
        'surface_km2': round(km2(g)) if not g.geom_type.endswith('LineString') else None,
        'logiciel': 'Python — Shapely/GEOS (mêmes opérations que les outils de géotraitement QGIS)',
        'script': 'outils/geo/deriver_snapshot0_lot02.py', 'date_creation': AUJOURDHUI, 'auteur': 'Claude',
        'licence': 'CC0 (OpenHistoricalMap) + segments sous licence d’origine listés dans licences_segments : à créditer' if lic else 'CC0 (OpenHistoricalMap) ; Natural Earth : domaine public',
        'licences_segments': lic,
        'points_a_verifier': points,
    }}
    with open(os.path.join(sortie, gid + '.geojson'), 'w', encoding='utf-8') as f:
        json.dump(feat, f, ensure_ascii=False, separators=(',', ':'))
    print(f"{gid:48} {(str(round(km2(g)))+' km²') if not g.geom_type.endswith('LineString') else str(round(g.length,2))+' ° de ligne':>14}  {g.geom_type}")

# Contrôles : pas de chevauchement entre territoires de premier niveau, enfants dans leur parent
urss_s0 = json.load(open(os.path.join(sortie, 'geom-territoire-su-urss-1945-01-01.geojson')))
from shapely.geometry import shape
U = shape(urss_s0['geometry'])
tops = {k: resultat[f'geom-territoire-{k}-1945-01-01'] for k in ['de-allemagne', 'at-autriche', 'pl-pologne', 'de-memel', 'de-dantzig']}
tops['su-urss'] = U
import itertools
for (a, ga), (b, gb) in itertools.combinations(tops.items(), 2):
    o = km2(ga.intersection(gb))
    if o > 1: print(f'CHEVAUCHEMENT {a} / {b} : {o:,.0f} km²')
for k in ['su-estonie', 'su-lettonie', 'su-lituanie']:
    print(f"contrôle {k} ⊂ su-urss : {km2(resultat[f'geom-territoire-{k}-1945-01-01'].difference(U)):,.1f} km² dépassent")
