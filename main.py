# -*- coding: utf-8 -*-

import dao
import beans
from network import Network
import json
import matplotlib.pyplot as plt
import math

import pandas as pd
import numpy as np
from datetime import datetime
import talib 
import json
import os

#获取股票列表
def pull_stock_from_tushare(network:Network, max:int):
    stocks = []
    stock_basics = network.stock_basic_api()
    if stock_basics["code"] == 0:
        raw_data = stock_basics["data"]["items"]
        
        for item in raw_data:
            if max == 0:
                break
            max = max - 1
            stocks.append(beans.Stock(max, item[0], item[1], item[2], item[3], item[4]))
    
    return stocks

#获取指定股票名的历史记录
def pull_daily_trade_from_tushare(network:Network, stocks:list[beans.Stock], start_date:str, end_date:str):
    daily_trades = []
    for stock in stocks:
        trades_json = network.daily_basic_api(stock.code, start_date, end_date)
        if trades_json["code"] == 0:
            raw_data = trades_json["data"]["items"]
            for item in raw_data:
                daily_trades.append(beans.DailyTrade(0, item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13], item[14], item[15], item[16], item[17]))
    return daily_trades

#存储每日基本交易数据
def save_daily_trade_date(data:pd.DataFrame, name:str):
    folder_path = "../data/" + name
    save_path = os.path.join(folder_path, name + ".csv")
    
    if os.path.exists(folder_path) == False:
        os.makedirs(folder_path)
    if os.path.exists(save_path):
        os.remove(save_path)
    data.to_csv(save_path)

#更新每日基本交易数据
def refresh_daily_trade_data(network:Network, start:str, end:str):
    stocks = pull_stock_from_tushare(network, 20)

    for stock in stocks:    
        if stock.name.startswith("*"):
            continue
        trades = pull_daily_trade_from_tushare(network, [stock], start, end)
        
        data = []
        dates = []
        for trade in trades:
            dates.append(datetime.strptime(str(trade.trade_date), "%Y%m%d"))
            data.append(trade.to_list())
        
        pd_data = pd.DataFrame(data, columns=("id" , "code" , "trade_date" , "close", "turnover_rate" , "turnover_rate_f" , "volume_ratio" , "pe" , "pe_ttm" , "pb" , "ps" , "ps_ttm" , "dv_ratio" , "dv_ttm" , "total_share" , "float_share" , "free_share" , "total_mv" , "circ_mv"), index=dates)
        save_daily_trade_date(pd_data, stock.name)




#依据csv数据生成各项量化指标
def analyze_daily_trade():
    path = "../data"
    stock_folder_list = os.listdir(path)
    for stock_folder in stock_folder_list:
        folder_path = os.path.join(path, stock_folder)
        csv_path = os.path.join(folder_path, stock_folder + ".csv")
        data = pd.read_csv(csv_path)
        
        #生成价格变化图
        ts =pd.Series(data["close"].to_numpy(), index=data.index)
        ts.plot()
        plt.savefig(os.path.join(folder_path, stock_folder + ".png"))
        plt.close()
        
        #生成其他技术指标


#config = json.load(open("./config.json"))
#start_date = "20220101"
#end_date = "20220930"

#network = Network(config["url"], config["token"])
#refresh_daily_trade_data(network, start_date, end_date)
analyze_daily_trade()

'''


ts =pd.Series(data["close"].to_numpy(), index=data.index)
ts.plot()

close = data["close"].to_numpy()
sma = talib.SMA(close)
print(sma)
'''

print("over")



'''
#历史遗留代码


def pull_daily_from_tushare(stocks:list[beans.Stock], start_date:str, end_date:str):
    daily = []
    for stock in stocks:
        trades_json = network.daily_api(stock.code, start_date, end_date)
        if trades_json["code"] == 0:
            raw_data = trades_json["data"]["items"]
            for item in raw_data:
                daily.append(beans.Daily(0, item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10]))
    return daily

def calc_average(xlist:list[float]):
    average = 0.0;
    for x in xlist:
        average += x;
    
    return average/len(xlist)

def calc_variance(xlist:list[float]):
    average = calc_average(xlist)
    variance = 0.0
    
    for x in xlist:
        variance += (x - average) * (x-average)
    return variance

def calc_cvariance(xlist:list[float], ylist:list[float]):
    x_average = calc_average(xlist)
    y_average = calc_average(ylist)
    
    cov = 0.0
    for i in range(len(xlist)):
        cov += (xlist[i] - x_average) * (ylist[i] - y_average)
    
    return cov

def calc_relative(xlist:list[float], ylist:list[float]):

#dao.init()
#stocks = pull_stock_from_tushare(20)
#stocks = dao.select_all_stock()
#trades = pull_daily_trade_from_tushare(stocks, "20220101", "20220615")
#daily = pull_daily_from_tushare(stocks, "20220101", "20220615")
#for trade in daily:
    #print(trade.to_string())
#dao.insert_stock_list(stocks)
#dao.insert_daily_trade_list(trades)
#dao.insert_daily_list(daily)
#trades = dao.select_daily_trade_by_code("000010.SZ")
#for trade in trades:
#    print(trade.to_string())
'''