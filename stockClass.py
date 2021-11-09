from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import requests
import tkinter as tk
import datetime 

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
        
        if price == '-':
            price = None
        else:
            price = float(price)
        
        now = datetime.datetime.now()
        timeStructTmp = datetime.datetime.strptime(time, "%H:%M:%S")
        timeStructTmp = timeStructTmp.replace(now.year, now.month, now.day)

        # add the time for 6 sec if the time fixed at 13:30, not a very good solution
        if self._timeList and timeStructTmp in self._timeList:
            timeStructTmp = self._timeList[-1] + datetime.timedelta(seconds = 5)

        self._priceList.append(price)
        self._timeList.append(timeStructTmp)

    def plot_cur_data(self, plotTargetFrame):

        fig = plt.figure()
        axis1 = fig.add_subplot(111)
        axis1.plot(self._timeList, self._priceList, '*-b')

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
                              command = lambda : self.plot_cur_data(plotTargetFrame),
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
        self._curStockInd = None

    def gen_fake_data(self):
        for sInd in self._dataDict:
            self._dataDict[sInd] = stockInfo(sInd)
            self._dataDict[sInd]._priceList = [11 + int(sInd), 5 + int(sInd), 7 + int(sInd), 9 + int(sInd), 8 + int(sInd)]
            self._dataDict[sInd]._timeList = [11, 5, 7, 9, 8]
            self._dataDict[sInd]._name = sInd

    def add_stock_member(self, sIndList):
        for sInd in sIndList:
            self._dataDict[sInd] = stockInfo(sInd)
        if sIndList:   # check if list is not empty
            self._curStockInd = sIndList[0]

    def get_dataDict(self):
        return self._dataDict

    def get_data_from_server(self, GUIMgr):   #dataBase should be a dictionary
        
        #data = {'ex_ch': '|'.join(['tse_{}.tw'.format(stockInd) for stockInd in monitorStock]), 'json': '1'}
        data = {'ex_ch': '|'.join([self._dataDict[sInd].get_query_str() for sInd in self._dataDict]), 'json': '1'}

        res = requests.get(self._sourceUrl, params = data)
        res = (res.json())['msgArray']
        
        sTimetmp = None
        for sInfoServer in res:
            sPrice = sInfoServer['z']
            sInd = sInfoServer['c']
            sTimetmp = sTime = sInfoServer['t']
            
            self._dataDict[sInd].add_price(sPrice, sTime)
            #print("{0:8.4f}  {1:s}".format(float(stockInfo['z']), stockInfo['n']))     
        
        print("Update data from server " + sTime)
        GUIMgr._window.after(5000, self.get_data_from_server, GUIMgr)
        # update the figure for the current figure
        self._dataDict[self._curStockInd].plot_cur_data(GUIMgr._plotFrame)


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