import pymysql as db
import json
class Data:
    def __init__(self):
        self.Left_Zone = "Data_packet1"
        self.Right_Zone = "Data_packet2"
        self.Front_Zone = "Data_packet3"
        self.path = "Data"
        
        return None

    def PacketJSON(self, data):
        try:
            filePathNameWExtL = './' + self.path + '/' + self.Left_Zone + '.json'
            filePathNameWExtR = './' + self.path + '/' + self.Right_Zone + '.json'
            filePathNameWExtF = './' + self.path + '/' + self.Front_Zone + '.json'
            with open(filePathNameWExtL, 'w') as fp:
                json.dump(data["Count_Lane_1"],fp)
            with open(filePathNameWExtR, 'w') as fp:
                json.dump(data["Count_Lane_2"],fp)
            with open(filePathNameWExtF, 'w') as fp:
                json.dump(data["Count_Lane_3"],fp)
        except :
            print("Error:501(Packet Not Addressed/Formed)")
        else:
            print("File is Found/Created")
        finally :
            print("ModuleExecuted:501")
        return None

    def CaptureMySQL(self, data):
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
            print("Error:502(Database Not Connected)")
            print(e)
        else:
            print("Database Connected")
        finally:
            print("ModuleExecuted:502")
            con.close()
        return None
