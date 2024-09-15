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
    pyautogui.moveTo(1057, 492)
    pyautogui.click()
    time.sleep(random_dealy())
    pyautogui.moveTo(1055, 536)
    pyautogui.click()

    for i in range (4):

        time.sleep(random_dealy())
        pyautogui.moveTo(tier_default[0], tier_default[1])
        pyautogui.click()

        time.sleep(random_dealy())
        pyautogui.moveTo(tier_t5[0], tier_t5[1])
        tier_t5[1] += interval
        pyautogui.click()

        enchant_e0 = [795, 535]

        for j in range(3):

            time.sleep(random_dealy())
            pyautogui.moveTo(enchant_default[0], enchant_default[1])
            pyautogui.click()

            time.sleep(random_dealy())
            pyautogui.moveTo(enchant_e0[0], enchant_e0[1])
            enchant_e0[1] += interval
            pyautogui.click()

    pass

def random_dealy():
    random_number = random.uniform(0.001, 0.7)
    return random_number

# check_script()
