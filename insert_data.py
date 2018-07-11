# -*- coding: utf-8 -*-
"""
@author: Kevin
"""
import requests,ast,sqlite3,os
import hashlib
from bs4 import BeautifulSoup

conn=sqlite3.connect('sqlite01.db')
conn.text_factory = str #讓他可以存取超過8-bite的文字
c = conn.cursor()
sqlstr='CREATE TABLE IF NOT EXISTS pm25 ("Place" TEXT, "Date" TEXT, "PM25" INTEGER)'
c.execute(sqlstr)

url='http://opendata.epa.gov.tw/ws/Data/ATM00756/?$skip=0&$top=1000&format=json'
htm=requests.get(url)

html=htm.text.encode('utf-8-sig')
html2=htm.text
sp=BeautifulSoup(html,'html.parser')

dicts=ast.literal_eval(sp.text)
md5=hashlib.md5(html).hexdigest()

print "初次使用"
sqlstr_input = '''INSERT OR IGNORE INTO pm25 (Place, Date, PM25) VALUES (?,?,?)'''

for dict in dicts:
  site = dict.get("Site")
 	date = dict.get("Date")
 	pm25 = dict.get("PM2.5_Mass_Concentration")
  project = (site, date, pm25)
  print project

  c.execute(sqlstr_input, project)
  conn.commit()
        
conn.close()