import json, numpy as np, pyproj
from scipy import ndimage, optimize
from shapely.geometry import shape, box
P=pyproj.Proj('+proj=lcc +lat_1=44 +lat_2=50 +lon_0=3 +lat_0=47')
E=np.load('wp71_bord.npy'); H,W=E.shape
D=ndimage.distance_transform_edt(~E)
zone=box(-5.5,42.5,10.5,54.5)
pts=[]
for f,step in [('ne_10m_coastline',0.02),('ne_10m_rivers_lake_centerlines',0.03)]:
    for ft in json.load(open(f+'.geojson'))['features']:
        if f.startswith('ne_10m_rivers') and ft['properties'].get('scalerank',9)>6: continue
        g=shape(ft['geometry']).intersection(zone)
        if g.is_empty: continue
        for l in (g.geoms if hasattr(g,'geoms') else [g]):
            if l.geom_type!='LineString': continue
            n=max(2,int(l.length/step))
            for i in range(n+1):
                p=l.interpolate(i/n,normalized=True); pts.append((p.x,p.y))
pts=np.array(pts); X,Y=P(pts[:,0],pts[:,1]); X=np.asarray(X)/1e5; Y=np.asarray(Y)/1e5
print(len(pts))
GCP={(2.35,48.86):(2192,1512),(-0.58,44.84):(1640,2488),(-4.49,48.39):(1000,1544),(7.26,43.70):(3104,2820),(-3.37,47.75):(1184,1724),(5.04,47.32):(2644,1864)}
A=[];B=[]
for (lo,la),(x,y) in GCP.items():
    a,b=P(lo,la); A.append([a/1e5,b/1e5,1]); B.append([x,y])
M0,_,_,_=np.linalg.lstsq(np.array(A),np.array(B),rcond=None)
print('résidus GCP grossiers',np.round(np.array(A)@M0-np.array(B)))
def feats(deg):
    F=[X,Y,np.ones_like(X)]
    if deg>=2: F+=[X*X,X*Y,Y*Y]
    return np.stack(F,1)
def perte(m,deg,c):
    q=feats(deg)@m.reshape(-1,2)
    ok=(q[:,0]>0)&(q[:,0]<W-1)&(q[:,1]>0)&(q[:,1]<H-1)
    d=ndimage.map_coordinates(D,[q[ok,1],q[ok,0]],order=1)
    return np.mean(np.minimum(d,c))+(1-ok.mean())*c
m=M0.ravel()
for c in [80,40,20,10,6]:
    r=optimize.minimize(perte,m,args=(1,c),method='Powell',options={'maxiter':20000}); m=r.x; print('aff',c,round(r.fun,2))
m2=np.concatenate([m.reshape(3,2),np.zeros((3,2))]).ravel()
for c in [10,6,4]:
    r=optimize.minimize(perte,m2,args=(2,c),method='Powell',options={'maxiter':40000}); m2=r.x; print('quad',c,round(r.fun,2))
q=feats(2)@m2.reshape(-1,2); d=ndimage.map_coordinates(D,[q[:,1],q[:,0]],order=1)
print('médiane',np.median(d),'<3px',(d<3).mean())
np.save('M71.npy',m2.reshape(-1,2))
