import pyautogui

#屏幕大小
size=pyautogui.size()
print(size)

#滑鼠位置
mouse_pose=pyautogui.position()
print(mouse_pose)

#判斷點是否在螢幕內
print(pyautogui.onScreen(100,100))

#將滑鼠移動到(10,10)的位置，週期1秒鐘
pyautogui.moveTo(10,10,duration=1)

#將滑鼠移動到畫面中間的位置，週期0.5秒鐘
pyautogui.moveTo(size.width/2,size.height/2,duration=0.5)

#以當前滑鼠的位置相對移動x軸向右100，週期1秒
pyautogui.moveRel(100,None,duration=1)

 

#隨時取得滑鼠座標

last_pos=pyautogui.position()
try:
    while True:
        #新位置
        new_pos=pyautogui.position()
        if last_pos!= new_pos:
            print(new_pos) 
            last_pos=new_pos
except KeyboardInterrupt:
    print('\nExit')