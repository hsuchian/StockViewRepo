# variable with camel case
# fucntion with '_'

#import stockClass
from stockClass import *
from guiPYQT5 import *
import json
import time
import sys


def start_update_5_sec(GUImgr, TotalStockData):
    TotalStockData.get_data_from_server()
    sdataDict = TotalStockData.get_dataDict()

    curStockInd = GUIMgr.get_cur_stock_ind()
    GUIMgr.plot_data(sdataDict[curStockInd])
    GUIMgr._window.after(5000, start_update_5_sec, GUIMgr, TotalStockData)


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

    # database and GUI initialization
    TotalStockData = dataBase(sourceUrl, monitorStock)
    TotalStockData.set_name_for_stock()


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)



    # add button, should after the dataBase initialization
    # since the button number and action fcn is decided by 
    # stock info
    ui.create_button_by_stock_database(TotalStockData)

    fig1 = plt.figure()

    ax1 = fig1.add_subplot(1,2,1)
    ax1.plot(range(1,6), [11, 10, None, 12, 13 ])

    scene = QtWidgets.QGraphicsScene()
    # QtWidgets.QGraphicsScene().add
    scene.addWidget(FigureCanvas(fig1))
    ui.graphicsView.setScene(scene)
    ui.graphicsView.show()
    MainWindow.show()
    sys.exit(app.exec_())



''' old code 

    GUIMgr = guiMgr()
    GUIMgr.init_cur_stock(monitorStock[0])   
    GUIMgr.create_button_by_stock_name_list(TotalStockData)

    
    start_update_5_sec(GUIMgr, TotalStockData)

    GUIMgr._window.mainloop() 

'''
