# Extraction des arcs rouges des poches (carte West Point 71) puis conversion en lon/lat avec l'inverse de M71.npy
# (même code que celui exécuté le 28/09/2026 ; voir README.md de ce dossier)
import numpy as np, json, pyproj, networkx as nx
from skimage.measure import label
from skimage.morphology import skeletonize
P=pyproj.Proj('+proj=lcc +lat_1=44 +lat_2=50 +lon_0=3 +lat_0=47')
M=np.load('M71.npy')
def fwd(lon,lat):
    X,Y=P(lon,lat); X=np.asarray(X)/1e5; Y=np.asarray(Y)/1e5
    return np.stack([X,Y,np.ones_like(X),X*X,X*Y,Y*Y],-1)@M
lo,la=np.meshgrid(np.linspace(-6,11,150),np.linspace(42,55,150)); lo=lo.ravel(); la=la.ravel()
px=fwd(lo,la); X,Y=P(lo,la)
def F(p):
    x=p[:,0]/1000; y=p[:,1]/1000
    return np.stack([np.ones_like(x),x,y,x*x,x*y,y*y,x**3,x*x*y,x*y*y,y**3],1)
C,_,_,_=np.linalg.lstsq(F(px),np.stack([X,Y],1),rcond=None)
def inv(p):
    q=F(np.asarray(p,float))@C; lon,lat=P(q[:,0],q[:,1],inverse=True); return np.stack([lon,lat],1)
rouge=np.load('wp71_rouge.npy'); lab=label(rouge,connectivity=2)
BOX={'dunkerque':(2176,919,2228,968),'lorient':(1188,1678,1260,1746),'saint_nazaire':(1365,1819,1450,1885),'la_rochelle':(1530,2087,1599,2201),'royan':(1563,2265,1629,2349),'pointe_de_grave':(1524,2354,1593,2369)}
out={}
for k,(x0,y0,x1,y1) in BOX.items():
    sub=lab[y0:y1+1,x0:x1+1]; ids,c=np.unique(sub[sub>0],return_counts=True); i=ids[np.argmax(c)]
    sk=skeletonize(lab==i); ys,xs=np.nonzero(sk)
    idx={(y,x):n for n,(y,x) in enumerate(zip(ys,xs))}; G=nx.Graph()
    for (y,x),n in idx.items():
        for dy in (-1,0,1):
            for dx in (-1,0,1):
                j=idx.get((y+dy,x+dx))
                if j is not None and j>n: G.add_edge(n,j,weight=(dx*dx+dy*dy)**.5)
    d1=nx.single_source_dijkstra_path_length(G,next(iter(G.nodes))); u=max(d1,key=d1.get)
    d2,p2=nx.single_source_dijkstra(G,u); v=max(d2,key=d2.get)
    pts=np.array([(xs[n],ys[n]) for n in p2[v]])[::3]
    out[k]=inv(pts).round(5).tolist()
json.dump(out,open('poches_wp71_lonlat.json','w'))
