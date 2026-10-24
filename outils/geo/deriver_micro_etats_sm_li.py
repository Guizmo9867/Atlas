"""Tracés des territoires Saint-Marin et Liechtenstein au 01/01/1945 (décision de Guizmo du 24/10/2026, lots 2.SM et 2.LI).
Saint-Marin : on reprend l'anneau du trou que l'Italie du lot 04 laisse déjà (identique à OHM r2853735 à 0,01 km² près),
pour que les deux tracés se touchent exactement. Liechtenstein : OHM r2746467 (1806-07-12 → 1960-03-17), sans chevauchement
avec la Suisse ni l'Autriche du lot 04. Licence : CC0 (OpenHistoricalMap).
Usage : python deriver_micro_etats_sm_li.py <racine du dépôt> (lancé une fois par Claude dans son espace de travail, le 24/10/2026)."""
import json, sys, os
sys.path.insert(0, os.path.join(sys.argv[1], 'outils/geo'))
import ohm_outils as O
from shapely.geometry import shape, mapping, Polygon, Point
O.CACHE = 'cache_geo'; os.makedirs(O.CACHE, exist_ok=True)
it = json.load(open(os.path.join(sys.argv[1], 'data/geometries/snapshot0/geom-territoire-it-italie-1945-01-01.geojson')))['geometry']
polys = [it['coordinates']] if it['type'] == 'Polygon' else it['coordinates']
sm = [Polygon(r) for p in polys for r in p[1:] if Polygon(r).contains(Point(12.457, 43.936))][0]
_, li = O.relation_ohm(2746467)
for nom, g in (('saint-marin', sm), ('liechtenstein', li)):
    print(nom, round(O.km2(g), 1), 'km²', mapping(O.arrondir(g.buffer(0)))['type'])
