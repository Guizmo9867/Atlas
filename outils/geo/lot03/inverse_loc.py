import numpy as np, pickle, json
from gcp_loc import P
M=np.load('M_quad.npy')
def fwd(lon,lat):
    X,Y=P(lon,lat); X=np.asarray(X)/1e5; Y=np.asarray(Y)/1e5
    return np.stack([X,Y,np.ones_like(X),X*X,X*Y,Y*Y],-1)@M
lo,la=np.meshgrid(np.linspace(1,10,120),np.linspace(46.5,53,120)); lo=lo.ravel(); la=la.ravel()
px=fwd(lo,la); X,Y=P(lo,la)
def F(p):
    x=p[:,0]/1000; y=p[:,1]/1000
    return np.stack([np.ones_like(x),x,y,x*x,x*y,y*y,x**3,x*x*y,x*y*y,y**3],1)
C,_,_,_=np.linalg.lstsq(F(px),np.stack([X,Y],1),rcond=None)
err=np.hypot(*(F(px)@C-np.stack([X,Y],1)).T); print('erreur inverse m: max',err.max(),'moy',err.mean())
def inv(p):
    q=F(np.asarray(p,float))@C; lon,lat=P(q[:,0],q[:,1],inverse=True); return np.stack([lon,lat],1)
morceaux=pickle.load(open('front_px.pkl','rb'))
out={k:inv(v).round(5).tolist() for k,v in morceaux.items() if k in ('principal','walcheren','beveland')}
json.dump(out,open('front_loc_lonlat.json','w'))
for k,v in out.items(): print(k,len(v),v[0],v[-1])
np.save('C_inv.npy',C)
