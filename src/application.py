from flask import Flask,request,jsonify,render_template
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIR, 'models', 'LinearRegression.pkl'), 'rb') as f:
    model = pickle.load(f)

with open(os.path.join(BASE_DIR, 'models', 'scaler.pkl'), 'rb') as f:
    scaler = pickle.load(f)

application=Flask(__name__)
app = application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        Temperature = float(request.form['Temperature'])
        RH          = float(request.form['RH'])
        Ws          = float(request.form['Ws'])
        Rain        = float(request.form['Rain'])
        FFMC        = float(request.form['FFMC'])
        DMC         = float(request.form['DMC'])
        DC          = float(request.form['DC'])
        ISI         = float(request.form['ISI'])
        BUI         = float(request.form['BUI'])
        Classes     = float(request.form['Classes'])
        region      = float(request.form['region'])


        input_data = [[Temperature,RH,Ws,Rain,FFMC,DMC,DC,ISI,BUI,Classes,region]]
        scaled_input = scaler.transform(input_data)
        prediction = model.predict(scaled_input)[0]
        return render_template('home.html',prediction=prediction)
    else:
        return render_template('home.html')

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)