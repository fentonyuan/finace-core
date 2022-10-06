# -*- coding: utf-8 -*-

import sqlite3
import beans


def __create_stock_table(cursor):
    cursor.execute('''
                   CREATE TABLE STOCK(
                       id INT PRIMARYKEY NOT NULL,
                       code CHAR(10) NOT NULL,
                       symbol CHAR(10),
                       name CHAR(50),
                       area CHAR(50),
                       industry CHAR(50)
                       )
                   ''')

def __create_daily_trade(cursor):
    cursor.execute('''
                   CREATE TABLE DAILYTRADE(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       code CHAR(10) NOT NULL,
                       date CHAR(10) NOT NULL,
                       close FLOAT,
                       turnover_rate FLOAT,
                       turnover_rate_f FLOAT,
                       volume_ratio FLOAT,
                       pe FLOAT,
                       pe_ttm FLOAT,
                       pb FLOAT,
                       ps FLOAT,
                       ps_ttm FLOAT,
                       dv_ratio FLOAT,
                       dv_ttm FLOAT,
                       total_share FLOAT,
                       float_share FLOAT,
                       free_share FLOAT,
                       total_mv FLOAT,
                       circ_mv FLOAT
                       )
                   ''')

def __create_daily(cursor):
    cursor.execute(''' 
                   CREATE TABLE DAILY(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       code CHAR(10) NOT NULL,
                       date CHAR(10) NOT NULL,
                       open FLOAT,
                       high FLOAT,
                       low FLOAT,
                       close FLOAT,
                       pre_close FLOAT,
                       change FLOAT,
                       pct_chg FLOAT,
                       vol FLOAT,
                       amount FLOAT
                       )
                   
                   ''')

def __init_table(cursor):
    #__create_stock_table(cursor)
    #__create_daily_trade(cursor)
    __create_daily(cursor)
    
    
def init():
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    
    __init_table(cursor)
    
    conn.commit()
    conn.close()

def insert_stock(stock:beans.Stock):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    
    cursor.execute('''
                   INSERT INTO STOCK(code, symbol, name, area, industry)
                   VALUES (?, ?, ?, ?, ?, ?)
                   ''', (stock.id, stock.code, stock.symbol, stock.name, stock.area, stock.industry))
    
    conn.commit()
    conn.close()

def insert_daily_trade(trade:beans.DailyTrade):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    
    cursor.execute('''
                   INSERT INTO DAILYTRADE(code, date , close , turnover_rate , 
                                     turnover_rate_f , volume_ratio , pe , pe_ttm , 
                                     pb , ps , ps_ttm , dv_ratio , dv_ttm , 
                                     total_share , float_share , free_share , 
                                     total_mv , circ_mv)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                   ''', (trade.ts_code, trade.trade_date, trade.close, trade.turnover_rate, trade.turnover_rate_f, trade.volume_ratio, trade.pe, trade.pe_ttm, trade.pb, trade.ps, trade.ps_ttm, trade.dv_ratio, trade.dv_ttm, trade.total_share, trade.float_share, trade.free_share, trade.total_mv, trade.circ_mv))
    
    conn.commit()
    conn.close()
    
def insert_daily(trade:beans.Daily):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    
    cursor.execute('''
                   INSERT INTO DAILY(code, date , open , high , 
                                     low , close , pre_close , change , 
                                     pct_chg , vol , amount)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                   ''', (trade.ts_code, trade.trade_date, trade.open, trade.high, trade.low, trade.close, trade.pre_close, trade.change, trade.pct_chg, trade.vol, trade.amount))
    
    conn.commit()
    conn.close()

def insert_daily_list(trades:list[beans.Daily]):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    
    for trade in trades:
        cursor.execute('''
                       INSERT INTO DAILY(code, date , open , high , 
                                         low , close , pre_close , change , 
                                         pct_chg , vol , amount)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                       ''', (trade.ts_code, trade.trade_date, trade.open, trade.high, trade.low, trade.close, trade.pre_close, trade.change, trade.pct_chg, trade.vol, trade.amount))
    
    conn.commit()
    conn.close()
    
def insert_daily_trade_list(trades:list[beans.DailyTrade]):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    
    for trade in trades:
        cursor.execute('''
                       INSERT INTO DAILYTRADE(code, date , close , turnover_rate , 
                                         turnover_rate_f , volume_ratio , pe , pe_ttm , 
                                         pb , ps , ps_ttm , dv_ratio , dv_ttm , 
                                         total_share , float_share , free_share , 
                                         total_mv , circ_mv)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                       ''', (trade.ts_code, trade.trade_date, trade.close, trade.turnover_rate, trade.turnover_rate_f, trade.volume_ratio, trade.pe, trade.pe_ttm, trade.pb, trade.ps, trade.ps_ttm, trade.dv_ratio, trade.dv_ttm, trade.total_share, trade.float_share, trade.free_share, trade.total_mv, trade.circ_mv))
    
    conn.commit()
    conn.close()
    
def insert_stock_list(stocks:list[beans.Stock]):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    
    for stock in stocks:
        cursor.execute('''
                       INSERT INTO STOCK(id, code, symbol, name, area, industry)
                       VALUES (?, ?, ?, ?, ?, ?)
                       ''', (stock.id, stock.code, stock.symbol, stock.name, stock.area, stock.industry))
    
    conn.commit()
    conn.close()

def select_all_stock():
    stocks = []
    
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM STOCK")
    for raw in cursor:
        stock = beans.Stock(raw[0], raw[1], raw[2], raw[3], raw[4], raw[5])
        stocks.append(stock)
    
    conn.close()
    return stocks;

def select_daily_trade_by_code(code:str):
    trades = []
    
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM DAILYTRADE WHERE code='" + code + "'")
    for trade in cursor:
        trades.append(beans.DailyTrade(trade[0], trade[1], trade[2], trade[3], trade[4], trade[5], trade[6], trade[7], trade[8], trade[9], trade[10], trade[11], trade[12], trade[13], trade[14], trade[15], trade[16], trade[17], trade[18]))
    
    conn.close()
    return trades;

def select_daily_by_code(code:str):
    trades = []
    
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM DAILY WHERE code='" + code + "'")
    for trade in cursor:
        trades.append(beans.Daily(trade[0], trade[1], trade[2], trade[3], trade[4], trade[5], trade[6], trade[7], trade[8], trade[9], trade[10], trade[11]))
    
    conn.close()
    return trades;