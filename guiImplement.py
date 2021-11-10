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

    def create_button_by_stock_name_list(self, stockDataBase):
        for stockName in stockDataBase.get_dataDict():
            self.create_button(stockName)

    def create_button(self, stockName):
        tmpButton = tk.Button(self._buttonFrame, 
                              text = stockName, 
                              command = lambda : self.plot_cur_data()
                             )
        tmpButton.grid()


    def plot_cur_data(self, timeList, priceList):

        fig = plt.figure()
        axis1 = fig.add_subplot(111)
        axis1.plot(timeList, priceList, '*-b')

        for item in plotTargetFrame.winfo_children():
            item.destroy()

        canvas = FigureCanvasTkAgg(fig, master=plotTargetFrame)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row = 0, column = 0)
        plotTargetFrame.rowconfigure(index = 0, weight = 1)
        plotTargetFrame.columnconfigure(index = 0, weight =1)

    def create_button(self, buttonTargetFrame, plotTargetFrame):
        for stockInd in self._dataDict:
            self._dataDict[stockInd].create_button(buttonTargetFrame, plotTargetFrame)