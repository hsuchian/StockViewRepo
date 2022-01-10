
from stockClass import *


def creat_fcn(stockDataBase):
    
    fcnList = list()
    sDataDict = stockDataBase.get_dataDict()
    for stockInd in sDataDict:
        sData = sDataDict[stockInd]
        fcnList.append(lambda x = sData.get_name(): print(x))
    
    return fcnList


# the reason why lambda not defined different value in for loop
# https://docs.python.org/3/faq/programming.html#id10
sourceUrl = "https://mis.twse.com.tw/stock/api/getStockInfo.jsp"
monitorStock = ['2330', '2454', '0050', '0056', '00878', '2603', '2886']

internet = 1
if not internet:
    exit(-1)

# database and GUI initialization
TotalStockData = dataBase(sourceUrl, monitorStock)
TotalStockData.set_name_for_stock()


fcn = creat_fcn(TotalStockData)

fcn[0]()
fcn[1]()
fcn[2]()
fcn[3]()
fcn[4]()
fcn[5]()

print(len(fcn))


test



wgwegwe

'''
Python utilizes a system, which is known as “Call by Object Reference” or “Call by assignment”.
 In the event that you pass arguments like whole numbers, strings or tuples to a function, 
 the passing is like call-by-value because you can not change the value of the immutable 
 objects being passed to the function. Whereas passing mutable objects can be considered
  as call by reference because when their values are changed inside the function, then it
   will also be reflected outside the function.
'''



'''
https://towardsdatascience.com/https-towardsdatascience-com-python-basics-mutable-vs-immutable-objects-829a0cb1530a


Mutable and Immutable Data Types in Python
Some of the mutable data types in Python are list, dictionary, set and user-defined classes.
On the other hand, some of the immutable data types are int, float, decimal, bool, string, tuple, and range.

'''
