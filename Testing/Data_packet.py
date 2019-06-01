from datetime import datetime as time
import json
import csv
import pymysql as db

#Live DataSaving;
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
            (data['Day'],data['Hours'],data['Min'],data['Count_Lane_1'],
             data['Count_Lane_2'],data['Count_Lane_3'],data['Count_Lane_4'])
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


#Creating datapacket in terms of the json;
def writeTOJSONFile(path, DataL, DataR, DataF, data):
    filePathNameWExtL = './' + path + '/' + DataL + '.json'
    filePathNameWExtR = './' + path + '/' + DataR + '.json'
    filePathNameWExtF = './' + path + '/' + DataF + '.json'
    with open(filePathNameWExtL, 'w') as fp:
        json.dump(data["Count_Lane_1"],fp)
    with open(filePathNameWExtR, 'w') as fp:
        json.dump(data["Count_Lane_2"],fp)
    with open(filePathNameWExtF, 'w') as fp:
        json.dump(data["Count_Lane_3"],fp)

curr = time.now()
Day = curr.weekday()+1
Hours = ((curr.hour+3)%12)+1
Min = (curr.minute//5)+1
print("Day : %d, Hours : %d, Min : %d."%(Day, Hours, Min))

data = {'Day' : Day,
        'Hours' : Hours,
        'Min' : Min,
        'Count_Lane_1' : 5,
        'Count_Lane_2' : 4,
        'Count_Lane_3' : 8,
        'Count_Lane_4' : 10 }

Left_Zone = "Data_packet1"
Right_Zone = "Data_packet2"
Front_Zone = "Data_packet3"

path = "Data"

writeTOJSONFile(path, Left_Zone, Right_Zone, Front_Zone, data)
#DataBaseSave(data)
print("Done :%d"%(555))
