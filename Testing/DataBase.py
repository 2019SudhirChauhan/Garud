import pymysql as db

def DataBaseSave(data):
    con = db.connect(host="localhost", user="root",
                         password="", db="garud",
                         charset='utf8mb4',cursorclass=db.cursors.DictCursor)
    try:
        cur = con.cursor()
        sql = "INSERT INTO `live_traffic_data`( `Day` , `Hour` , `Min` , \
            `Count_Lane_1` , `Count_Lane_2` , \
            `Count_Lane_3` , `Count_Lane_4` )\
            VALUES (%d,%d,%d,%d,%d,%d,%d)"% \
            (data[],data[],data[],data[],data[],data[],data[])
        cur.execute(sql)
        con.commit()
    except con.Error as e:
        print("Error:505(Database Not Connected)")
        print(e)
    else:
        print("Database Connected")
    finally:
        print("Operation is done:-)")
        con.close()
