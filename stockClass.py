import requests
import datetime 

class stockInfo:
    def __init__(self, stockIndStr):
        self._priceList = list()                # float or None
        self._timeList = list()                 # datetime.datetime structure
        self._stockQueryStr = 'tse_{}.tw'.format(stockIndStr)
        self._stockIndStr = stockIndStr         # str
        self._name = None                       # str

    def add_price_time(self, price, time):

        # add the time for 6 sec if the time fixed at 13:30, not a very good solution
        if self._timeList and time in self._timeList:
            time = self._timeList[-1] + datetime.timedelta(seconds = 5)

        self._priceList.append(price)
        self._timeList.append(time)

    def get_price_list(self):
        return self._priceList

    def get_time_list(self):
        return self._timeList

    def get_ind_str(self):
        return self._stockIndStr

    def get_query_str(self):
        return self._stockQueryStr

    def set_name(self, name):
        self._name = name
    
    def get_name(self):
        return self._name

class dataBase:
    def __init__(self, sourceUrl, monitorStock):
        self._dataDict = dict()
        self._sourceUrl = sourceUrl          # str

        self.add_stock_member(monitorStock) 

    def add_stock_member(self, sIndStrList): 
        for sIndStr in sIndStrList:
            self._dataDict[sIndStr] = stockInfo(sIndStr)

    def set_name_for_stock(self):
        data = {'ex_ch': '|'.join([self._dataDict[sInd].get_query_str() 
                                  for sInd in self._dataDict]), 'json': '1'}

        res = requests.get(self._sourceUrl, params = data)
        res = (res.json())['msgArray']
        
        for sInfoServer in res:
            sName = sInfoServer['n']
            sInd = sInfoServer['c']
            self._dataDict[sInd].set_name(sName)

    def server_data_preprocess(self, oriStockPrice, oriStockTime):
        if oriStockPrice == '-': 
            price = None
        else: 
            price = float(oriStockPrice)

        now = datetime.datetime.now()
        timeStructTmp = datetime.datetime.strptime(oriStockTime, "%H:%M:%S")
        timeStructTmp = timeStructTmp.replace(now.year, now.month, now.day)

        return price, timeStructTmp

    def get_data_from_server(self):   #dataBase should be a dictionary
        
        data = {'ex_ch': '|'.join([self._dataDict[sInd].get_query_str() for sInd in self._dataDict]), 'json': '1'}
        res = requests.get(self._sourceUrl, params = data)
        res = (res.json())['msgArray']
        
        sTimetmp = None
        for sInfoServer in res:
            sPrice = sInfoServer['z']               # str of price or '-'
            sInd = sInfoServer['c']                 # str of stockInd
            sTimetmp = sTime = sInfoServer['t']     # str of HH:MM:SS
            
            # return floting sPrice and datetime.datetime struct sTime
            sPrice, sTime = self.server_data_preprocess(sPrice, sTime)
            self._dataDict[sInd].add_price_time(sPrice, sTime)
        
        print("Update data from server " + sTimetmp)


    def get_dataDict(self):
        return self._dataDict

 
    def gen_fake_data(self):
        for sInd in self._dataDict:
            self._dataDict[sInd] = stockInfo(sInd)
            self._dataDict[sInd]._priceList = [11 + int(sInd), 5 + int(sInd), 7 + int(sInd), 9 + int(sInd), 8 + int(sInd)]
            self._dataDict[sInd]._timeList = [11, 5, 7, 9, 8]
            self._dataDict[sInd]._name = sInd

if __name__ == '__main__':
    print('Cannot execute this file directly')
    exit(-1)



# --------------------------------- useful code ------------------------
#data = {'ex_ch': '|'.join(['tse_{}.tw'.format(stockInd) for stockInd in monitorStock]), 'json': '1'}
#print("{0:8.4f}  {1:s}".format(float(stockInfo['z']), stockInfo['n']))     