import json, numpy as np
from scipy import ndimage, optimize
from shapely.geometry import shape, box
from gcp_loc import P, fit, VILLES
bleu=np.load('bleu.npy'); H,W=bleu.shape
D=ndimage.distance_transform_edt(~bleu)
zone=box(1.5,47.0,9.6,52.6)
pts=[]
for f in ['ne_10m_rivers_lake_centerlines','ne_10m_rivers_europe']:
    for ft in json.load(open(f+'.geojson'))['features']:
        g=shape(ft['geometry']).intersection(zone)
        if g.is_empty: continue
        for l in (g.geoms if hasattr(g,'geoms') else [g]):
            if l.geom_type!='LineString': continue
            n=max(2,int(l.length/0.01))
            for i in range(n+1):
                p=l.interpolate(i/n,normalized=True); pts.append((p.x,p.y))
pts=np.array(pts); X,Y=P(pts[:,0],pts[:,1]); X/=1e5; Y/=1e5
print(len(pts),'points')
def feats(X,Y,deg):
    F=[X,Y,np.ones_like(X)]
    if deg>=2: F+=[X*X,X*Y,Y*Y]
    return np.stack(F,1)
def perte(m,deg,c=25):
    F=feats(X,Y,deg); M=m.reshape(-1,2); q=F@M
    ok=(q[:,0]>0)&(q[:,0]<W-1)&(q[:,1]>0)&(q[:,1]<H-1)
    d=ndimage.map_coordinates(D,[q[ok,1],q[ok,0]],order=1)
    return np.mean(np.minimum(d,c))+ (1-ok.mean())*c
G=json.load(open('gcp.json')); M0=fit(G)
M0[0]*=1e5; M0[1]*=1e5
m=M0.ravel()
for c in [40,20,10,6]:
    r=optimize.minimize(perte,m,args=(1,c),method='Powell',options={'maxiter':20000,'xtol':1e-4,'ftol':1e-6}); m=r.x; print('affine',c,r.fun)
m2=np.concatenate([m.reshape(3,2),np.zeros((3,2))]).ravel()
for c in [10,6,4]:
    r=optimize.minimize(perte,m2,args=(2,c),method='Powell',options={'maxiter':40000,'xtol':1e-5,'ftol':1e-7}); m2=r.x; print('quad',c,r.fun)
F=feats(X,Y,2); q=F@m2.reshape(-1,2); d=ndimage.map_coordinates(D,[q[:,1],q[:,0]],order=1)
print('médiane px',np.median(d),'part <3px',(d<3).mean(),'<6px',(d<6).mean())
np.save('M_quad.npy',m2.reshape(-1,2))
