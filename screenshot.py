import pyautogui
import os

# 獲得黑市裝備交易介面圖 (需設定2560x1440並100%視窗)
def get_ss():   

    # 80% 介面數值 | [內容名稱],[left], [top], [width], [height]
    # Value = [
    #     # [內容名稱],[left], [top], [width], [height]
    #     ["1_ItemName", 723, 396, 483, 50],
    #     ["3_Enchantment", 814, 525, 132, 20],
    #     ["4_SellOrderNow", 1356, 485, 110, 32],
    #     ["5_AveragePrice", 1878, 948, 80, 30]
    # ]

    # 100% 介面數值 | [內容名稱],[left], [top], [width], [height]
    Value = [
        ["1_ItemName", 574, 315, 634, 60],
        ["3_Enchantment", 702, 478, 160, 23],
        ["4_SellOrderNow", 1372, 435, 135, 28],
        ["5_AveragePrice", 2022, 999, 108, 40]
    ]

    # 在 Value 中執行迴圈
    for result in Value:

        # 執行畫面截圖 Function | take,ss(left, top, width, height, name)
        take_ss(result[1], result[2], result[3], result[4], result[0])

    print("已截圖")

# 畫面截圖相關 Function
def take_ss(left, top, width, height, name):

    # 擷取螢幕的指定範圍
    screenshot = pyautogui.screenshot(region=(left, top, width, height))

    # 將 output 值設定為圖片說明值
    output = str(name) + ".png"

    # 保存名為 output 的圖片
    screenshot.save(os.path.join('source', output))

# 獲取半成品市場估價圖片 (需將視窗拉至右下角)
def get_resource_ss():

    # [內容名稱],[left], [top], [width], [height]
    Value = ["99_Resource", 2252, 915, 89, 35]

    # 執行畫面截圖 Function | take,ss(left, top, width, height, name)
    take_ss(Value[1], Value[2], Value[3], Value[4], Value[0])

    print("已截圖")

# get_resource_ss()