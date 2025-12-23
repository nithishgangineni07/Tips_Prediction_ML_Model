
import joblib #to load the trained model
import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS

#flask to create api end point

app = Flask(__name__) #create a flask app or create an api end point
CORS(app)

#load the traine dmodel
model = joblib.load('random_forest_model.pkl')

@app.route('/predict',methods=['POST'])

def predict():
    """api end point to get the data from the streamlit app and return the predicted tip  amount"""

    data = request.json ##get the data from the streamlit it app 
    # convert the data into a pandas dataframe

    input_df = pd.DataFrame([{
        'total_bill' : data['total_bill'],
        'sex' : data['sex'],
        'smoker' : data['smoker'],
        'day' : data['day'],
        'time' : data['time'],
        'size' : data['size'] # convert the data into data frame
    }])

    #make the prediction

    prediction = model.predict(input_df) #make the prediction
    return jsonify({'predicted_tip':float(prediction[0])}) #return the prediction to the streamlit

if __name__ == '__main__':
    app.run(debug = True) #run the app in debug mode