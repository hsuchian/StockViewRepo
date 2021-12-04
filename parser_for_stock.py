# variable with camel case
# fucntion with '_'

#import stockClass
from stockClass import *
from guiPYQT5 import *
import json
import time
import sys


# The name will be file name parser_for_stock if this file was imported by
# other file, so the below code will not be executed
# The name will be __main__ if this file was exectued directly
if __name__ == '__main__':
    # basic definition
    sourceUrl = "https://mis.twse.com.tw/stock/api/getStockInfo.jsp"
    monitorStock = ['2330', '2454', '0050', '0056', '00878', '2603', '2886']

    internet = 1
    if not internet:
        exit(-1)

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow(sourceUrl, monitorStock)

    ui._mainWindow.show()

    ui.setAutoUpdateStart()

    sys.exit(app.exec_())



''' old code 

    GUIMgr = guiMgr()
    GUIMgr.init_cur_stock(monitorStock[0])   
    GUIMgr.create_button_by_stock_name_list(TotalStockData)

    
    start_update_5_sec(GUIMgr, TotalStockData)

    GUIMgr._window.mainloop() 

'''
