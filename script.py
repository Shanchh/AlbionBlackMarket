import pyautogui
import time
import random
from insert_data import insert_data

def check_script():

    data =[]

    tier_default = [545, 490]
    enchant_default = [790, 495]

    tier_t5 = [549, 583]
    enchant_e0 = [795, 535]
    interval = 47
    # time.sleep(1.5)
    
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

            data.append(insert_data())
    
    return data

def click_event(x, y):
    time.sleep(random_delay())
    pyautogui.moveTo(x, y)
    pyautogui.click()

def random_delay():
    random_number = random.uniform(0.001, 0.7)
    return random_number

def long_random_delay():
    random_number = random.uniform(1.5, 2)
    return random_number

def resource_script(value):
    # 布料Cloth、皮革Leather、鐵條MetalBar、木條Planks、類別選項、類別半成品
    check_point = [951, 975], [951, 1107], [915,1153], [915, 1289], [718, 340], [714, 1241]

    click_event(check_point[4][0],check_point[4][1])

    time.sleep(random_delay())
    pyautogui.moveTo(check_point[5][0],check_point[5][1])
    
    click_event(check_point[value][0],check_point[value][1])

def resource_tier_script(value):

    Tier_Point = [966, 338]
    Tier4_Point = [964, 564]
    interval = 44

    click_event(Tier_Point[0], Tier_Point[1])

    click_event(Tier4_Point[0], int(Tier4_Point[1]) + (interval * value))

def resource_enchant_script(value):

    Enchant_Point = [675, 575]
    interval = 131

    click_event(Enchant_Point[0], int(Enchant_Point[1]) + (interval * value))

# check_script()
