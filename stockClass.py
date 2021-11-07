from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import requests
import tkinter as tk



class stockInfo:
    def __init__(self, stockInd):
        self._priceList = list()
        self._timeList = list()
        self._stockQueryStr = 'tse_{}.tw'.format(stockInd)
        self._stockInd = stockInd
        self._name = None

    def set_name(self, name):
        self._name = name
    
    def get_name(self):
        return self._name

    def add_price(self, price, time):
        # if no current data, use starting price to replace 
        if price == '-':
            price = None
        
        self._priceList.append(float(price))
        self._timeList.append(time)

    def plot_cur_data(self, plotTargetFrame):
        fig = plt.figure()
        axis1 = fig.add_subplot(111)
        axis1.plot(range(1,6), self._priceList)
        
        for item in plotTargetFrame.winfo_children():
            item.destroy()

        canvas = FigureCanvasTkAgg(fig, master=plotTargetFrame)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row = 0, column = 0)
        plotTargetFrame.rowconfigure(index = 0, weight = 1)
        plotTargetFrame.columnconfigure(index = 0, weight =1)

    
    def create_button(self, buttonTargetFrame, plotTargetFrame):
        tmpButton = tk.Button(buttonTargetFrame, 
                              text = self._name, 
                              command = lambda : self.plot_cur_data(plotTargetFrame)
                              )
        tmpButton.grid()
    
    def get_ind(self):
        return self._stockInd

    def get_query_str(self):
        return self._stockQueryStr


class dataBase:
    def __init__(self, sourceUrl):
        self._dataDict = dict()
        self._sourceUrl = sourceUrl

    def add_stock_member(self, sIndList):
        for sInd in sIndList:
            self._dataDict[sInd] = stockInfo(sInd)

    def get_dataDict(self):
        return self._dataDict

    def get_data_from_server(self):   #dataBase should be a dictionary
    
        #data = {'ex_ch': '|'.join(['tse_{}.tw'.format(stockInd) for stockInd in monitorStock]), 'json': '1'}
        data = {'ex_ch': '|'.join([self._dataDict[sInd].get_query_str() for sInd in self._dataDict]), 'json': '1'}

        res = requests.get(self._sourceUrl, params = data)
        res = (res.json())['msgArray']
        
        for sInfoServer in res:
            sPrice = sInfoServer['z']
            sInd = sInfoServer['c']
            sTime = sInfoServer['t']
            
            self._dataDict[sInd].add_price(sPrice, sTime)
            #print("{0:8.4f}  {1:s}".format(float(stockInfo['z']), stockInfo['n']))      

    def set_name_for_stock(self):
        data = {'ex_ch': '|'.join([self._dataDict[sInd].get_query_str() for sInd in self._dataDict]), 'json': '1'}

        res = requests.get(self._sourceUrl, params = data)
        res = (res.json())['msgArray']
        
        for sInfoServer in res:
            sName = sInfoServer['n']
            sInd = sInfoServer['c']
            self._dataDict[sInd].set_name(sName)

    def create_button(self, buttonTargetFrame, plotTargetFrame):
        for stockInd in self._dataDict:
            self._dataDict[stockInd].create_button(buttonTargetFrame, plotTargetFrame)

if __name__ == '__main__':
    print('Cannot execute this file directly')
    exit(-1)