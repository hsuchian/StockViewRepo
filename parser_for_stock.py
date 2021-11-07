# variable with camel case
# fucntion with '_'

#import stockClass
from stockClass import *
from guiImplement import *
import json
import time


# The name will be file name parser_for_stock if this file was imported by
# other file, so the below code will not be executed
# The name will be __main__ if this file was exectued directly
if __name__ == '__main__':
    # basic definition
    sourceUrl = "https://mis.twse.com.tw/stock/api/getStockInfo.jsp"
    monitorStock = ['2330', '2454', '0050', '0056', '00878']

    TotalStockData = dataBase(sourceUrl)    
    TotalStockData.add_stock_member(monitorStock)
    TotalStockData.set_name_for_stock()    

    for i in range(0, 5):
        print("Update data")
        TotalStockData.get_data_from_server()
        #time.sleep(1)

    GUIMgr = guiMgr()

    # add button
    #TotalStockData.create_button(GUIMgr._buttonFrame, GUIMgr._plotFrame)

    GUIMgr._window.mainloop()