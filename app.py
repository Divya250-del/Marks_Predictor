from operator import index
import numpy as np
import pandas as pd
from flask import Flask,request,render_template
import joblib


app=Flask(__name__)
model=joblib.load("predictor.pkl")
df=pd.DataFrame()

@app.route('/')
def home():
    return render_template('index.html')
    

@app.route('/predict',methods=["POST", "GET"])
def predict():

    if request.method == "POST":
     #global df
     data1 = [] 
     data = request.form["mark"]
     print(f"Data = {data}")
     if int(data) >= 1 and int(data) <=24:
      data1.append(int(data))

      features = np.array(data1)

      output = model.predict( [features] )[0][0].round(2)
      if output <= 100:
       return render_template('index.html',prediction_text=f'You will get {output}% when you study {data} hours per day')
      else:
        return render_template('index.html',prediction_text = f'If you study {data} hours then You can get 100% Marks')
     else:
       return render_template('index.html',prediction_text = 'Please Enter hours between 1-24')

   


        

    

if __name__ == "__main__":
    app.run(debug=True)