import sys
from PIL import Image, ImageDraw
im=Image.open('loc12ag.jpg').convert('RGB')
x0,y0,x1,y1=map(int,sys.argv[1:5]); out=sys.argv[5]
c=im.crop((x0,y0,x1,y1)); d=ImageDraw.Draw(c)
for x in range((x0//50+1)*50,x1,50):
    d.line([(x-x0,0),(x-x0,y1-y0)],fill=(255,0,0) if x%100==0 else (255,170,170),width=1)
    if x%100==0: d.text((x-x0+2,2),str(x),fill=(200,0,0))
for y in range((y0//50+1)*50,y1,50):
    d.line([(0,y-y0),(x1-x0,y-y0)],fill=(255,0,0) if y%100==0 else (255,170,170),width=1)
    if y%100==0: d.text((2,y-y0+2),str(y),fill=(200,0,0))
c.save(out)
