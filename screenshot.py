import pyautogui
import os


# 獲得道具名稱圖片
def get_ss():   

    # 80% 介面
    # Value = [
    #     # [內容名稱],[left], [top], [width], [height]
    #     ["1_ItemName", 723, 396, 483, 50],
    #     ["3_Enchantment", 814, 525, 132, 20],
    #     ["4_SellOrderNow", 1356, 485, 110, 32],
    #     ["5_AveragePrice", 1878, 948, 80, 30]
    # ]

    # 100% 介面
    Value = [
        # [內容名稱],[left], [top], [width], [height]
        ["1_ItemName", 574, 315, 634, 60],
        ["3_Enchantment", 702, 478, 160, 23],
        ["4_SellOrderNow", 1372, 435, 135, 28],
        ["5_AveragePrice", 2022, 999, 108, 40]
    ]

    for result in Value:
        take_ss(result[1], result[2], result[3], result[4], result[0])

    print("已截圖")

def take_ss(left, top, width, height, name):

    # 擷取螢幕的指定範圍
    screenshot = pyautogui.screenshot(region=(left, top, width, height))

    output = str(name) + ".png"

    # 保存為圖片
    screenshot.save(os.path.join('source', output))

# get_ss()