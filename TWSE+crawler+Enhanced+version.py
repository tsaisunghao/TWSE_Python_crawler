
# coding: utf-8

# In[9]:

import requests
import json
import csv
import time, datetime,os


# In[10]:

dt = datetime.datetime.now()
dt.year
dt.month


# In[11]:

id_list = ['2303','2330','1234','3006','2412'] #inout the stock IDs
now = datetime.datetime.now()
year_list = range (2007,now.year+1) #since 2007 to this year
month_list = range(1,13)  # 12 months


# In[15]:

for stock_id in id_list:
    for year in year_list:
        for month in month_list:
            if (dt.year == year and month > dt.month) :break  # break loop while month over current month
            sid = str(stock_id)
            yy  = str(year)
            mm  = month
            directory = 'D:/stock'+'/'+sid +'/'+yy +'/'       #setting directory
            filename = str(yy)+str("%02d"%mm)+'.csv'          #setting file name
            smt = get_webmsg(year ,month, stock_id)           #put the data into smt 
            makedirs (year, month, stock_id)                  #create directory function
            write_csv (stock_id,directory, filename, smt)    # write files into CSV
            time.sleep(1)
            


# ###http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20170605&stockNo=2330

# In[12]:

#standard web crawing process
def get_webmsg (year, month, stock_id):
    date = str (year) + "{0:0=2d}".format(month) +'01' ## format is yyyymmdd
    sid = str(stock_id)
    url_twse = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date='+date+'&stockNo='+sid
    res =requests.post(url_twse,)
    soup = bs(res.text , 'html.parser')
    smt = json.loads(soup.text)     #convert data into json
    return smt


# In[13]:

def write_csv(stock_id,directory,filename,smt) :
    writefile = directory + filename               #set output file name
    outputFile = open(writefile,'w',newline='')
    outputWriter = csv.writer(outputFile)
    head = ''.join(smt['title'].split())
    a = [head,""]
    outputWriter.writerow(a)
    outputWriter.writerow(smt['fields'])
    for data in (smt['data']):
        outputWriter.writerow(data)

    outputFile.close()


# In[14]:

#判斷路徑，如果路徑不存在則建立路徑
def makedirs (year, month, stock_id):
    sid = str(stock_id)
    yy      = str(year)
    mm       = str(month)
    directory = 'D:/stock'+'/'+sid +'/'+ yy
    if not os.path.isdir(directory):
        os.makedirs (directory)  # os.makedirs 可以一次建立好幾層資料夾

