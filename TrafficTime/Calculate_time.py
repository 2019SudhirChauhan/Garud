def calculateTime(count):
    timeInSec = 30000
    try:
        timeInSec = int((3/2)*count)*10000
        return timeInSec
    except :
        print("Error:201(Time Not Calculated)")
    else:
        print("Time Calulated")
    finally :
        print("ModuleExecuted:201")

def FromTime(data):
    time = [{
            'Time_Lane1' :calculateTime(data['Count_Lane_1']),
            'Time_Lane2' :calculateTime(data['Count_Lane_2']),
            'Time_Lane3' :calculateTime(data['Count_Lane_3']),
            'Time_Lane4' :calculateTime(data['Count_Lane_4'])
        }]
    return time
