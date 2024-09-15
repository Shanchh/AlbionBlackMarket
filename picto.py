from PIL import Image, ImageEnhance
import pytesseract
import os

def loading_source():

    export = []
    folder_path = 'source/'
    files = os.listdir(folder_path)

    for result in files:
        data = read_pic(folder_path, result)
        export.append([data[0], data[1].strip()])
        
    final_ex = tidy_data(export)

    # print(final_ex)

    return final_ex

def read_pic(folder_path, name):

    # 載入圖片
    image_path = str(folder_path) + str(name)
    image = Image.open(image_path)

    # 使用 Tesseract 提取圖片中的文字
    text = pytesseract.image_to_string(image, lang='eng')

    file_n, file_e = os.path.splitext(name)

    return file_n, text

def tidy_data(export):

    sname = split_first_space(export[0][1])

    # 分割階級與物品名稱
    export[0][1] = sname[1]
    tier_name = w_corrections(sname[0])
    insert_data = ['2_Tier', tier_name]
    export.insert(1,insert_data)

    # 附魔文字取最後一個字
    export[2][1] = export[2][1][-1]

    # SellOrder去除所有符號
    export[3][1] = export[3][1].replace(",","")

    # AveragePrice將K,M轉為數字
    export[4][1] = AP_trans(export[4][1])

    return export

def split_first_space(text):

    # 分割字符串，最多分割一次
    parts = text.split(' ', 1)
    
    if len(parts) == 2:
        f_parts = parts[0][:-2]
        return f_parts, parts[1]
    else:
        return text, ''

def AP_trans(value):

    if value[-1] == 'm':
        return int(float(value[:-1]) * 1000000)
    elif value[-1] == 'k':
        return int(value[:-1]) * 1000
    else:
        value = value.replace(",","")
        return int(value) 

def w_corrections(check_v):

    corrections = {
        "Masfer": "Master",
    }
    
    for wrong, correct in corrections.items():
        output_v = check_v.replace(wrong, correct)
        if check_v != output_v:
            print(f"已自動將Tier[{wrong}]修正成[{correct}]")

    return output_v

# loading_source()