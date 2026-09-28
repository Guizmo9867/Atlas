"""
Atlas — outils communs de dérivation des géométries (OpenHistoricalMap + Natural Earth).
Utilisés par les scripts deriver_snapshot0_lot*.py. Voir leurs en-têtes pour la méthode.
"""
import json, sys, os, datetime, urllib.request, urllib.parse
from shapely.geometry import LineString, Polygon, box, shape, mapping, Point
from shapely.ops import polygonize, unary_union, transform
import pyproj

CACHE = 'cache_geo'  # remplacé par le script appelant
DATE = '1945-01-01'
AUJOURDHUI = datetime.date.today().isoformat()
OVERPASS = 'https://overpass-api.openhistoricalmap.org/api/interpreter'
EQ = pyproj.Transformer.from_crs(4326, 6933, always_xy=True).transform  # aire égale, pour les km²
km2 = lambda g: transform(EQ, g).area / 1e6

def telecharger(url, fichier, data=None):
    chemin = os.path.join(CACHE, fichier)
    if not os.path.exists(chemin):
        req = urllib.request.Request(url, data=urllib.parse.urlencode({'data': data}).encode() if data else None)
        with urllib.request.urlopen(req, timeout=600) as r, open(chemin, 'wb') as f: f.write(r.read())
    return chemin

def relation_ohm(rid):
    """Reconstruit le polygone d'une relation OHM à partir de ses chemins (rôle outer/inner)."""
    d = json.load(open(telecharger(OVERPASS, f'ohm_{rid}.json', f'[out:json][timeout:300];relation({rid});out geom;')))
    r = d['elements'][0]
    ext, inte = [], []
    for m in r['members']:
        if m['type'] == 'way' and 'geometry' in m:
            (inte if m.get('role') == 'inner' else ext).append(LineString([(p['lon'], p['lat']) for p in m['geometry']]))
    res = None
    for p in polygonize(unary_union(ext)):          # parité : un anneau à l'intérieur d'un autre = trou
        res = p if res is None else res.symmetric_difference(p)
    if inte: res = res.difference(unary_union(list(polygonize(unary_union(inte)))))
    return r['tags'], res.buffer(0)

def licences_segments(rid):
    """OHM est en CC0, MAIS certains segments importés gardent leur licence d'origine (tag license / source:license).
    On les liste pour pouvoir créditer correctement (ex. Kartverket CC BY 4.0, OCHA CC BY-IGO)."""
    d = json.load(open(telecharger(OVERPASS, f'wt_{rid}.json', f'[out:json][timeout:200];relation({rid});way(r);out tags;')))
    compte = {}
    for w in d['elements']:
        t = w.get('tags', {})
        lic = t.get('license') or t.get('source:license')
        if lic:
            cle = (lic, (t.get('source') or '').strip())
            compte[cle] = compte.get(cle, 0) + 1
    return [{'relation': rid, 'licence': l, 'source': src, 'segments': n} for (l, src), n in compte.items()]

_TERRES = None

def terres(zone):
    """Terres Natural Earth 10m (+ petites îles) qui touchent la zone."""
    global _TERRES
    if _TERRES is None:
        _TERRES = []
        for f in ('ne_10m_land', 'ne_10m_minor_islands'):
            chemin = telecharger(f'https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/{f}.geojson', f + '.geojson')
            _TERRES += [shape(x['geometry']).buffer(0) for x in json.load(open(chemin))['features']]
    feats = _TERRES
    b = zone.bounds
    return unary_union([g for g in feats if g.intersects(box(*b))])

def arrondir(g, n=5):
    return transform(lambda x, y, z=None: (round(x, n), round(y, n)), g)

