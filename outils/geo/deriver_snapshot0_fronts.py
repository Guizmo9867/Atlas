"""
Atlas — Snapshot 0 : lignes de front et poches, par géoréférencement de cartes militaires.

1) Front de l'Est au 31/12/1944 (+ poche de Courlande) — carte West Point n° 31,
   « Russian Balkan and Baltic Campaigns, 19 Aug.–31 Dec. 1944 » (Digital History Center, USMA).
   - Géoréférencement : 23 points d'appui (villes) → projection conique conforme de Lambert + affine,
     puis correction « plaque mince » (thin plate spline, comme dans QGIS). Erreur de validation croisée ≈ 9 km en moyenne.
   - Extraction : le trait rouge plein du 31 décembre est isolé par sa couleur et son épaisseur (ouverture morphologique),
     les pointillés (positions antérieures) et les textes sont écartés, puis le trait est réduit à sa ligne centrale.
   - Zone d'incertitude : tampon de 15 km autour de la ligne (carte stylisée + erreur de géoréférencement).
   - Poche de Courlande = partie de la RSS de Lettonie à l'ouest du front de Courlande.
2) Laponie : front de la position « Sturmbock » sur la rivière Lätäseno (tracé de la rivière : OpenHistoricalMap),
   zone tenue par les Allemands = Finlande à l'ouest / au nord-ouest de la rivière.

Usage : python deriver_snapshot0_fronts.py <racine_du_depot> <dossier_cache>
Dépendances : pip install shapely pyproj numpy scipy scikit-image networkx pillow
"""
import json, sys, os, urllib.request
import numpy as np, networkx as nx, pyproj
from PIL import Image
from skimage import morphology, measure
from scipy.interpolate import RBFInterpolator
from shapely.geometry import LineString, MultiLineString, Point, shape, mapping
from shapely.ops import split, unary_union, linemerge, transform as stransform
import ohm_outils as O
from ohm_outils import km2, arrondir, AUJOURDHUI, OVERPASS, licences_segments

RACINE, CACHE = sys.argv[1], sys.argv[2]
os.makedirs(CACHE, exist_ok=True); O.CACHE = CACHE
HERE = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE, 'points_appui_westpoint_map31.py')).read())

URL_CARTE = 'https://dhc.westpoint.edu/wp-content/uploads/sites/6/2025/01/WWIIEurope31.jpg'
carte = os.path.join(CACHE, 'WWIIEurope31.jpg')
if not os.path.exists(carte): urllib.request.urlretrieve(URL_CARTE, carte)
im = np.asarray(Image.open(carte).convert('RGB')).astype(int)

# ---------------------------------------------------------------- 1. géoréférencement
LCC = '+proj=lcc +lat_1=40 +lat_2=60 +lon_0=26 +lat_0=50'
t = pyproj.Transformer.from_crs('EPSG:4326', LCC, always_xy=True); ti = pyproj.Transformer.from_crs(LCC, 'EPSG:4326', always_xy=True)
P = np.array([[g[3], g[4]] for g in G]); X, Y = t.transform([g[1] for g in G], [g[2] for g in G]); XY = np.c_[X, Y]
A = np.c_[P, np.ones(len(P))]; coef = np.linalg.lstsq(A, XY, rcond=None)[0]
tps = RBFInterpolator(P, XY - A @ coef, kernel='thin_plate_spline', smoothing=5.0)
def px2lonlat(pts):
    pts = np.asarray(pts, float); xy = np.c_[pts, np.ones(len(pts))] @ coef + tps(pts)
    lo, la = ti.transform(xy[:, 0], xy[:, 1]); return np.c_[lo, la]
erreurs = []
for i in range(len(P)):
    m = np.ones(len(P), bool); m[i] = False
    c = np.linalg.lstsq(A[m], XY[m], rcond=None)[0]; r = RBFInterpolator(P[m], XY[m] - A[m] @ c, kernel='thin_plate_spline', smoothing=5.0)
    erreurs.append(np.hypot(*((A[i] @ c + r(P[i:i + 1])[0]) - XY[i])) / 1000)
ERR_MOY, ERR_MAX = float(np.mean(erreurs)), float(np.max(erreurs))
print(f'géoréférencement : erreur de validation croisée {ERR_MOY:.1f} km en moyenne, {ERR_MAX:.1f} km au pire')

# ---------------------------------------------------------------- 2. extraction du trait rouge plein
R, Gc, B = im[..., 0], im[..., 1], im[..., 2]
rouge = morphology.opening((R > 190) & (Gc < 90) & (B < 100), morphology.disk(3))
lab = measure.label(rouge, connectivity=2)
def composante_en(x, y):  # l'étiquette de la composante rouge la plus proche d'un point pixel donné
    ys, xs = np.nonzero(lab[y - 40:y + 40, x - 40:x + 40])
    d = (xs - 40) ** 2 + (ys - 40) ** 2; k = d.argmin(); return lab[y - 40 + ys[k], x - 40 + xs[k]]
