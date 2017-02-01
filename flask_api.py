# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 11:50:35 2016

@author: hduser
"""

import numpy as np
from flask import Flask, abort, jsonify, request
import cPickle as pickle

my_random_forest = pickle.load(open("iris_rfc_pkl", "rb"))

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    predict_request = [data['sl'],data['sw'],data['pl'],data['pw']]
    predict_request = np.array(predict_request)
    y_hat = my_random_forest.predict(predict_request)
    output = [y_hat[0]]
    return jsonify(results=output)
    
if __name__ == '__main__':
    app.run(port=9000, debug=True)