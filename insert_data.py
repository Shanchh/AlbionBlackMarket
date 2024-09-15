from picto import loading_source, reading_resource
from screenshot import get_ss, get_resource_ss
from config import connection
from datetime import datetime

def insert_data():

    try:
        try:
            get_ss()
        except:
            print("抓取圖片發生錯誤")

        try:
            final = loading_source()
        except:
            print("判讀圖片發生錯誤")
            
            
        cursor = connection.cursor()
        query = "INSERT INTO blackmarketprice (Date, Time, ItemName, Tier, Enchantment, SellOrderNow, AveragePrice) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = [
            # 現在日期、時間
            (datetime.today().date(), datetime.now().time().strftime("%H:%M:%S"),
            # 裝備名稱、階級、附魔、現在售價、平均售價
            final[0][1], final[1][1], final[2][1], final[3][1], final[4][1])
        ]
        cursor.executemany(query, values)
        connection.commit()

        return values
    except Exception as e:
        print(f"發生錯誤: {e}")

def insert_resource_data(Category, Tier, Enchant):

    resource_name = ['Cloth', 'Leather', 'MetalBar', 'Planks']

    try:
        try:
            get_resource_ss()
        except:
            print("抓取圖片發生錯誤")

        try:
            final = reading_resource()  
        except:
            print("判讀圖片發生錯誤")
            
            
        cursor = connection.cursor()
        query = "INSERT INTO albionbm.resourceprice (Date, Time, ResourceName, Tier, Enchantment, AveragePrice) VALUES (%s, %s, %s, %s, %s, %s)"
        values = [
            # 現在日期、時間
            (datetime.today().date(), datetime.now().time().strftime("%H:%M:%S"),
            # 半成品名稱、階級、附魔、平均售價
            resource_name[Category], Tier, Enchant, final)
        ]
        cursor.executemany(query, values)
        connection.commit()

        return values
    except Exception as e:
        print(f"發生錯誤: {e}")
