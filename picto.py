from PIL import Image
import pytesseract
import os

# 讀取 source 資料夾內的圖片並輸出成字串
def loading_source():

    export = []

    # 設定贖取資料夾路徑
    folder_path = 'source/'
    # 讀取 folder_path 路徑內的所有資料名稱
    files = os.listdir(folder_path)

    # 將所有圖片進行 For 迴圈
    for result in files:

        # 將圖片內容讀取成文字 | (資料夾路徑, 檔案名稱)
        data = read_pic(folder_path, result)
        # 把data[1]後的\n刪除,並將資料新增至 export | (檔案名稱, 輸出內容)
        export.append([data[0], data[1].strip()])
        
    # 整理數據
    final_ex = tidy_data(export)

    # 回傳整理完的所有數據 [(1~99_標題), 數據] 2x6陣列
    return final_ex

# 單獨讀取 99_Resource.png 半成品圖片
def reading_resource():

    # 將圖片內容讀取成文字 | (資料夾路徑, 檔案名稱)
    data = read_pic('source/', '99_Resource.png')

    # 將 data[1] 去掉\n後將K,M轉為數字
    re_data = AP_trans(data[1].strip())
    
    # 回傳半成品價格
    return re_data

# 讀取圖片轉為文字 | (資料夾路徑, 檔案名稱)
def read_pic(folder_path, name):

    # 設定檔案路徑 | source/ + 檔案名稱
    image_path = str(folder_path) + str(name)
    # 開啟路徑檔案
    image = Image.open(image_path)

    # 使用 Tesseract 提取圖片中的文字 eng為英文
    text = pytesseract.image_to_string(image, lang='eng')

    # 分離檔名與附檔名
    file_n, file_e = os.path.splitext(name)

    # 回傳檔名,輸出結果
    return file_n, text

# 整理資料
def tidy_data(export):

    # 分割裝備名稱內的階級與裝備名稱 | sname = 階級名稱, 裝備名稱
    sname = split_first_space(export[0][1])

    # 將分割完的裝備名稱傳回 export 資料陣列
    export[0][1] = sname[1]
    # tier_name 易別字修正
    tier_name = w_corrections(sname[0])
    # 定義要輸入 export 陣列的 Tier 資料
    insert_data = ['2_Tier', tier_name]
    # 將 insert_data 插入至 export 第1列的位置
    export.insert(1,insert_data)

    # 附魔文字取最後一個字
    export[2][1] = export[2][1][-1]

    # SellOrder去除所有符號
    export[3][1] = export[3][1].replace(",","")

    # AveragePrice將K,M轉為數字
    export[4][1] = AP_trans(export[4][1])

    # 回傳 export 裝備資料價格陣列
    return export

# 分割裝備名稱內的階級與裝備名稱
def split_first_space(text):

    # 分割字串，設定分割1次
    parts = text.split(' ', 1)
    
    # 如果成功分割成兩個字符
    if len(parts) == 2:

        # 去除階級後綴的 's 兩個字
        f_parts = parts[0][:-2]

        # 回傳 | 階級名稱, 裝備名稱
        return f_parts, parts[1]
    
    else:
        
        # 不變更回傳
        return text, ''

# 價格 K,M 轉為數字金額
def AP_trans(value):

    # 如果字串最後一個字為 M
    if value[-1] == 'm':

        # 將資料去掉 M 以後乘以 1000000 轉為 INT
        return int(float(value[:-1]) * 1000000)
    
    # 如果字串最後一個字為 K
    elif value[-1] == 'k':

        # 將資料去掉 K 以後乘以 1000 轉為 INT
        return int(value[:-1]) * 1000
    
    else:

        # 將 Value 中的 , 符號去除
        value = value.replace(",","")
        # 回傳 Value
        return int(value) 

# 易錯字修正
def w_corrections(check_v):

    # 易錯字辭典
    corrections = {

        "Masfer": "Master",

    }
    
    # 遍歷字典 `corrections` 中的每一個錯誤(wrong)與對應的正確(correct)值
    for wrong, correct in corrections.items():
        
        # 使用 replace 將 `check_v` 中所有的錯誤值替換為正確值
        output_v = check_v.replace(wrong, correct)

        # 如果 check_v 和 output_v 不相等
        if check_v != output_v:

            print(f"已自動將Tier[{wrong}]修正成[{correct}]")

    # 回傳 (無須修正/修正完) 結果
    return output_v

reading_resource()