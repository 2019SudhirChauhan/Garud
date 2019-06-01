import Model1
import Model2
import Model3
import Model4

##test = Model1.ML_Model1()
test1 = Model2.ML_Model1()
test2 = Model3.ML_Model1()
test3 = Model4.ML_Model1()

print(Model1.ML_Model1().Load_Model_Predict([1,1,1]))
print(test1.Load_Model_Predict([1,1,7]))
print(test2.Load_Model_Predict([1,3,12]))
print(test3.Load_Model_Predict([1,7,10]))
