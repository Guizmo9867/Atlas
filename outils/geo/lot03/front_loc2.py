import numpy as np, networkx as nx, pickle
from PIL import Image, ImageDraw
G,xs,ys,comps=pickle.load(open('skel.pkl','rb'))
def chemin(c,a,b):
    nodes=list(c); P=np.array([(xs[i],ys[i]) for i in nodes])
    ia=nodes[np.argmin(((P-a)**2).sum(1))]; ib=nodes[np.argmin(((P-b)**2).sum(1))]
    p=nx.shortest_path(G.subgraph(c),ia,ib,weight='weight'); return np.array([(xs[i],ys[i]) for i in p])
main=comps[0]
Pm=np.array([(xs[i],ys[i]) for i in main])
w=Pm[np.argmin(Pm[:,0])]; print('ouest',w)
princ=chemin(main,w,np.array([2310,2757]))
morceaux={'principal':princ}
for k,(a,b) in {'walcheren':((769,470),(849,440)),'beveland':((866,445),(951,440)),'tholen':((997,450),(1056,420)),'bout':((1078,421),(1125,421))}.items():
    c=[c for c in comps if any((abs(xs[i]-a[0])<6 and abs(ys[i]-a[1])<25) for i in list(c)[:2000])]
    # plus simple : composante contenant le point le plus proche de a
    best=None;bd=1e9
    for cc in comps[1:15]:
        P=np.array([(xs[i],ys[i]) for i in cc]); d=((P-a)**2).sum(1).min()
        if d<bd: bd=d;best=cc
    morceaux[k]=chemin(best,np.array(a),np.array(b))
pickle.dump(morceaux,open('front_px.pkl','wb'))
im=Image.open('loc12ag.jpg').convert('RGB'); d=ImageDraw.Draw(im)
for k,p in morceaux.items():
    d.line([tuple(x) for x in p],fill=(255,0,0),width=6); print(k,len(p),p[0],p[-1])
im.resize((1096,996)).save('front_check.jpg')
