import Object_Count, Previous_Count

val1 = Object_Count.getCount(2)
val2 = Previous_Count.GetCount(2)
val3 = [Object_Count.getCount(2)for _ in range(0,4)]
val4 = [Previous_Count.GetCount(2)for _ in range(0,4)]
print("Val1 :%d, Val2:%d"%(val1,val2))
print(val3)
print(val4)
