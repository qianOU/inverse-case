# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 23:23:03 2018

@author: Administrator
"""
import json,copy
a={'hong':89,'洪':43}
with open('text.txt','w+',encoding='utf-8') as f:
    f.seek(0,0)
    a1=json.dumps(a,indent=2,ensure_ascii=False)
    f.write(a1)
f=open('text.txt','r',encoding='utf-8')
t=f.read()
a=json.loads(t)
print(a)
  
import csv
with open('text1.csv','w',encoding='utf-8',newline='') as f:
    writer=csv.writer(f,delimiter=',')
    writer.writerow(['id','name','age'])
    writer.writerow(['2014','hong',13])
    writer.writerow(['2915','合肥市地方',65])
    writer=csv.DictWriter(f,delimiter='\t',fieldnames=['hong','洪'])
    writer.writeheader()
    writer.writerow(a)
    writer.writerows([a,copy.copy(a)])

with open('text1.csv','r',encoding='utf-8',newline='') as f:
    reader=csv.reader(f)
    print(type(reader))
    for i in reader:
        print(i)
    