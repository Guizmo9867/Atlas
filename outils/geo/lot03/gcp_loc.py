import json, sys, numpy as np, pyproj
from PIL import Image, ImageDraw
P = pyproj.Proj('+proj=lcc +lat_1=45 +lat_2=55 +lon_0=5 +lat_0=50')
VILLES = {'Middelburg':(3.61,51.50),'Vlissingen':(3.57,51.44),'Rotterdam':(4.48,51.92),'Dordrecht':(4.67,51.81),"'s-Hertogenbosch":(5.30,51.69),
'Tilburg':(5.09,51.56),'Eindhoven':(5.48,51.44),'Nijmegen':(5.86,51.84),'Antwerpen':(4.40,51.22),'Gent':(3.72,51.05),'Bruxelles':(4.35,50.85),
'Leuven':(4.70,50.88),'Liege':(5.57,50.63),'Namur':(4.87,50.47),'Maastricht':(5.69,50.85),'Aachen':(6.08,50.78),'Koln':(6.96,50.94),'Bonn':(7.10,50.73),
'Koblenz':(7.59,50.36),'Trier':(6.64,49.75),'Luxembourg':(6.13,49.61),'Metz':(6.18,49.12),'Nancy':(6.18,48.69),'Saarbrucken':(7.00,49.23),
'Strasbourg':(7.75,48.58),'Colmar':(7.36,48.08),'Mulhouse':(7.34,47.75),'Basel':(7.59,47.56),'Reims':(4.03,49.26),'Paris':(2.35,48.86),
'Frankfurt':(8.68,50.11),'Mannheim':(8.47,49.49),'Karlsruhe':(8.40,49.01),'Sedan':(4.94,49.70),'Verdun':(5.38,49.16),'Epinal':(6.45,48.17),
'Troyes':(4.07,48.30),'Dijon':(5.04,47.32),'Besancon':(6.02,47.24),'Bastogne':(5.72,50.00),'Arlon':(5.82,49.68),'Lille':(3.06,50.63),'Amiens':(2.30,49.89),
'Dusseldorf':(6.78,51.23),'Mainz':(8.27,50.00),'St-Quentin':(3.29,49.85),'Charleroi':(4.44,50.41),'Hasselt':(5.34,50.93),'Venlo':(6.17,51.37),'Roermond':(5.99,51.19),
'Sarreguemines':(7.07,49.11),'Haguenau':(7.79,48.82),'Belfort':(6.86,47.64),'Chalons':(4.36,48.96),'Kaiserslautern':(7.77,49.44),'Wissembourg':(7.94,49.04)}
def fit(G):
    A=[];B=[]
    for n,(x,y) in G.items():
        X,Y=P(*VILLES[n]); A.append([X,Y,1]); B.append([x,y])
    A=np.array(A);B=np.array(B); M,_,_,_=np.linalg.lstsq(A,B,rcond=None); return M
def pred(M,n):
    X,Y=P(*VILLES[n]); return np.array([X,Y,1])@M
if __name__=='__main__':
    G=json.load(open('gcp.json'))
    M=fit(G)
    for n,(x,y) in G.items():
        p=pred(M,n); print(f'{n:15} res {p[0]-x:6.1f} {p[1]-y:6.1f}')
    im=Image.open('loc12ag.jpg').convert('RGB')
    noms=sys.argv[1].split(',')
    T=[]
    for n in noms:
        px,py=pred(M,n); c=im.crop((int(px)-100,int(py)-100,int(px)+100,int(py)+100)).resize((400,400)); d=ImageDraw.Draw(c)
        for k in range(0,400,20): 
            col=(255,0,0) if k==200 else ((255,190,190) if k%100 else (255,120,120))
            d.line([(k,0),(k,399)],fill=col); d.line([(0,k),(399,k)],fill=col)
        d.text((4,4),f'{n} {int(px)},{int(py)}',fill=(0,0,200))
        T.append(c)
    W=Image.new('RGB',(400*min(3,len(T)),400*((len(T)+2)//3)),'white')
    for i,c in enumerate(T): W.paste(c,((i%3)*400,(i//3)*400))
    W.save('tuiles.jpg')
