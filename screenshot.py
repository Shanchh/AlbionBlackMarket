import pyautogui
import os


# 獲得道具名稱圖片
def get_ss():   

    Value = [
        # [內容名稱],[left], [top], [width], [height]
        ["ItemName", 723, 396, 483, 50],
        ["Enchantment", 814, 525, 132, 20],
        ["SellOrderNow", 1356, 485, 110, 32],
        ["AveragePrice", 1878, 948, 80, 30]
    ]

    for result in Value:
        take_ss(result[1], result[2], result[3], result[4], result[0])

def take_ss(left, top, width, height, name):

    # 擷取螢幕的指定範圍
    screenshot = pyautogui.screenshot(region=(left, top, width, height))

    output = str(name) + ".png"

    # 保存為圖片
    screenshot.save(os.path.join('source', output))
