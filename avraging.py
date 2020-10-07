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
    pt2=(199,40,58)#[255,0,220]
    distance=math.sqrt(((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2)+((pt1[2]-pt2[2])**2))
    return(distance)

img = Image.open("Untitled.png")
g=[]
k=0
pix=[0,0,0]
pixno=0
no=[]
for y in range(900):
    for x in range(1440):
        d=img.getpixel((x,y))
        if d[1]>0 and d[0]>0:#dis(d,[170,10,154])>10 and 
            pixno+=1
            pix[0]+=d[0]
            pix[1]+=d[1]
            pix[2]+=d[2]
            if d not in g :
                fr=dis(d)
                if k<fr and d not in no:
                    k=fr
                    print(d,',')
                    


print(k,pix[0]/pixno,pix[1]/pixno,pix[2]/pixno)



