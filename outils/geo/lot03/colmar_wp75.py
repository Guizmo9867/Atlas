# Sud de la poche de Colmar : carte West Point 75a (tireté rouge « 20 Jan. »).
# Calage affine (Lambert) sur 13 villes lues sur la carte ; points de la ligne relevés à la main sur le recadrage (700,1700)-(2200,2900).
import numpy as np, json, pyproj
P=pyproj.Proj('+proj=lcc +lat_1=45 +lat_2=55 +lon_0=5 +lat_0=50')
O=(700,1700)
G={'Colmar':((7.358,48.079),(969,483)),'Neuf-Brisach':((7.528,48.018),(1100,551)),'Breisach':((7.580,48.030),(1151,531)),'Rouffach':((7.300,47.958),(934,600)),
'Guebwiller':((7.211,47.910),(821,639)),'Cernay':((7.177,47.807),(834,779)),'Mulhouse':((7.338,47.750),(959,849)),'Belfort':((6.863,47.638),(551,996)),
'Epinal':((6.450,48.172),(233,349)),'Remiremont':((6.591,48.017),(357,535)),'Vesoul':((6.155,47.623),(54,928)),'Freiburg':((7.842,47.999),(1369,592)),'Rhinau':((7.705,48.319),(1247,207))}
A=np.array([[x+O[0],y+O[1],1] for (_, (x,y)) in G.values()],float); B=np.array([P(*ll) for (ll,_) in G.values()])
M,_,_,_=np.linalg.lstsq(A,B,rcond=None); res=np.hypot(*(A@M-B).T)/1000
pts=[(715,505),(690,540),(672,580),(665,620),(668,660),(690,715),(740,760),(800,800),(855,835),(910,848),(960,845),(1010,832),(1050,845),(1080,880),(1095,930),(1100,965)]
q=np.array([[x+O[0],y+O[1],1] for x,y in pts],float)@M; lon,lat=P(q[:,0],q[:,1],inverse=True)
json.dump({'colmar_sud_20jan':np.stack([lon,lat],1).round(5).tolist(),'residus_km':res.round(2).tolist(),'moyenne_km':float(res.mean())},open('colmar_sud_wp75_lonlat.json','w'))
