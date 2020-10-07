import pyautogui,time
from PIL import Image
import math
'''
img = pyautogui.screenshot()
img.save('new.jpg')
k=time.time()'''

u=[0,0,0]
l=[112,194,127]
def dis(pt1,pt2=(2,35,47)):
    #pt1=[170,10,154]
    pt2=(222,231,233)#[255,0,220]
    distance=math.sqrt(((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2)+((pt1[2]-pt2[2])**2))
    return(distance)

img = Image.open("000w.png")
g=[]
k=0
pix=[0,0,0]
pixno=0
no=[]
no0=[(170, 8, 160) ,
(170, 10, 162) ,
(172, 8, 160) ,
(198, 6, 179) ,
(227, 2, 199) ,
(228, 6, 203),
(170, 10, 158) ,
(170, 9, 160) ,
(170, 11, 161) ,
(170, 9, 161) ,
(181, 21, 171) ,
(198, 6, 178) ,
(201, 11, 186) ,
(228, 5, 201) ,]

def tell_color_dis(pt1,pt2,h=134.74791278531924):
    distance=math.sqrt(  ((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2)+((pt1[2]-pt2[2])**2)  )
    return(distance<=h)
for y in range(900):
    for x in range(1440):
        d=img.getpixel((x,y))
        #print(d[1]!=0 , d[0]!=255 , d[2]!=220, (tell_color_dis(d,(4,36,48),190.4051442080838)!=True))
        if d[1]!=0 and d[0]!=255 and d[2]!=220 and (tell_color_dis(d,(4,36,48),190.4051442080838)!=True):#dis(d,[170,10,154])>10 and 
            pixno+=1
            pix[0]+=d[0]
            pix[1]+=d[1]
            pix[2]+=d[2]
            if d not in g :
                fr=dis(d)
                if k<fr and d not in no:
                    k=fr
                    print(d,',',(x,y))
                    


print(k,pix[0]/pixno,pix[1]/pixno,pix[2]/pixno)



