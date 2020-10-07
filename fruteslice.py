import pyautogui
import time
import math
import PIL

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
    im = PIL.ImageGrab.grab()
    pyautogui.moveTo(70, 664)
    flag=0
    for i in range(409):#703 110#737 110im.getpixel((722,662))
        g=im.getpixel((811,820))
        #if color in not from bg
        f=[im.getpixel((685,110+i)),im.getpixel((756,110+i))]
        direction=''
        if (
            (tell_color_dis(f[0],(4,36,48),190.4051442080838)!=True)and
            (tell_color_dis(f[0],(222,231,233),146.13350060817677)!=True)):
            direction='lr'
        if(
            (tell_color_dis(f[1],(4,36,48),190.4051442080838)!=True)and
            (tell_color_dis(f[1],(222,231,233),146.13350060817677)!=True)
            ):
            direction='rl'
        '''
        for k in range(80):
            if direction=='lr':
                if (
                (tell_color_dis(im.getpixel((684+k,110)),(4,36,48),190.4051442080838)!=True)and((tell_color_dis(im.getpixel((684+k,110)),(222,231,233),146.13350060817677)!=True))):
                    flag+=1
                    break
            if direction=='rl':
                if (
                (tell_color_dis(im.getpixel((760-k,110)),(4,36,48),190.4051442080838)!=True)and(tell_color_dis(im.getpixel((760-k,110)),(222,231,233),146.13350060817677)!=True)):
                    flag+=1
                    break
        '''
        if flag!=1 and direction!='':
            #pyautogui.dragTo(720,50,duration=0.2)
            pyautogui.click(720, 664)
            print('pweee',direction)
            #im.save('G:\\Downloads\\Compressed\\scrcpy-win64-v1.8\\MLP\\fruteslice\\data\\'+str(k)+'.png')
            k+=1
            time.sleep(1)
            break
    






    
    
