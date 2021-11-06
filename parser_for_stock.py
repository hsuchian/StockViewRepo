# variable with camel case
# fucntion with '_'

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import requests
import tkinter as tk
import json
import time

class stockInfo:
    def __init__(self, stockInd):
        self._priceList = list()
        self._timeList = list()
        self._stockQueryStr = 'tse_{}.tw'.format(stockInd)
        self._stockInd = stockInd

    def add_price(self, price, time):
        # if no current data, use starting price to replace 
        if price == '-':
            price = None
        
        self._priceList.append(float(price))
        self._timeList.append(time)

    def get_ind(self):
        return self._stockInd

    def get_query_str(self):
        return self._stockQueryStr

    def plot_cur_data(self, plotTarget):
        fig = plt.figure()
        axis1 = fig.add_subplot(111)
        axis1.plot(range(1,5), range(11, 15))

        canvas = FigureCanvasTkAgg(fig, master=plotTarget)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack() 

class dataBase:
    def __init__(self):
        self._dataDict = dict()

    def add_stock_member(self, sInfo):
        self._dataDict[sInfo.get_ind()] = sInfo
    

    def get_dataDict(self):
        return self._dataDict


    def get_data_from_server(self):   #dataBase should be a dictionary
    
        #data = {'ex_ch': '|'.join(['tse_{}.tw'.format(stockInd) for stockInd in monitorStock]), 'json': '1'}
        data = {'ex_ch': '|'.join([self._dataDict[sInd].get_query_str() for sInd in self._dataDict]), 'json': '1'}

        res = requests.get(sourceUrl, params = data)
        res = (res.json())['msgArray']
        
        for sInfoServer in res:
            sName = sInfoServer['n']
            sPrice = sInfoServer['z']
            sInd = sInfoServer['c']
            sTime = sInfoServer['t']
            
            self._dataDict[sInd].add_price(sPrice, sTime)
            #print("{0:8.4f}  {1:s}".format(float(stockInfo['z']), stockInfo['n']))      

        #for stockInfo in res:
        #    print("{0:8.4f}  {1:s}".format(float(stockInfo['z']), stockInfo['n']))



# The name will be file name parser_for_stock if this file was imported by
# other file, so the below code will not be executed
# The name will be __main__ if this file was exectued directly
if __name__ == '__main__':
    # basic definition
    sourceUrl = "https://mis.twse.com.tw/stock/api/getStockInfo.jsp"
    monitorStock = ['2330', '2454', '0050', '0056', '00878']

    TotalStockData = dataBase()    
    for stockInd in monitorStock:
        tmpStock = stockInfo(stockInd)
        TotalStockData.add_stock_member(tmpStock)
    
    # start getting raw data

    for i in range(0, 5):
        print("Update data")
        TotalStockData.get_data_from_server()
        #time.sleep(1)

    
    windowLen = 600
    windowWid = 800
    window = tk.Tk()
    window.title('Stock View')
    window.geometry(str(windowWid) + 'x' + str(windowLen))

    div_size = 200
    img_size = div_size * 2
    plotFrame = tk.Frame(window,  width=img_size , height=img_size , bg='white')
    div2 = tk.Frame(window,  width=div_size , height=div_size , bg='orange')
    div3 = tk.Frame(window,  width=div_size , height=div_size , bg='blue')

    plotFrame.grid(row = 0, column = 0, rowspan=2)
    div2.grid(row = 0, column = 1)
    div3.grid(row = 1, column = 1)

    for 

    TotalStockData._dataDict['2330'].plot_cur_data(plotFrame)

    window.mainloop()