from picto import loading_source, reading_resource
from screenshot import get_ss, get_resource_ss
from config import connection
from datetime import datetime

# 黑市裝備價格擷取並讀取內容,將數據導入至資料庫
def insert_data():
    try:
        try:

            # 獲得黑市裝備交易介面圖
            get_ss()

        except:

            print("抓取圖片發生錯誤")

        try:

            # 讀取 source 資料夾內的圖片並輸出成字串
            final = loading_source()

        except:

            print("判讀圖片發生錯誤")
        
        # 連結至資料庫
        cursor = connection.cursor()
        # 設定輸入指令 | (日期, 時間, 裝備名稱, 階級, 附魔等級, 現在售價, 四週平均價)
        query = "INSERT INTO blackmarketprice (Date, Time, ItemName, Tier, Enchantment, SellOrderNow, AveragePrice) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = [
            # 現在日期、時間
            (datetime.today().date(), datetime.now().time().strftime("%H:%M:%S"),
            # 裝備名稱、階級、附魔、現在售價、平均售價
            final[0][1], final[1][1], final[2][1], final[3][1], final[4][1])
        ]
        # 使用 values 數值來執行 query 指令
        cursor.executemany(query, values)
        # 提交資料庫變更
        connection.commit()

        # 回傳整串資料 | (日期, 時間, 裝備名稱, 階級, 附魔等級, 現在售價, 四週平均價)
        return values
    
    # 常見錯誤例外事件處理
    except Exception as e:

        print(f"發生錯誤: {e}")

# 半成品價格擷取並讀取內容,將數據導入至資料庫 | (半成品類別代碼, 階級, 附魔等級)
def insert_resource_data(Category, Tier, Enchant):

    # 定義半成品類別
    resource_name = ['Cloth', 'Leather', 'MetalBar', 'Planks']

    try:
        try:

            # 獲取半成品市場估價圖片
            get_resource_ss()

        except:

            print("抓取圖片發生錯誤")

        try:

            # 獲取 99_Resource.png 圖片中的價格
            final = reading_resource()

        except:

            print("判讀圖片發生錯誤")
            
        # 連結至資料庫
        cursor = connection.cursor()
        # 設定輸入指令 | (日期, 時間, 半成品名稱, 階級, 附魔等級, 市場估價)
        query = "INSERT INTO albionbm.resourceprice (Date, Time, ResourceName, Tier, Enchantment, AveragePrice) VALUES (%s, %s, %s, %s, %s, %s)"
        values = [
            # 現在日期、時間
            (datetime.today().date(), datetime.now().time().strftime("%H:%M:%S"),
            # 半成品名稱、階級、附魔、平均售價
            resource_name[Category], Tier, Enchant, final)
        ]
        # 使用 values 數值來執行 query 指令
        cursor.executemany(query, values)
        # 提交資料庫變更
        connection.commit()

        # 回傳整串資料 | (日期, 時間, 半成品名稱, 階級, 附魔等級, 市場估價)
        return values
    
    # 常見錯誤例外事件處理
    except Exception as e:
        
        print(f"發生錯誤: {e}")
