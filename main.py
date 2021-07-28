import numpy as np
import requests
import time
import matplotlib as plot
import seaborn as sb

"""
个人股票投资分析，指标为北向资金动态，分析北向趋势，针对个股进行投资建议。
1、数据源：港交所披露易：https://sc.hkexnews.hk/TuniS/www.hkexnews.hk/index_c.htm
2、主要指标：上一日
3、形成策略：
"""

class scopy():

    pass

class Data:
    __slots__ = ('date', 'code', 'num', 'percent') #日期，股票代码，股票名，当日结算后持股数量和占比
    @property



    def putdata(self):
        pass

    def getnum(self, code, date):
        pass

    def plotdata(self, code, model="日"):
        if model=="日":
            pass
        elif model=="周":
            pass
        elif model=="月":
            pass
        pass
    pass

if __name__ == '__main__':
    Newdata = Data()


    pass
