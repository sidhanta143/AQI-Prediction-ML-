from unittest import result

from flask import Flask, render_template, request
import pickle
import matplotlib.pyplot as plt
# from graph import plot_result

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("Home.html")

@app.route("/About")
def About():
    return render_template("About.html")



@app.route("/predict")
def prediction():
    return render_template("prediction.html")


@app.route("/visualization")
def visualization():
    return render_template("Visualization.html")

@app.route("/predict", methods=["POST"])
def predict():

    pm25 = float(request.form["pm25"])
    pm10 = float(request.form["pm10"])
    no2  = float(request.form["no2"])
    so2  = float(request.form["so2"])
    co   = float(request.form["co"])
    o3   = float(request.form["o3"])

    # Prediction
    Prediction = model.predict([[pm25, pm10, no2, so2, co, o3]])

    result = round(Prediction[0], 2)

    return render_template("prediction.html", Prediction=result)






if __name__ == "__main__":
    app.run(debug=True)

    







