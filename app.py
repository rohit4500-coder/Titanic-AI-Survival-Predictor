from flask import Flask, request, render_template
import pickle
import numpy as np


app = Flask(__name__)


# Load trained Titanic model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Get values from form

        pclass = int(request.form["Pclass"])

        sex = int(request.form["Sex"])

        age = float(request.form["Age"])

        sibsp = int(request.form["SibSp"])

        parch = int(request.form["Parch"])

        fare = float(request.form["Fare"])

        embarked = int(request.form["Embarked"])


        # Arrange features exactly as used during training

        features = np.array([[
            pclass,
            sex,
            age,
            sibsp,
            parch,
            fare,
            embarked
        ]])


        # Make prediction

        prediction = model.predict(features)


        # Get survival probability

        probability = model.predict_proba(features)[0][1] * 100


        # Convert result

        if prediction[0] == 1:
            output = "Passenger Survived"
        else:
            output = "Passenger Did Not Survive"


        return render_template(
            "index.html",
            prediction_text=f"{output} | Survival Probability: {probability:.2f}%"
        )


    except Exception as e:

        return render_template(
            "index.html",
            prediction_text=f"Error: {str(e)}"
        )


if __name__ == "__main__":
    app.run(debug=True)