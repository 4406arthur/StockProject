from datetime import *

weekend = set([5, 6])
def dyurl(a):
    url = []
    for  i in range (5,12):
        for j in range (1,31):
          if datetime(2014, i, j).weekday() not in weekend:
          	url.append('http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/genpage/Report20140'+ str(i) + '/A11220140' + str(i) + str(j) + str(13) + '.php?select2=13&chk_date=103/0' + str(i) + '/' + str(j))
            #url = 'http://www.twse.com.tw/ch/trading/exchange/STOCK_DAY/genpage/Report' + y + m + '/' + y + m + '_F3_1_8_' + str(stockNumber) + '.php?STK_NO=' + str(stockNumber) + '&myear=' + y + '&mmon=' + m
    return url