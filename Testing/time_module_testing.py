from datetime import datetime as time

curr = time.now()
#For Machine Learning
#Get the week in current
print("Week : %d"%(curr.weekday()+1))

#Get the time
print("Time : %d"%((curr.minute//5)+1))

#Get the hour
print("Hours : %d"%(((curr.hour+3)%12)+1))

def writeToCSVFile(path, DataL, DataR, DataF, data):
    filePathNameWExtL = './' + path + '/' + DataL + '.csv'
    filePathNameWExtR = './' + path + '/' + DataR + '.csv'
    filePathNameWExtF = './' + path + '/' + DataF + '.csv'
    with open(filePathNameWExt, 'a', newline='') as csvfile:
        fieldnames = ['Day','Hours','Min','Count_Lane_1', 'Count_Lane_2','Count_Lane_3', 'Count_Lane_4']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(data)
