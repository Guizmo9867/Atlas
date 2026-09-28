import numpy as np, networkx as nx, json
from skimage.morphology import skeletonize
from skimage.measure import label
op=np.load('noir_op.npy')
# retirer le cartouche (titre + légende) et la marge
op[:330,:1300]=False; op[:400,:960]=False; op[2350:,:700]=False; op[2760:,:]=False
lab=label(op,connectivity=2)
sizes=np.bincount(lab.ravel()); sizes[0]=0
sk=skeletonize(op)
ys,xs=np.nonzero(sk)
idx={(y,x):i for i,(y,x) in enumerate(zip(ys,xs))}
G=nx.Graph()
for (y,x),i in idx.items():
    for dy in (-1,0,1):
        for dx in (-1,0,1):
            j=idx.get((y+dy,x+dx))
            if j is not None and j>i: G.add_edge(i,j,weight=(dx*dx+dy*dy)**.5)
comps=sorted(nx.connected_components(G),key=len,reverse=True)
out=[]
for c in comps[:40]:
    pts=np.array([(xs[i],ys[i]) for i in c])
    out.append((len(c),pts.min(0).tolist(),pts.max(0).tolist()))
for o in out[:25]: print(o)
nx.write_gpickle=None
import pickle; pickle.dump((G,xs,ys,comps[:40]),open('skel.pkl','wb'))
