# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 12:57:27 2022

@author: blaine
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import talib


class Analyzer:
    data_path = "../data"
    
    def __init__(self, path:str):
        self.data_path = path
    
    #依据csv数据生成各项量化指标
    def analyze_daily_trade(self):
        stock_folder_list = os.listdir(self.data_path)
        for stock_folder in stock_folder_list:
            folder_path = os.path.join(self.data_path, stock_folder)
            csv_path = os.path.join(folder_path, stock_folder + ".csv")
            data = pd.read_csv(csv_path)
            
            self._generate_total_price_plt(data, folder_path, stock_folder)
            
            #生成其他技术指标
            self._generate_star(data, folder_path)
    
    #生成全局价格变化图
    def _generate_total_price_plt(self, data, folder_path, stock_name):
        save_path = os.path.join(folder_path, stock_name + ".png")
        
        close_ts =pd.Series(data["close"].to_numpy(), index=data.index)
        close_ts.plot()
        
        plt.savefig(save_path)
        plt.close()
        
    #生成晨曦之星
    def _generate_star(self, data, folder_path):
        save_path = os.path.join(folder_path, "sma.png")
        close = data["close"].to_numpy()
        sma = talib.SMA(close)
        upper, middle, lower = talib.BBANDS(close, matype=talib.MA_Type.T3)
        
        sma_ts =pd.Series(sma, index=data.index)
        sma_ts.plot()
        upper_ts =pd.Series(upper, index=data.index)
        upper_ts.plot()
        middle_ts =pd.Series(middle, index=data.index)
        middle_ts.plot()
        lower_ts =pd.Series(lower, index=data.index)
        lower_ts.plot()
        
        plt.savefig(save_path)
        plt.close()
        
        