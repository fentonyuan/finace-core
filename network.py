# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 14:41:48 2022

@author: blaine
"""
import requests

class Network:
    url = "http://api.tushare.pro"
    token = ""
    
    def __init__(self, url, token):
        self.url = url
        self.token = token
    
    def stock_basic_api(self):
        params = '{"api_name":"stock_basic", "token":"' + self.token +'", "params":{"exchange":"", "list_status":""}}'
        encodeData = params.encode("utf-8")
    
        postRequest = requests.post(self.url, data=encodeData)
        if postRequest.status_code == 200:
            return postRequest.json()
        else:
            return ""
        
    def daily_basic_api(self, ts_code:str, start_date:str, end_date:str):    
        params = '{"api_name":"daily_basic", "token":"' + self.token +'", "params":{"ts_code":"' + ts_code + '", "start_date":"'+ start_date +'", "end_date":"' + end_date +'"}}'
        encodeData = params.encode("utf-8")
    
        postRequest = requests.post(self.url, data=encodeData)
        if postRequest.status_code == 200:
            return postRequest.json()
        else:
            return ""
    
    def daily_api(self, ts_code:str, start_date:str, end_date:str):
        params = '{"api_name":"daily", "token":"' + self.token +'", "params":{"ts_code":"' + ts_code + '", "start_date":"'+ start_date +'", "end_date":"' + end_date +'"}}'
        encodeData = params.encode("utf-8")
    
        postRequest = requests.post(self.url, data=encodeData)
        if postRequest.status_code == 200:
            return postRequest.json()
        else:
            return ""
