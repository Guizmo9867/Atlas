# Sud de la poche de Colmar au 15/12/1944 : carte West Point n° 70 (trait rouge plein « 8 Nov.-15 Dec. »).
# Recadrage (3250,2250)-(4150,3050) de WWIIEurope70.jpg ; extraction automatique du trait rouge ; calage affine (Lambert) sur 11 villes.
import numpy as np, json, pyproj, networkx as nx
from PIL import Image
from skimage.measure import label
from skimage.morphology import skeletonize
O = (3250, 2250)
im = np.asarray(Image.open('wp70.jpg').convert('RGB')).astype(int)[O[1]:O[1] + 800, O[0]:O[0] + 900]
R, G, B = im[..., 0], im[..., 1], im[..., 2]
lab = label((R > 200) & (G < 80) & (B < 80), connectivity=2)
m = lab == lab[450, 395]                      # composante du trait plein (passe à l'ouest de Colmar)
sk = skeletonize(m); ys, xs = np.nonzero(sk)
idx = {(y, x): n for n, (y, x) in enumerate(zip(ys, xs))}; Gr = nx.Graph()
for (y, x), n in idx.items():
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            j = idx.get((y + dy, x + dx))
            if j is not None and j > n: Gr.add_edge(n, j, weight=(dx * dx + dy * dy) ** .5)
d1 = nx.single_source_dijkstra_path_length(Gr, next(iter(Gr.nodes))); u = max(d1, key=d1.get)
d2, p2 = nx.single_source_dijkstra(Gr, u); v = max(d2, key=d2.get)
path = np.array([(xs[n], ys[n]) for n in p2[v]])
P = pyproj.Proj('+proj=lcc +lat_1=45 +lat_2=55 +lon_0=5 +lat_0=50')
GCP = {'Nancy': ((6.184, 48.692), (133, 30)), 'Luneville': ((6.496, 48.591), (253, 77)), 'St-Die': ((6.949, 48.285), (430, 244)), 'Mirecourt': ((6.134, 48.300), (131, 248)),
       'Epinal': ((6.450, 48.172), (241, 315)), 'Colmar': ((7.358, 48.079), (588, 366)), 'Mulhouse': ((7.338, 47.750), (599, 558)), 'Vesoul': ((6.155, 47.623), (148, 656)),
       'Belfort': ((6.863, 47.638), (407, 659)), 'Bale': ((7.590, 47.559), (708, 658)), 'Strasbourg': ((7.748, 48.583), (722, 68))}
A = np.array([[x, y, 1] for (_, (x, y)) in GCP.values()], float); Bm = np.array([P(*ll) for (ll, _) in GCP.values()])
M, _, _, _ = np.linalg.lstsq(A, Bm, rcond=None); res = np.hypot(*(A @ M - Bm).T) / 1000
q = np.c_[path[::4], np.ones(len(path[::4]))] @ M; lon, lat = P(q[:, 0], q[:, 1], inverse=True)
L = np.stack([lon, lat], 1).round(5)
if L[0][1] < L[-1][1]: L = L[::-1]           # du nord (Strasbourg) vers le sud (Rhin près de Bâle)
json.dump({'front_15dec': L.tolist(), 'residus_km': res.round(2).tolist(), 'moyenne_km': float(res.mean())}, open('alsace_sud_wp70_lonlat.json', 'w'))
