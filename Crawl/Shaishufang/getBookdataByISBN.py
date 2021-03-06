# -*- coding:utf-8 -*-
import unirest, json, time
from collections import OrderedDict

def PutData(isbnurls):
    """ data """
    spidername = 'ShaishufangAmazon'
    cnt = 0
    for url in isbnurls:
        print cnt, '-->', url
        cnt += 1
        unirest.timeout(180)
        response = unirest.get(url, headers={"Accept":"application/json"}) # handle url = baseurl + isbn
        try:
            #bookdt
            bookdt = response.body['isbn']
            bookdt['spider'] = spidername
            #data style
            datadict = {}
            datadict['datas'] = [bookdt]
            #put datadict
            unirest.timeout(180)
            resdata = unirest.put(
                            "http://192.168.100.3:5000/data",
                            headers={ "Accept": "application/json", "Content-Type": "application/json" },
                            params=json.dumps(datadict)
                         )
        except:
            pass
        if ((cnt%80)==0):
            time.sleep(3)

if __name__ == '__main__':
    #baseurl = 'http://192.168.1.156:5001/book?isbn='     # mac-mini
    baseurl = 'http://192.168.100.3:5001/book?isbn='    # server
    #baseurl = 'http://192.168.31.187:5001/book?isbn='   # home-703
    #baseurl = 'http://192.168.1.124:5001/book?isbn='    # kids-5G
    isbnurls = []
    with file('./shaishufang.isbns.txt', 'rb') as fi:
        for line in fi.readlines():
            isbnurls.append(baseurl + line.strip())
    fi.close()

    #server
    #PutData(isbnurls[150000:190000])
    #PutData(isbnurls[190000:230000])
    #PutData(isbnurls[270000:670000])	# NOT DONE.

    #388726 - 21724 = 367002 		# 2015.12.28
    PutData(isbnurls[367002:670000])	

    #mac-mini [-20000+(-1724):-20000]
    #PutData(isbnurls[230000:270000])
