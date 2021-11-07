import tkinter as tk


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
        self._window = window
        self._plotFrame = plotFrame
        self._buttonFrame = buttonFrame
