"""Encadrement temporel du front de l'Ouest : carte LOC du 31/12/1944 à midi contre celle du 01/01/1945 à midi.
Le Snapshot 0 est à 00:00 le 01/01 : entre les deux. Si les deux lignes concordent, la géométrie est une approximation
solide de minuit ; sinon les secteurs divergents sont signalés.
Usage (depuis outils/geo/lot03) : python comparer_31dec_01jan.py <racine_du_depot>"""
import json, sys, numpy as np, pyproj
from shapely.geometry import Polygon, LineString, Point, box, shape
from shapely.ops import transform, unary_union
EQ = pyproj.Transformer.from_crs(4326, 3035, always_xy=True).transform
QE = pyproj.Transformer.from_crs(3035, 4326, always_xy=True).transform
a = json.load(open('front_loc_12ag_lonlat.json'))['principal']
b = json.load(open('front_loc_12ag_1944-12-31_lonlat.json'))['principal']
lb = transform(EQ, LineString(b))
d = np.array([lb.distance(transform(EQ, Point(p))) for p in a[::5]]) / 1000
print(f'écart 01/01 12h → 31/12 12h : médiane {np.median(d):.1f} km, 90e centile {np.percentile(d, 90):.1f} km')
cote = lambda l: Polygon(l + [(7.60, 47.62), (13, 47.62), (13, 55.5), (2.8, 55.5), (2.8, 51.7), (l[0][0], 51.9)]).buffer(0)
G = lambda k: shape(json.load(open(f'{sys.argv[1]}/data/geometries/snapshot0/geom-territoire-{k}-1945-01-01.geojson'))['geometry'])
terre = unary_union([G(k) for k in ['fr-france', 'be-belgique', 'lu-luxembourg', 'nl-pays-bas', 'de-allemagne']]).intersection(box(4.2, 48.1, 8.5, 52))
diff = transform(EQ, cote(a).symmetric_difference(cote(b)).intersection(terre)).buffer(-1500).buffer(1500)
for p in sorted(getattr(diff, 'geoms', [diff]), key=lambda p: -p.area):
    if p.area < 5e6: continue
    c = transform(QE, p.centroid)
    print(f'{p.area / 1e6:.0f} km² vers {c.x:.2f} E {c.y:.2f} N')
