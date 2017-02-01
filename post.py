# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 11:50:18 2016

@author: hduser
"""

import requests, json

url = "http://localhost:5000/api"
data = json.dumps({'sl':5.1,'sw':3.5,'pl':1.4,'pw':0.2})
r = requests.post(url,data)

print r.json()