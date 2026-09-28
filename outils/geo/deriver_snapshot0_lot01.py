"""
Atlas — dérivation des géométries du Snapshot 0 (1945-01-01), lot 01 Nord/Est.

Trace d'audit : ce script refait EXACTEMENT les opérations qui ont produit les fichiers
data/geometries/snapshot0/*.geojson. Un historien peut le relire, le relancer, le contester.

Sources :
  - OpenHistoricalMap (OHM, CC0) : relations administratives datées, extraites via Overpass.
    Référence de COMPARAISON selon le récap technique, jamais base de vérité → géométries « provisoires ».
  - Natural Earth 1:10m (domaine public) : trait de côte, pour ne garder que les terres
    (OHM inclut les eaux territoriales).
  - CShapes 2.0 (ETH Zurich, CC BY-NC-SA 4.0) : UNIQUEMENT pour comparer (licence non commerciale :
    on ne redistribue pas ses tracés).

Dépendances : pip install shapely pyproj geopandas requests
Usage : python deriver_snapshot0_lot01.py <racine_du_depot> <dossier_cache>
"""
import json, sys, os
from shapely.geometry import box, mapping, Point
from shapely.ops import unary_union
import ohm_outils as O
from ohm_outils import *

RACINE, CACHE = sys.argv[1], sys.argv[2]
os.makedirs(CACHE, exist_ok=True)
O.CACHE = CACHE

# ---------------------------------------------------------------- 1. Extraction OHM
REL = {
    'urss': 2957472,       # Soviet Union, 1944-10-11 → 1945-08-01
    'fi_1944': 2855285,    # Finland, 1944-09-19 → 1947-04-18
    'fi_1940': 2692833,    # Finland, 1940-03-12 → 1944-09-19 (sert à isoler Petsamo et Porkkala)
    'kazakh': 2697958,     # Kazakh SSR, 1936-12-05 → 1991-12-26
    'touva': 2958149,      # Tuvan Autonomous Oblast, 1944-10-11 → 1961-10-10
    'mongolie': 2942671,   # Mongolian People's Republic, 1924-11-26 → 1992-02-12
}
BRUT = {k: relation_ohm(v) for k, v in REL.items()}
G = {k: v[1] for k, v in BRUT.items()}

# ---------------------------------------------------------------- 2. Opérations
perdu_1944 = G['fi_1940'].difference(G['fi_1944'])                      # ce que la Finlande perd à l'armistice
porkkala_brut = perdu_1944.intersection(box(23.5, 59.5, 25.5, 60.6))    # la partie sud = zone de Porkkala
petsamo_brut = perdu_1944.intersection(box(26.0, 67.5, 34.0, 71.5))     # la partie nord = Petsamo

# Décision du lot 02 (Ether, 28/09/2026) : la frontière soviéto-polonaise du Snapshot 0 suit l'accord URSS–PKWN
# du 27/07/1944 (Białystok, Łomża, Przemyśl côté polonais). OHM place l'URSS sur la ligne de 1941 : on retire
# donc de l'URSS le territoire de la Pologne du Snapshot 0 (même calcul que dans deriver_snapshot0_lot02.py).
POLOGNE_S0 = relation_ohm(2692205)[1].intersection(relation_ohm(2692206)[1])

MONDE = unary_union([G['urss'], G['fi_1940'], G['mongolie']])
TERRES = terres(MONDE)

resultat = {
    'geom-territoire-su-urss-1945-01-01': G['urss'].difference(porkkala_brut).difference(POLOGNE_S0).intersection(TERRES),
    'geom-territoire-su-kazakhstan-1945-01-01': G['kazakh'].intersection(TERRES),
    'geom-territoire-su-touva-1945-01-01': G['touva'].intersection(TERRES),
    'geom-territoire-mn-mongolie-1945-01-01': G['mongolie'].intersection(TERRES),
    'geom-territoire-fi-finlande-1945-01-01': G['fi_1944'].union(porkkala_brut).intersection(TERRES),
    'geom-territoire-su-petsamo-1945-01-01': petsamo_brut.intersection(TERRES),
    'geom-territoire-fi-porkkala-1945-01-01': porkkala_brut.intersection(TERRES),
}
resultat = {k: arrondir(v.buffer(0)) for k, v in resultat.items()}

