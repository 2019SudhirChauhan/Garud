from datetime import datetime as t

class time:
    def __init__(self):
        return None
    
    def getTime(self):
        curr = t.now()
        Day = curr.weekday()+1
        Hours = ((curr.hour+3)%12)+1
        Min = (curr.minute//5)+1
        return Day, Hours, Min
    
    def getTimeByStr(self, string):
        curr = t.strptime(string, '%Y-%m-%d %H:%M:%S')
        Day = curr.weekday()+1
        Hours = ((curr.hour+3)%12)+1
        Min = (curr.minute//5)+1
        return Day, Hours, Min
