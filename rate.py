import pyautogui
import time
#'''
h=time.time()
for i in range(20):
    im = pyautogui.screenshot()
    #print(im.getpixel((571,110+i)))
g=time.time()
print(g-h)
#'''
    
import PIL.ImageGrab

#im = PIL.ImageGrab.grab()
#im.show()
h=time.time()
for i in range(20):
    im = PIL.ImageGrab.grab()
    #print(im.getpixel((571,110+i)))
g=time.time()
print(g-h)
