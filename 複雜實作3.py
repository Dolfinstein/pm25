# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 18:41:12 2018

@author: Archer
"""
import requests,ast,sqlite3,os
from bs4 import BeautifulSoup

conn=sqlite3.connect('sqlite01')
sqlstr='CREATE TABLE IF NOT EXISTS pm25 ("Place"INTEGER PRIMARY KEY NOT NULL,"Date" TEXT,"PM25" TEXT)'
conn.execute(sqlstr)
url='http://opendata.epa.gov.tw/ws/Data/ATM00756/?$skip=0&$top=1000&format=json'
htm=requests.get(url)

import hashlib
html=htm.text.encode('utf-8-sig')
html2=htm.text
#print(html2)
sp=BeautifulSoup(html,'html.parser')

dicts=ast.literal_eval(sp.text)
#print(type(dict))

#print(htm.text)
md5=hashlib.md5(html).hexdigest()
if os.path.exists('old_md5.txt'):
    with open('old_md5.txt','r') as f:
        old_md5=f.read()
    if old_md5==md5:
        print("資料未更新")
        cursor=conn.execute('select * from pm25')
        rows=cursor.fetchall()
        print(rows)
    else:
        print("資料已更新")
        for dict in dicts:
            print(dict.get("PM2.5_Mass_Concentration"))
        
    
else:
    with open('old_md5.txt','w') as f:
        f.write(md5)
    print("初次使用")
    for dict in dicts:
        sqlstr='insert into pm25 values(dict.get("Site"),dict.get("Date"),dict.get("PM2.5_Mass_Concentration")'
        cursor.execute(sqlstr)
        conn.commit()

conn.close()


#print(md5)



#for x in sp:
  #  print(sp[0])
#    break
#print(sp.text)
#print(sp.text)
#target=sp.find(" ")   #  type = list
#6print(target)
#print(sp.find_all("td"))
#print(target)

#for item in target:
  #  list.append(item.text)
   # print(item)
   # print(item.text)
  #  if item.text!="none":
     #   print(item.text)
      #  
 #   else:
   #     print("空白")
#print(type(item.text))





#print()





#print(list)




































