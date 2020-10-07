import pyautogui
import time
import math

def dis(pt1):
    pt1=[255,0,255]
    pt2=[76,255,0]#109
    distance=math.sqrt(  ((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2)+((pt1[2]-pt2[2])**2)  )
    return(distance<=187.11761007451972)
def check_dis(k):
    for i in range(len(k)):
        if dis(k[i]):
            return True
    return False

def tell_color_dis(pt1,pt2,h=134.74791278531924):
    distance=math.sqrt(  ((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2)+((pt1[2]-pt2[2])**2)  )
    return(distance<=h)
k=0
while True:
    im = pyautogui.screenshot()
    
    for i in range(409):#703 110#737 110im.getpixel((722,662))
        g=im.getpixel((811,820))
        #if color in not from bg
        f=[im.getpixel((711,110+i)),im.getpixel((722,110+i))]
        if (
            (
            (tell_color_dis(f[0],(4,36,48),190.4051442080838)!=True)or
            (tell_color_dis(f[1],(4,36,48),190.4051442080838)!=True)
            ) and#and...........
            (
            (tell_color_dis(f[0],(222,231,233),146.13350060817677)!=True)or
            (tell_color_dis(f[1],(222,231,233),146.13350060817677)!=True)
            )
            ):#and g!=(143,216,76) and g!=(255,255,255) and tell_color_dis(g,(199,40,58),159.01572249309186) ):
            pyautogui.click(720, 664)
            im.save('G:\\Downloads\\Compressed\\scrcpy-win64-v1.8\\MLP\\fruteslice\\data\\'+str(k)+'.png')
            k+=1
            time.sleep(1)
            break
        






    
    
