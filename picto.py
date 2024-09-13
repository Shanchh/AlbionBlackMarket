from PIL import Image
import pytesseract

# 載入圖片
image_path = 'screenshot.png'
image = Image.open(image_path)

# 保存或直接處理
image.save('processed_image.png')

# 使用 Tesseract 提取圖片中的文字
text = pytesseract.image_to_string(image, lang='eng')

print("提取的文字：")   
print(text)