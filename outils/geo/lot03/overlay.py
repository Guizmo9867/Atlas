import json, sys, numpy as np
from PIL import Image, ImageDraw
from shapely.geometry import shape, box
from gcp_loc import P, VILLES
M=np.load(sys.argv[1]); x0,y0,x1,y1=map(int,sys.argv[2:6])
def proj(lon,lat):
    X,Y=P(np.asarray(lon),np.asarray(lat)); X=X/1e5; Y=Y/1e5
    F=[X,Y,np.ones_like(X)]
    if M.shape[0]==6: F+=[X*X,X*Y,Y*Y]
    return np.stack(F,-1)@M
im=Image.open('loc12ag.jpg').convert('RGB').crop((x0,y0,x1,y1)); d=ImageDraw.Draw(im)
zone=box(1.5,47,9.6,52.6)
for f in ['ne_10m_rivers_lake_centerlines','ne_10m_rivers_europe']:
    for ft in json.load(open(f+'.geojson'))['features']:
        g=shape(ft['geometry']).intersection(zone)
        for l in (g.geoms if hasattr(g,'geoms') else [g]):
            if l.geom_type!='LineString': continue
            c=np.array(l.coords); q=proj(c[:,0],c[:,1])
            d.line([(a-x0,b-y0) for a,b in q],fill=(255,0,0),width=1)
for n,(lo,la) in VILLES.items():
    a,b=proj(lo,la); d.ellipse([a-x0-4,b-y0-4,a-x0+4,b-y0+4],outline=(0,160,0),width=2); d.text((a-x0+5,b-y0-5),n,fill=(0,120,0))
im.save(sys.argv[6])
