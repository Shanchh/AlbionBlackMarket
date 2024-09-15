import pyautogui
import time
import random

def check_script():

    tier_default = [545, 490]
    enchant_default = [790, 495]

    tier_t5 = [549, 583]
    enchant_e0 = [795, 535]
    interval = 47
    time.sleep(1.5)
    
    # 選擇裝備品質
    click_event(1057, 492)
    click_event(1055, 536)

    for i in range (4):

        click_event(tier_default[0], tier_default[1])

        click_event(tier_t5[0], tier_t5[1])
        tier_t5[1] += interval

        enchant_e0 = [795, 535]

        for j in range(3):

            click_event(enchant_default[0], enchant_default[1])

            click_event(enchant_e0[0], enchant_e0[1])
            enchant_e0[1] += interval

def click_event(x, y):
    time.sleep(random_dealy())
    pyautogui.moveTo(x, y)
    pyautogui.click()

def random_dealy():
    random_number = random.uniform(0.001, 0.7)
    return random_number

check_script()
