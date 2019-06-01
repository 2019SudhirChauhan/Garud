from flask import Flask, render_template, url_for, request
from Helper import Timer, DataFormation, DataCreate
from ML_Module import Model1, Model2, Model3, Model4
from DummyState import Object_Count, Previous_Count
from TrafficTime import Calculate_time
app = Flask(__name__)

app.config["SECRET_KEY"] = "6bd4f7b4328844903bb25da88207c1ad"

@app.route("/")
@app.route("/Home")
def home():
	Day, Hours, Min = Timer.time().getTime()
	cur_lane_value_pre = Model1.ML_Model1().Load_Model_Predict([Day, Hours, Min])
	left_lane_value_pre = Model2.ML_Model1().Load_Model_Predict([Day, Hours, Min])
	right_lane_value_pre = Model3.ML_Model1().Load_Model_Predict([Day, Hours, Min])
	front_lane_value_pre = Model4.ML_Model1().Load_Model_Predict([Day, Hours, Min])
	dataform = DataFormation.Data()
	Image_Rec_Count = [Object_Count.getCount(2)for _ in range(0,4)]
	Pre_sig_Count = [Previous_Count.GetCount(2)for _ in range(0,4)]
	data = DataCreate.Create(Day, Hours, Min, cur_lane_value_pre,left_lane_value_pre,
		right_lane_value_pre, front_lane_value_pre, Image_Rec_Count, Pre_sig_Count)
	dataform.PacketJSON(data)
	dataform.CaptureMySQL(data)
	timeData = Calculate_time.FromTime(data)
	print(timeData)
	return render_template("Home.html", posts=timeData)

@app.route("/About")
def about():
    return render_template("About.html")

@app.route("/Traffic_Prediction", methods=["GET", "POST"])
def Traffic_Prediction():
	if request.method == "POST":
		Date = request.form.get("Date")
		Time = request.form["Time"]
		print("Date and Time : {}".format(Date+" "+Time))
		#print("Time : {}".format(Time))
		Day, Hours, Min = Timer.time().getTimeByStr(Date+" "+Time)
		Lane1 = Model1.ML_Model1().Load_Model_Predict([Day, Hours, Min])
		Lane2 = Model2.ML_Model1().Load_Model_Predict([Day, Hours, Min])
		Lane3 = Model3.ML_Model1().Load_Model_Predict([Day, Hours, Min])
		Lane4 = Model4.ML_Model1().Load_Model_Predict([Day, Hours, Min])
		data = [{"Lane1" : Lane1, "Lane2" : Lane2, "Lane3" : Lane3, "Lane4" : Lane4}]
		return render_template("Count.html", posts=data)
	return render_template("Traffic_Prediction.html")

@app.route("/Futher_Updates")
def Futher_Updates():
	return render_template("Futher_Updates.html")

@app.route("/Login")
def Login():
	return render_template("index3.html")

if __name__ == '__main__':
	app.run(debug=True)