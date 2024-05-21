# -*- coding: utf-8 -*-
"""
Created on Tue May  4 19:26:32 2021

@author: Majoju Krishna Sai Prahlad
"""

from flask import Flask, jsonify, render_template, request
import numpy as np
import pickle
app = Flask(__name__)
model = pickle.load(open('chronic_k_d.pkl', 'rb'))
# l=[0.75,	0.0,	0.012712,	0.768707,	0.666667,	0.0]
# a=np.array(l)
# print(a.shape)
# pred=(model.predict([[a]]))


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    if request.method == 'POST':

        int_features = [float(x) for x in request.form.values()]
        final_features = [np.array(int_features)]
        prediction = model.predict([final_features])
        output = ""
        if(prediction == 0):
            output = ("Not a Chronic")
        else:
            output = ("Chronic")

    #output = round(prediction[0], 2)

        return render_template('index.html', prediction_text='It is {} a Kidney Disease Presence'.format(output))
    return None
# =============================================================================
#
# @app.route('/predict_api',methods=['POST'])
# def predict_api():
#     '''
#     For direct API calls trought request
#     '''
#     data = request.get_json(force=True)
#     prediction = model.predict([np.array(list(data.values()))])
#
#     output1=""
#     if(prediction==0):
#         output1=("Not a Chronic")
#     else:
#         output1=("Chronic")
#     return jsonify(output1)
# =============================================================================


if __name__ == "__main__":
    app.run(debug=True)
