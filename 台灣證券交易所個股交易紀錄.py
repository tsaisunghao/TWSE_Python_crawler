
# coding: utf-8

# In[7]:

import requests
import json
import csv


# In[4]:

url_twse ='http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20170501&stockNo=2330&'
res = requests.get(url_twse)
s = json.loads(res.text)


# In[5]:

s


# In[6]:

for data in (s['data']):
    print (data)


# In[8]:

outputfile = open(r'D:\stock\output.csv','w', newline='')
outputwriter = csv.writer(outputfile)
outputwriter.writerow(s['title'])
outputwriter.writerow(s['fields'])
for data in (s['data']):
    outputwriter.writerow(data)


# In[9]:

outputfile.close()


# In[ ]:



