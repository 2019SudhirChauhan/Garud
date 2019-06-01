import pickle
import warnings
warnings.filterwarnings("ignore")

class ML_Model1:
    def __init__(self):
        self.file_name = "RF_Model5.sav"
        self.clf = pickle.load(open("Random_Forest_Model/"+self.file_name, 'rb'))
        #df = pd.read_csv('Node1.csv')
        #self.le = LabelEncoder()
        #self.le.fit(df["Count Lane 1"])
        return None

    def Load_Model_Predict(self,arr):
        return int((self.clf.predict([arr])))
