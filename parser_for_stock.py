# variable with camel case
# fucntion with '_'

#import stockClass
from stockClass import *
from guiImplement import *
import json
import time


def start_update_5_sec(GUImgr, TotalStockData):
    TotalStockData.get_data_from_server()
    sdataDict = TotalStockData.get_dataDict()
    curStockInd = GUIMgr.get_cur_stock_ind()
    GUIMgr.plot_data(sdataDict[curStockInd].get_time_list(), sdataDict[curStockInd].get_price_list())
    GUIMgr._window.after(5000, start_update_5_sec, GUIMgr, TotalStockData)


# The name will be file name parser_for_stock if this file was imported by
# other file, so the below code will not be executed
# The name will be __main__ if this file was exectued directly
if __name__ == '__main__':
    # basic definition
    sourceUrl = "https://mis.twse.com.tw/stock/api/getStockInfo.jsp"
    monitorStock = ['2330', '2454', '0050', '0056', '00878']

    internet = 1

    # database and GUI initialization
    GUIMgr = guiMgr()
    TotalStockData = dataBase(sourceUrl, monitorStock)
    GUIMgr.init_cur_stock(monitorStock[0])

    if internet: TotalStockData.set_name_for_stock()    
    else:  TotalStockData.gen_fake_data()

    # add button
    GUIMgr.create_button_by_stock_name_list(TotalStockData)
        #if internet: TotalStockData.get_data_from_server()

    
    start_update_5_sec(GUIMgr, TotalStockData)

    GUIMgr._window.mainloop()
