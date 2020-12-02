import requests
import json
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from helper_functions import pickle_load, transformations


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    transformed = transformations(int_features)
    result = XGB.predict(transformed)[0]
    
    return render_template('home.html', prediction_text='Price should be {}'.format(result[3:]))


if __name__ == '__main__':
    XGB = pickle_load('./clf.pickle')
    app.run(debug=True, host='0.0.0.0')