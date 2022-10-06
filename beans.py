# -*- coding: utf-8 -*-

class Stock:
    id = 0
    code = ""
    symbol = ""
    name = ""
    area = ""
    industry = ""
    
    def __init__(self, id, code, symbol, name, area, industry):
        self.id = id
        self.code = code
        self.symbol = symbol
        self.name = name
        self.area = area
        self.industry = industry
        
    def to_string(self):
        return "Stock:[" + str(self.id) + " , " + self.code + " , " + self.symbol + " , " + self.name + " , " + self.area + " , " + self.industry + "]"

class Daily:
    id = 0;
    ts_code = ""
    trade_date = ""
    open = 0.0;
    high = 0.0;
    low  = 0.0;
    close = 0.0;
    pre_close = 0.0;
    change = 0.0;
    pct_chg = 0.0;
    vol = 0.0;
    amount = 0.0;
    
    def __init__(self, id, ts_code, trade_date, open, high, low, close, pre_close, change, pct_chg, vol, amount):
        self.id = id
        self.ts_code = ts_code
        self.trade_date = trade_date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.pre_close = pre_close
        self.change = change
        self.pct_chg = pct_chg
        self.vol = vol
        self.amount = amount
    
    def to_string(self):
        return "daily:[id:" + str(self.id) + " , "+ str(self.ts_code) + " , "+ self.trade_date + " , "+ str(self.open) + " , "+ str(self.high) + " , "+ str(self.low) + " , "+ str(self.close) + " , "+ str(self.pre_close) + " , "+ str(self.change) + " , "+ str(self.pct_chg) + " , "+ str(self.vol) + " , "+ str(self.amount) +"]"
        
        
class DailyTrade:
    id = 0
    ts_code = ""
    trade_date = ""
    close = 0.0
    turnover_rate = 0.0
    turnover_rate_f = 0.0
    volume_ratio = 0.0
    pe = 0.0
    pe_ttm = 0.0
    pb = 0.0
    ps = 0.0
    ps_ttm = 0.0
    dv_ratio = 0.0
    dv_ttm = 0.0
    total_share = 0.0
    float_share = 0.0
    free_share = 0.0
    total_mv = 0.0
    circ_mv = 0.0
    
    def __init__(self, id, ts_code,trade_date,close,turnover_rate,turnover_rate_f,volume_ratio,pe,pe_ttm,pb,ps,ps_ttm,dv_ratio,dv_ttm,total_share,float_share,free_share,total_mv,circ_mv):
       self.id = id
       self.ts_code = ts_code
       self.trade_date = trade_date
       self.close = close
       self.turnover_rate = turnover_rate
       self.turnover_rate_f = turnover_rate_f
       self.volume_ratio = volume_ratio
       self.pe = pe
       self.pe_ttm = pe_ttm
       self.pb = pb
       self.ps = ps
       self.ps_ttm = ps_ttm
       self.dv_ratio = dv_ratio
       self.dv_ttm = dv_ttm
       self.total_share = total_share
       self.float_share = float_share
       self.total_mv = total_mv
       self.circ_mv = circ_mv
       self.free_share = free_share
      
    def to_string(self):
        return "DailyTrade:[id" + str(self.id) + " , "+ str(self.ts_code) + " , "+ self.trade_date + " , "+ str(self.close) + " , "+ str(self.turnover_rate) + " , "+ str(self.turnover_rate_f) + " , "+ str(self.volume_ratio) + " , "+ str(self.pe) + " , "+ str(self.pe_ttm) + " , "+ str(self.pb) + " , "+ str(self.ps) + " , "+ str(self.ps_ttm) + " , "+ str(self.dv_ratio) + " , "+ str(self.dv_ttm) + " , "+ str(self.total_share) + " , "+ str(self.float_share) + " , "+ str(self.free_share) + " , "+ str(self.total_mv) + " , "+ str(self.circ_mv) + "]"
    
    def to_list(self):
        return [self.id, self.ts_code , self.trade_date , self.close  ,  self.turnover_rate , self.turnover_rate_f  , self.volume_ratio , self.pe , self.pe_ttm , self.pb , self.ps , self.ps_ttm , self.dv_ratio , self.dv_ttm , self.total_share , self.float_share , self.free_share , self.total_mv , self.circ_mv]