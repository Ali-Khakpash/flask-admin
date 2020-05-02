# -*- coding: utf-8 -*-
'''
    REST_API_Client.rest
    -------------------------
    The REST class.
'''

import requests
from flask import json, jsonify
from .config import BASE_URL



class REST():

    def __init__(self):
        self.url = BASE_URL

    def post(self, endpoint, data, header):
        req = requests.post(self.url + endpoint, json=data)
        dics = json.loads(req.text)
        dics["stat_code"] = req.status_code
        return dics


    def register(self, endpoint, data):
         res = requests.post(self.url + endpoint, json=data)
         #dics = json.loads(req.text)
         #dics["stat_code"] = req.status_code

         #return res.json()
         response = res.json()
         response['status_code'] = res.status_code
         return response



