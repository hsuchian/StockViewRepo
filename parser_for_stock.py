import requests
import tkinter as tk
import json

# Global definition
sourceUrl = "https://mis.twse.com.tw/stock/api/getStockInfo.jsp"
monitorStock = ['2330', '2454', '0050', '0056', '00878']

def get_data_from_server():
    data = {'ex_ch': '|'.join(['tse_{}.tw'.format(stockInd) for stockInd in monitorStock]), 'json': '1'}

    res = requests.get(sourceUrl, params = data)
    res = (res.json())['msgArray']
    for stockInfo in res:
        print("{0:8.4f}  {1:s}".format(float(stockInfo['z']), stockInfo['n']))



# The name will be file name parser_for_stock if this file was imported by
# other file, so the below code will not be executed
# The name will be __main__ if this file was exectued directly
if __name__ == '__main__':    
    # get_data_from_server()
    window = tk.Tk()
    window.title('Stock View')
    window.geometry('800x600')
    window.mainloop()