# Morceaux du trait du 31/12/1944, repérés par un point de passage (pixels) — relevés visuellement sur la carte
MORCEAUX = {
    'courlande': [(1738, 896), (1787, 900), (1909, 881)],
    'memel': [(1749, 962)],
    'principal': [(1822, 1163), (1664, 1773), (1231, 2524)],
    'budapest': [(1373, 2231)],
}
def chemin(mask):
    sk = morphology.skeletonize(mask); ys, xs = np.nonzero(sk); pts = set(zip(ys, xs)); Gr = nx.Graph()
    for (y, x) in pts:
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if (dy or dx) and (y + dy, x + dx) in pts: Gr.add_edge((y, x), (y + dy, x + dx), weight=(dx * dx + dy * dy) ** .5)
    Gr = Gr.subgraph(max(nx.connected_components(Gr), key=len)).copy()
    ends = [n for n in Gr if Gr.degree(n) == 1]
    if len(ends) < 2:
        c = max(nx.cycle_basis(Gr), key=len); c.append(c[0]); return [(x, y) for y, x in c]
    d0 = nx.single_source_dijkstra_path_length(Gr, ends[0]); a = max(ends, key=lambda e: d0.get(e, 0))
    da = nx.single_source_dijkstra_path_length(Gr, a); b = max(ends, key=lambda e: da.get(e, 0))
    return [(x, y) for y, x in nx.dijkstra_path(Gr, a, b)]
def relier(morceaux):
    ligne = list(morceaux[0])
    for k, mcx in enumerate(morceaux[1:]):
        d = lambda p, q: np.hypot(*np.subtract(p, q))
        if k == 0 and min(d(ligne[0], mcx[0]), d(ligne[0], mcx[-1])) < min(d(ligne[-1], mcx[0]), d(ligne[-1], mcx[-1])): ligne = ligne[::-1]
        if d(ligne[-1], mcx[0]) > d(ligne[-1], mcx[-1]): mcx = mcx[::-1]
        ligne += mcx
    return ligne
FRONT = {}
for nom, reperes in MORCEAUX.items():
    ids = list(dict.fromkeys(composante_en(x, y) for x, y in reperes))
    ligne = relier([chemin(lab == i) for i in ids])
    FRONT[nom] = LineString(px2lonlat(ligne[::4] + [ligne[-1]])).simplify(0.005)
    print(f'front {nom:10} {len(ids)} morceau(x), {len(FRONT[nom].coords)} points')

# ---------------------------------------------------------------- 3. géométries
geo = lambda n: shape(json.load(open(os.path.join(RACINE, 'data', 'geometries', 'snapshot0', n + '.geojson')))['geometry'])
def prolonger(l, km=25):
    c = list(l.coords); f = km / 60.0
    def ext(p, q):
        v = np.subtract(p, q); v = v / np.hypot(*v); return tuple(np.add(p, v * f))
    return LineString([ext(c[0], c[1])] + c + [ext(c[-1], c[-2])])
from shapely.geometry import Polygon
lettonie = geo('geom-territoire-su-lettonie-1945-01-01')
# Le front de Courlande longe par endroits la frontière lituanienne : on ne « coupe » pas la Lettonie,
# on garde la partie de la Lettonie située au nord-ouest du front (fermé par la mer).
fc = list(FRONT['courlande'].coords)
if fc[0][0] > fc[-1][0]: fc = fc[::-1]                       # d'ouest (côte) en est (golfe de Riga)
cote_ouest = (fc[0][0] - 1.5, fc[0][1]); golfe = (fc[-1][0], fc[-1][1] + 0.35)
cote_nord = (golfe[0], 58.3); nord_ouest = (cote_ouest[0], 58.3)
courlande = lettonie.intersection(Polygon([cote_ouest] + fc + [golfe, cote_nord, nord_ouest])).buffer(0)
print(f'poche de Courlande : {km2(courlande):,.0f} km²')

# Laponie : la rivière Lätäseno dans OpenHistoricalMap
d = json.load(open(O.telecharger(OVERPASS, 'ohm_latasen.json', '[out:json][timeout:60];way["waterway"]["name"~"Lätäseno"];out geom;')))
riviere = linemerge(MultiLineString([[(p['lon'], p['lat']) for p in e['geometry']] for e in d['elements']]))
if riviere.geom_type == 'MultiLineString': riviere = max(riviere.geoms, key=lambda g: g.length)
finlande = geo('geom-territoire-fi-finlande-1945-01-01')
rc = list(riviere.coords)
if rc[0][1] > rc[-1][1]: rc = rc[::-1]                        # de l'embouchure (sud) vers la source (nord)
laponie = finlande.intersection(Polygon(rc + [(rc[-1][0], 69.8), (19.0, 69.8), (19.0, 68.2), (rc[0][0], 68.2)])).buffer(0)
print(f'zone allemande de Laponie : {km2(laponie):,.0f} km²')

