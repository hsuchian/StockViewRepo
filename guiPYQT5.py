# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file '.\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from stockClass import *


class Ui_MainWindow(object):   # this is inheritance from object

    def __init__(self, sourceUrl, monitorStock):
        self._mainWindow = QtWidgets.QMainWindow()
        self._currentStock = monitorStock[0]
        self._stockDataBase = None
        

        self.setupUi()
        self.dataBaseInit(sourceUrl, monitorStock)
        self.guiInit()

    def guiInit(self):
        self.create_button_by_stock_database(self._stockDataBase)   

    def dataBaseInit(self, sourceUrl, monitorStock):
        self._stockDataBase = dataBase(sourceUrl, monitorStock)
        self._stockDataBase.set_name_for_stock()
        #self._stockDataBase.get_data_from_server()

    def updateFcn(self):
        self._stockDataBase.get_data_from_server()
        self.plot_data(self._stockDataBase._dataDict[self._currentStock])

    def setAutoUpdateStart(self):
        self._timer = QtCore.QTimer()
        self._timer.timeout.connect(self.updateFcn)
        self._timer.setInterval(5000)  # 1000ms = 1s
        self._timer.start()


    def plot_data(self, sData):
        
        timeList = sData.get_time_list() 
        priceList = sData.get_price_list()
        
        fig = plt.figure(figsize=(8,6))  # difined in inches
        axis1 = fig.add_subplot(111)
        axis1.plot(timeList, priceList, '*-b')

        scene = QtWidgets.QGraphicsScene()
        # QtWidgets.QGraphicsScene().add
        scene.addWidget(FigureCanvas(fig))
        self.graphicsView.setScene(scene)
        self.graphicsView.show()


    def button_action(self, sData):
        self._currentStock = sData.get_ind_str()
        self.plot_data(sData)

    def create_button(self, sData, buttonInd):

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(870, 50*buttonInd + 50, 151, 31))
        self.pushButton.setObjectName("pushButton" + sData.get_name())

        # QPushButton.clicked() will pass a boolean variable to the button_action
        # and thus cause unexpected result
        self.pushButton.clicked.connect(lambda unused, localsData = sData: self.button_action(localsData))

        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("MainWindow", sData.get_name()))

    def create_button_by_stock_database(self, stockDataBase):
        sDataDict = stockDataBase.get_dataDict()
        buttonInd = 0
        for stockInd in sDataDict:
            sData = sDataDict[stockInd]
            self.create_button(sData, buttonInd)
            buttonInd += 1

    def setupUi(self):
        self._mainWindow.setObjectName("StockView")
        self._mainWindow.resize(1136, 797)

        self.centralwidget = QtWidgets.QWidget(self._mainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(30, 60, 781, 611))
        self.graphicsView.setObjectName("graphicsView")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 161, 31))
        self.label.setObjectName("label")
        
        self._mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self._mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1136, 25))
        self.menubar.setObjectName("menubar")
        self._mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self._mainWindow)
        self.statusbar.setObjectName("statusbar")
        self._mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self._mainWindow)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self._mainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))

    def init_cur_stock(self, sInd):
        self._currentStock = sInd

    def get_cur_stock_ind(self):
        return self._currentStock



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)


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
