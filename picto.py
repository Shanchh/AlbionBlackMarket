from PIL import Image
import pytesseract
import os

def loading_source():

    folder_path = 'source/'
    files = os.listdir(folder_path)

    for result in files:
        read_pic(folder_path, result)

def read_pic(folder_path, name):

    # 載入圖片
    image_path = str(folder_path) + str(name)
    image = Image.open(image_path)

    # 使用 Tesseract 提取圖片中的文字
    text = pytesseract.image_to_string(image, lang='eng')

    file_n, file_e = os.path.splitext(name)

    print(f"{file_n}: {text}")
