from config import connection

def resource_price_search(Category):

    num = int(Category[0]) -1

    cursor = connection.cursor()

    Resource_name = ["Cloth", "Leather", "MetalBar", "Planks"]

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
    for i in range(5):
            
        row = []

        Tier = "Tier" + str(i + 4)
        row.append(Tier)
        for j in range(5):
            
            params = (Resource_name[num], i + 4, j)

            cursor.execute(query, params)

            result = cursor.fetchone()
            
            row.append(result[6])

        data.append(row)

    return data

resource_price_search("1_布料")