# ---------------------------------------------------------------- 3. Métadonnées de dérivation (protocole des sources)
def ohm(rid, quoi): return {'source_id': 'src-openhistoricalmap', 'locator': f'relation {rid} — {quoi}', 'usage': 'tracé de la frontière'}
NE = {'source_id': 'src-natural-earth-10m', 'locator': 'ne_10m_land + ne_10m_minor_islands', 'usage': 'trait de côte (on retire les eaux territoriales incluses par OHM)'}
META = {
    'geom-territoire-su-urss-1945-01-01': ([ohm(2957472, 'Soviet Union 1944-10-11 → 1945-08-01'), NE],
        ['OHM r2957472', 'moins la zone de Porkkala (souveraineté finlandaise : OHM la compte comme soviétique)', 'moins la Pologne du Snapshot 0 (ligne de l’accord URSS–PKWN du 27/07/1944 au lieu de la ligne de 1941 d’OHM ; décision du lot 02)', '∩ terres Natural Earth']),
    'geom-territoire-su-kazakhstan-1945-01-01': ([ohm(2697958, 'Kazakh SSR 1936-12-05 → 1991-12-26'), NE], ['OHM r2697958', '∩ terres Natural Earth']),
    'geom-territoire-su-touva-1945-01-01': ([ohm(2958149, 'Tuvan Autonomous Oblast 1944-10-11 → 1961-10-10'), NE], ['OHM r2958149', '∩ terres Natural Earth']),
    'geom-territoire-mn-mongolie-1945-01-01': ([ohm(2942671, "Mongolian People's Republic 1924-11-26 → 1992-02-12"), NE], ['OHM r2942671', '∩ terres Natural Earth']),
    'geom-territoire-fi-finlande-1945-01-01': ([ohm(2855285, 'Finland 1944-09-19 → 1947-04-18'), ohm(2692833, 'Finland 1940-03-12 → 1944-09-19'), NE],
        ['OHM r2855285', "∪ zone de Porkkala (souveraineté finlandaise, voir territoire-fi-porkkala)", '∩ terres Natural Earth']),
    'geom-territoire-su-petsamo-1945-01-01': ([ohm(2692833, 'Finland 1940-03-12 → 1944-09-19'), ohm(2855285, 'Finland 1944-09-19 → 1947-04-18'), NE],
        ['OHM r2692833 moins OHM r2855285 (territoire perdu par la Finlande à l’armistice)', 'partie nord (67,5°N–71,5°N)', '∩ terres Natural Earth']),
    'geom-territoire-fi-porkkala-1945-01-01': ([ohm(2692833, 'Finland 1940-03-12 → 1944-09-19'), ohm(2855285, 'Finland 1944-09-19 → 1947-04-18'), NE],
        ['OHM r2692833 moins OHM r2855285', 'partie sud (59,5°N–60,6°N ; 23,5°E–25,5°E)', '∩ terres Natural Earth']),
}
# Points à vérifier : écarts repérés en comparant OHM, CShapes 2.0 et l'histoire connue (à sourcer par Ether)
A_VERIFIER = {
    'geom-territoire-su-urss-1945-01-01': [
        "TRANCHÉ (lot 02) : frontière soviéto-polonaise = accord URSS–PKWN du 27/07/1944 ; Białystok, Łomża et Przemyśl sont retirés de l'URSS. Le tracé exact de cette ligne reprend celui du traité du 16/08/1945 (OHM, Pologne 1945-1948) : écarts locaux possibles avec la ligne de juillet 1944, à vérifier.",
        "CShapes 2.0 garde la frontière polonaise d'avant-guerre jusqu'au 07/05/1945 : lecture « reconnaissance internationale », non retenue comme géométrie mais à rappeler dans les fiches.",
        "États baltes inclus (annexion de 1940, non reconnue par les États-Unis et le Royaume-Uni) : à noter dans souverainete_id/note. La poche de Courlande, tenue par l'armée allemande au 01/01/1945, relève de la couche contrôle/ligne de front.",
        "Exclus à juste titre au 01/01/1945 : Königsberg, Memel/Klaipėda, Ruthénie subcarpatique (traité du 29/06/1945), Sakhaline du Sud et Kouriles (août-septembre 1945).",
        "Côtes : Natural Earth 1:10m (précision ~1 km) ; eaux territoriales retirées.",
    ],
    'geom-territoire-su-kazakhstan-1945-01-01': [
        "OHM reprend la frontière moderne du Kazakhstan. Or le district de Bostanliq (Bo'stonliq, vers 70°E 41,6°N) appartenait à la RSS kazakhe en 1945 et n'a été transféré à la RSS ouzbèke qu'en 1956 : il manque probablement ici. À sourcer puis corriger.",
        "Autres ajustements RSS kazakhe / RSS ouzbèke / RSFSR entre 1945 et 1991 à vérifier.",
    ],
    'geom-territoire-su-touva-1945-01-01': [
        "OHM s'appuie sur les limites administratives modernes (Rosreestr). À comparer avec une carte de 1944-1945 (frontière Touva–Mongolie notamment).",
    ],
    'geom-territoire-mn-mongolie-1945-01-01': [
        "Géométrie = territoire effectivement administré par Oulan-Bator au 01/01/1945 (≈ Mongolie actuelle) : Touva exclue (soviétique), Mongolie intérieure exclue (côté chinois), Hulunbuir/Mandchourie exclus (Mandchoukouo). Décision Ether/Guizmo du 28/09/2026.",
        "Frontière sino-mongole historiquement imparfaitement délimitée (délimitation seulement en 1962) : OHM utilise le tracé moderne (LSIB). CShapes 2.0 donne ≈ 5 800 km² de plus à la Mongolie vers 116,6°E 47,7°N (secteur de Khalkhin Gol / Nomonhan) et deux zones d'environ 1 100 km². À signaler comme incertaine tant qu'une carte des années 1940 ne permet pas mieux.",
    ],
    'geom-territoire-fi-finlande-1945-01-01': [
        "Inclut la zone de Porkkala (souveraineté finlandaise). Les transferts de Janiskoski et Niskakoski (1947) sont postérieurs : bien absents ici.",
        "Archipels : le trait de côte Natural Earth 1:10m simplifie les îles (Åland, archipel de Turku).",
    ],
    'geom-territoire-su-petsamo-1945-01-01': [
        "Surface obtenue : ≈ 11 200 km² de terres. À comparer avec la surface historique de la province de Petsamo cédée en 1944 (chiffre à sourcer).",
    ],
    'geom-territoire-fi-porkkala-1945-01-01': [
        "Seules les terres sont gardées (≈ 200 km²), avec une côte Natural Earth grossière dans l'archipel. Le bail couvrait aussi des eaux (≈ 1 000 km² au total selon les sources secondaires) : à reprendre avec une carte du bail si l'on crée une couche maritime.",
    ],
}