CARTE = {'source_id': 'src-westpoint-russian-balkan-baltic-1944', 'locator': 'carte n° 31, trait rouge plein « 31 Dec. »', 'usage': 'position du front au 31/12/1944'}
def ecrire(gid, g, ops, points, sources, statut='provisoire_carte_georeferencee', incertitude_km=None):
    props = {'geometry_id': gid, 'date_validite': '1945-01-01', 'statut': statut, 'sources': sources,
             'method': 'georeferencement_puis_vectorisation' if statut.endswith('georeferencee') else 'extraction_ohm', 'operations': ops,
             'precision': f'erreur de géoréférencement ≈ {ERR_MOY:.0f} km en moyenne ({ERR_MAX:.0f} km au pire) ; carte stylisée' if statut.endswith('georeferencee') else 'tracé de rivière OHM (~100 m)',
             'logiciel': 'Python — scikit-image, SciPy (thin plate spline), Shapely : mêmes opérations que le géoréférenceur de QGIS',
             'script': 'outils/geo/deriver_snapshot0_fronts.py', 'date_creation': AUJOURDHUI, 'auteur': 'Claude',
             'points_a_verifier': points}
    if not g.geom_type.endswith('LineString'): props['surface_km2'] = round(km2(g))
    if incertitude_km: props['zone_incertitude_km'] = incertitude_km
    with open(os.path.join(RACINE, 'data', 'geometries', 'snapshot0', gid + '.geojson'), 'w', encoding='utf-8') as f:
        json.dump({'type': 'Feature', 'geometry': mapping(arrondir(g, 4)), 'properties': props}, f, ensure_ascii=False, separators=(',', ':'))

ecrire('geom-ligne_front-de-su-est-europe-1945-01-01',
       MultiLineString([FRONT['courlande'], FRONT['memel'], FRONT['principal'], FRONT['budapest']]),
       ['géoréférencement de la carte West Point n° 31 (23 points d’appui, Lambert + plaque mince)', 'extraction du trait rouge plein du 31/12/1944', 'squelettisation, simplification (~500 m)'],
       ['Carte arrêtée au 31/12/1944 : utilisée pour le 01/01/1945 à 0 h. Tout mouvement du 31 décembre dans la journée est invisible.',
        'Quatre morceaux : front de Courlande, tête de pont de Memel, front principal (Prusse-Orientale → Vistule → Carpates → Hongrie → Yougoslavie), anneau de Budapest (encerclée depuis le 26/12/1944).',
        'Carte militaire stylisée : incertitude d’environ 15 km, à croiser avec une carte d’état-major datée (LoC, cartes allemandes Lage Ost) pour les secteurs importants.'],
       [CARTE], incertitude_km=15)
ecrire('geom-territoire-su-courlande-1945-01-01', courlande,
       ['RSS de Lettonie (lot 02)', 'coupée par le front de Courlande géoréférencé (West Point n° 31), côté ouest'],
       ['Limite est de la poche = trait du 31/12/1944 (incertitude ≈ 15 km).'], [CARTE], incertitude_km=15)
ecrire('geom-ligne_front-de-fi-laponie-1945-01-01', riviere,
       ['rivière Lätäseno (OpenHistoricalMap)'],
       ['La position « Sturmbock » suit la Lätäseno ; le tracé exact des lignes allemandes et finlandaises (quelques km de part et d’autre) reste à préciser avec une carte de 1944-1945.'],
       [{'source_id': 'src-openhistoricalmap', 'locator': 'chemins « Lätäseno » (waterway)', 'usage': 'tracé de la rivière'},
        {'source_id': 'src-metsahallitus-schutzwall-2002', 'locator': 'passage sur la position de la Lätäseno (« Sturmbock »)', 'usage': 'la position Sturmbock est sur la Lätäseno'}],
       statut='provisoire_ohm', incertitude_km=5)
ecrire('geom-territoire-fi-laponie-nord-ouest-1945-01-01', laponie,
       ['Finlande (lot 01)', 'coupée par la rivière Lätäseno (OHM), côté nord-ouest (Kilpisjärvi)'],
       ['Zone du « bras » de Finlande (Käsivarsi) au-delà de la Lätäseno, tenue par les Allemands du 29/11/1944 au 27/04/1945.'],
       [{'source_id': 'src-openhistoricalmap', 'locator': 'chemins « Lätäseno » (waterway)', 'usage': 'limite de la zone'},
        {'source_id': 'src-piirainen-lapland-war', 'locator': 'Western Lapland', 'usage': 'arrêt de l’avance finlandaise sur la Lätäseno le 29/11/1944 ; retrait allemand le 27/04/1945'}],
       statut='provisoire_ohm', incertitude_km=5)
print('ok')
