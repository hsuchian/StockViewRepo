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

        plotFrame.grid(row = 0, column = 0)
        buttonFrame.grid(row = 0, column = 1)

        window.rowconfigure(index = 0, weight = 2)
        window.rowconfigure(index = 1, weight = 1)

        window.columnconfigure(index = 0, weight = 1)  
        window.columnconfigure(index = 1, weight = 1)

        window.bind("<Configure>", self.resize_function)

        # class member
        self._window = window
        self._plotFrame = plotFrame
        self._buttonFrame = buttonFrame
        self._currentStock = None

    def resize_function(newWidth, newLen):    # resize function when
        #print('Hello' + str(newWidth) + ' ' + str(newLen))
        x = 10

    def create_button_by_stock_name_list(self, stockDataBase):  # mutable object type, call by reference for stockDataBase
        
        sDataDict = stockDataBase.get_dataDict()
        for stockInd in sDataDict:
            sData = sDataDict[stockInd]
            self.create_button(sData)

    def create_button(self, sData):   # already create local variable for sData, so no problem using lambda
        tmpButton = tk.Button(self._buttonFrame, 
                              text = sData.get_name(), 
                              command = lambda : self.button_action(sData)
                             )
        tmpButton.grid()

    def button_action(self, sData):
        self._currentStock = sData.get_ind_str()
        self.plot_data(sData)

    def plot_data(self, sData):

        timeList = sData.get_time_list() 
        priceList = sData.get_price_list()
        
        fig = plt.figure(figsize=(8,6))  # difined in inches
        axis1 = fig.add_subplot(111)
        axis1.plot(timeList, priceList, '*-b')

        for item in self._plotFrame.winfo_children():
            item.destroy()

        canvas = FigureCanvasTkAgg(fig, master=self._plotFrame)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row = 0, column = 0)
        
        # shoulde close the fig explicitly
        plt.close(fig)
    
        self._plotFrame.rowconfigure(index = 0, weight = 1)
        self._plotFrame.columnconfigure(index = 0, weight =1)

        plt.close()

    def init_cur_stock(self, sInd):
        self._currentStock = sInd

    def get_cur_stock_ind(self):
        return self._currentStock



if __name__ == '__main__':
    print('Cannot execute this file directly')
    exit(-1)




# ------------------- reference -------------------------------
# https://web.archive.org/web/20201111211515id_/https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm


'''

def start_update_5_sec(GUIMgr, TotalStockData):
    TotalStockData.get_data_from_server()
    sdataDict = TotalStockData.get_dataDict()

    curStockInd = GUIMgr.get_cur_stock_ind()
    GUIMgr.plot_data(sdataDict[curStockInd])
    GUIMgr._window.after(5000, start_update_5_sec, GUIMgr, TotalStockData)


'''