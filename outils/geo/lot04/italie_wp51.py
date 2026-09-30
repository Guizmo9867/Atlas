"""Front d'Italie au 31/12/1944 : carte West Point n° 51 « Allied Offensives in Italy, 5 June-31 December 1944 ».
Ligne = tireté rouge « 31 Dec. » (Apennins, de la côte tyrrhénienne à l'Adriatique au nord de Ravenne), prolongé à
l'ouest par le trait plein resté inchangé jusqu'à la côte. Points relevés à la main sur l'image (5100×3300 px).
Calage : 26 villes, transformation affine (Lambert) + plaque mince lissée (carte stylisée, villes parfois déplacées).
Usage : python italie_wp51.py  (écrit front_italie_31dec_lonlat.json)"""
import json, numpy as np, pyproj
from scipy.interpolate import RBFInterpolator
LCC = '+proj=lcc +lat_1=40 +lat_2=47 +lon_0=11 +lat_0=44'
t = pyproj.Transformer.from_crs('EPSG:4326', LCC, always_xy=True); ti = pyproj.Transformer.from_crs(LCC, 'EPSG:4326', always_xy=True)
G = {'Bologna': ((11.343, 44.494), (2145, 1835)), 'Faenza': ((11.883, 44.286), (2435, 2000)), 'Ravenna': ((12.199, 44.418), (2515, 1890)), 'Florence': ((11.256, 43.770), (2095, 2238)),
     'Milan': ((9.19, 45.464), (1232, 1220)), 'Verona': ((10.992, 45.438), (2012, 1264)), 'Padua': ((11.877, 45.407), (2376, 1296)), 'Treviso': ((12.245, 45.667), (2532, 1108)),
     'Udine': ((13.235, 46.063), (2964, 876)), 'Trieste': ((13.777, 45.650), (3188, 1136)), 'Genoa': ((8.934, 44.407), (1108, 1844)), 'Savona': ((8.481, 44.309), (892, 1912)),
     'Spezia': ((9.824, 44.107), (1480, 2064)), 'Pisa': ((10.402, 43.716), (1720, 2288)), 'Leghorn': ((10.310, 43.548), (1684, 2404)), 'Siena': ((11.331, 43.318), (2100, 2536)),
     'Arezzo': ((11.880, 43.463), (2392, 2396)), 'Rimini': ((12.568, 44.059), (2640, 2096)), 'Ancona': ((13.519, 43.616), (3072, 2372)), 'Ferrara': ((11.619, 44.838), (2264, 1620)),
     'Modena': ((10.926, 44.647), (1956, 1748)), 'Parma': ((10.328, 44.801), (1736, 1664)), 'Piacenza': ((9.693, 45.052), (1452, 1476)), 'Bolzano': ((11.354, 46.498), (2148, 640)),
     'Ljubljana': ((14.506, 46.056), (3588, 880)), 'Grosseto': ((11.114, 42.760), (1988, 2800))}
P = np.array([px for (_, px) in G.values()], float)
X, Y = t.transform([ll[0] for (ll, _) in G.values()], [ll[1] for (ll, _) in G.values()]); XY = np.c_[X, Y]
A = np.c_[P, np.ones(len(P))]; coef = np.linalg.lstsq(A, XY, rcond=None)[0]
tps = RBFInterpolator(P, XY - A @ coef, kernel='thin_plate_spline', smoothing=50.0)
def px2ll(pts):
    pts = np.asarray(pts, float); xy = np.c_[pts, np.ones(len(pts))] @ coef + tps(pts)
    lo, la = ti.transform(xy[:, 0], xy[:, 1]); return np.c_[lo, la]
err = []
for i in range(len(P)):
    m = np.ones(len(P), bool); m[i] = False
    c = np.linalg.lstsq(A[m], XY[m], rcond=None)[0]; r = RBFInterpolator(P[m], XY[m] - A[m] @ c, kernel='thin_plate_spline', smoothing=50.0)
    err.append(np.hypot(*((A[i] @ c + r(P[i:i + 1])[0]) - XY[i])) / 1000)
print(f'validation croisée : {np.mean(err):.1f} km en moyenne, {np.max(err):.1f} km au pire')
# Ligne du 31/12/1944, d'ouest (côte tyrrhénienne) en est (côte adriatique)
LIGNE = [(1640, 2182), (1700, 2155), (1760, 2128), (1790, 2122), (1830, 2112), (1870, 2096), (1910, 2078), (1940, 2060), (1985, 2030), (2010, 2008),
         (2040, 1982), (2080, 1965), (2110, 1950), (2160, 1945), (2190, 1960), (2240, 1995), (2260, 2015), (2290, 2060), (2310, 2074), (2330, 2078),
         (2345, 2060), (2365, 2040), (2380, 1975), (2410, 1930), (2430, 1890), (2450, 1860), (2470, 1835), (2500, 1820), (2525, 1820), (2560, 1822), (2575, 1822)]
ll = px2ll(LIGNE).round(5).tolist()
json.dump({'front_31dec': ll, 'validation_croisee_km': {'moyenne': round(float(np.mean(err)), 1), 'max': round(float(np.max(err)), 1)}},
          open('front_italie_31dec_lonlat.json', 'w'))
print(ll[0], ll[-1])
