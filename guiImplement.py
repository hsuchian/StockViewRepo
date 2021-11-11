import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class guiMgr:
    def __init__(self, ):

        window = tk.Tk()
        window.title('Stock View')
        w, h = window.winfo_screenwidth(), window.winfo_screenheight()
        window.geometry(str(w) + 'x' + str(h))
        
        plotFrame = tk.Frame(window, width=w*2/3 , height=h, bg='white')
        #plotFrame = tk.Frame(window, bg='white')
        buttonFrame = tk.Frame(window, width=w*1/3 , height=h, bg='green')
        #div3 = tk.Frame(window,  width=div_size , height=div_size , bg='blue')

        plotFrame.grid(row = 0, column = 0,)
        buttonFrame.grid(row = 0, column = 1)

        window.rowconfigure(index = 0, weight = 2)
        window.rowconfigure(index = 1, weight = 1)
        window.columnconfigure(index = 0, weight = 1)  
        window.columnconfigure(index = 1, weight = 1)

        # class member
        self._window = window
        self._plotFrame = plotFrame
        self._buttonFrame = buttonFrame
        self._currentStock = None

    def init_cur_stock(self, sInd):
        self._currentStock = sInd

    def get_cur_stock_ind(self):
        return self._currentStock

    def create_button_by_stock_name_list(self, stockDataBase):
        
        sDataDict = stockDataBase.get_dataDict()
        for stockInd in sDataDict:
            sData = sDataDict[stockInd]
            #print(sData.get_name(), sData.get_price_list(), sData.get_time_list())
            self.create_button(sData.get_name(), sData.get_price_list(), sData.get_time_list())

    def create_button(self, stockName, stockPriceList, stockTimeList):
        tmpButton = tk.Button(self._buttonFrame, 
                              text = stockName, 
                              command = lambda : self.plot_data(stockTimeList, stockPriceList)
                             )
        tmpButton.grid()


    def plot_data(self, timeList, priceList):

        fig = plt.figure()
        axis1 = fig.add_subplot(111)
        axis1.plot(timeList, priceList, '*-b')

        for item in self._plotFrame.winfo_children():
            item.destroy()

        canvas = FigureCanvasTkAgg(fig, master=self._plotFrame)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row = 0, column = 0)
        self._plotFrame.rowconfigure(index = 0, weight = 1)
        self._plotFrame.columnconfigure(index = 0, weight =1)


if __name__ == '__main__':
    print('Cannot execute this file directly')
    exit(-1)