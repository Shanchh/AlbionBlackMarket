from config import connection

# 從資料庫調特定種類半成品的所有階級附魔價格
def resource_price_search(Category):
    
    # 將Category字串取一個值並-1
    num = int(Category[0]) -1

    # 連結至資料庫
    cursor = connection.cursor()

    # 定義所有半成品種類名稱
    Resource_name = ["Cloth", "Leather", "MetalBar", "Planks"]

    # 從資料庫搜尋 用半成品名稱、階級、附魔並日期、時間為最新的一條資料 
    query = """
    SELECT *
    FROM resourceprice
    WHERE ResourceName = %s
      AND Tier = %s
      AND Enchantment = %s
    ORDER BY Date DESC, Time DESC
    LIMIT 1;
    """

    data = []

    # 用For迴圈執行階級 0~5
    for i in range(5):
            
        row = []

        # 定義字串第一筆為階級說明 Tier4 ~ Tier8
        Tier = "Tier" + str(i + 4)
        # 將 Tier 新增至字串
        row.append(Tier)

        for j in range(5):
            
            # 定義資料庫指令的導入變數 (半成品種類選擇、階級、附魔)
            params = (Resource_name[num], i + 4, j)

            # 執行資料庫指令 query
            cursor.execute(query, params)

            # 將執行結果導入至 result | result = [ID, Date, Time, ResourceName, Tier, Enchantment, AveragePrice]
            result = cursor.fetchone()
            
            # 將 result 第七個值導入進字串
            row.append(result[6])

        # 將 row 字串導入至 data | row = ['Tier4', .0價格, .1價格, .2價格, .3價格, .4價格]
        data.append(row)

    # 回傳 data | data = Tier4 ~ Tier8 的 row

    return data