sortie = os.path.join(RACINE, 'data', 'geometries', 'snapshot0')
os.makedirs(sortie, exist_ok=True)
for gid, g in resultat.items():
    sources, ops = META[gid]
    rels = sorted({int(x['locator'].split()[1]) for x in sources if x['source_id'] == 'src-openhistoricalmap'})
    lic = [l for r in rels for l in licences_segments(r)]
    feat = {'type': 'Feature', 'geometry': mapping(g), 'properties': {
        'geometry_id': gid, 'date_validite': DATE, 'statut': 'provisoire_ohm',
        'sources': sources, 'method': 'extraction_ohm_puis_decoupage_trait_de_cote', 'operations': ops,
        'precision': 'frontières terrestres : celles d’OHM (souvent reprises de tracés officiels modernes, LSIB) ; côtes : Natural Earth 1:10m (~1 km)',
        'surface_km2': round(km2(g)), 'logiciel': 'Python — Shapely/GEOS (mêmes opérations que les outils de géotraitement QGIS)',
        'script': 'outils/geo/deriver_snapshot0_lot01.py', 'date_creation': AUJOURDHUI, 'auteur': 'Claude',
        'licence': 'CC0 (OpenHistoricalMap) + segments sous licence d’origine listés dans licences_segments : à créditer (voir docs/LICENCES_ET_ATTRIBUTIONS.md)' if lic else 'CC0 (OpenHistoricalMap) ; Natural Earth : domaine public',
        'licences_segments': lic,
        'comparaison': {'source_id': 'src-cshapes-2-0', 'usage': 'contrôle des écarts uniquement (licence non commerciale, tracés non redistribués)'},
        'points_a_verifier': A_VERIFIER[gid],
    }}
    with open(os.path.join(sortie, gid + '.geojson'), 'w', encoding='utf-8') as f:
        json.dump(feat, f, ensure_ascii=False, separators=(',', ':'))
    print(f'{gid:45} {km2(g):>12,.0f} km²  {g.geom_type}')

# ---------------------------------------------------------------- 4. Contrôles de cohérence (enfant ⊂ parent)
for enfant, parent in [('su-kazakhstan', 'su-urss'), ('su-touva', 'su-urss'), ('su-petsamo', 'su-urss'), ('fi-porkkala', 'fi-finlande')]:
    e, p = resultat[f'geom-territoire-{enfant}-1945-01-01'], resultat[f'geom-territoire-{parent}-1945-01-01']
    print(f'contrôle {enfant} ⊂ {parent} : {km2(e.difference(p)):,.1f} km² dépassent')
