import random
def GetCount(minitus):
    if(minitus == 1):
        count = random.randint(5,15)
    elif(minitus == 2):
        count = random.randint(10,20)
    elif(minitus == 3):
        count = random.randint(15,25)
    elif(minitus == 4):
        count = random.randint(15,25)
    elif(minitus == 5):
        count = random.randint(20,30)
    elif(minitus == 6):
        count = random.randint(20,30)
    elif(minitus == 7):
        count = random.randint(25,35)
    elif(minitus == 8):
        count = random.randint(25,35)
    elif(minitus == 9):
        count = random.randint(30,40)
    elif(minitus == 10):
        count = random.randint(35,45)
    elif(minitus == 11):
        count = random.randint(35,50)
    else:
        count = random.randint(35,50)
    return count
    
