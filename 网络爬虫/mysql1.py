# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:36:24 2018

@author: Administrator
"""

# 导入pymysql模块
import pymysql
# 连接database
conn = pymysql.connect(host='localhost', user='root',password='13262523878',port=3306,db='spiders')
# 得到一个可以执行SQL语句的光标对象
cursor=conn.cursor()
'''
#(1)
cursor.execute('SELECT VERSION()')
print(cursor.fetchone())
cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')
conn.close()  
#(2)
sql=cursor.execute('CREATE TABLE IF NOT EXISTS students(id VARCHAR(255) NOT NULL,name VARCHAR(255) NOT NULL,age INT NOT NULL,PRIMARY KEY (id))')
conn.close()
'''
#字典后面用得着
"""
dict1={
 'id':"5",
'name':'s3df1',
'age':55
}
"""

'''
#(3)
sql1='UPDATE students SET name=%s, age=%s WHERE id=%s'
sql='INSERT INTO students({0}) values({1})'.format(','.join(dict1.keys()),','.join(['%s']*len(dict1)))
print(sql1 )
print(sql)
try:
    print(2)
    cursor.execute(sql1,('22','22','5'))
    #cursor.execute(sql,tuple(dict1.values()))
    #cursor.execute(sql,tuple(dict1.values()))
    conn.commit()
    
except:
    print('failed')
    conn.rollback()
    
conn.close()
'''

'''
#(4)
tables='students'
keys=','.join(dict1.keys())
#values=','.join(dict1.values())
sql='INSERT INTO students({0}) values({1}) on DUPLICATE KEY UPDATE '.format(','.join(dict1.keys()),','.join(['%s']*len(dict1)))
update=','.join(['{key}=%s'.format(key=key)for key in dict1])
print(update)
sql=sql+update
print(sql)
sql1='INSERT INTO students({0}) values({1})'.format(','.join(dict1.keys()),','.join(['%s']*len(dict1)))
sql2='DELETE FROM students WHERE id>100'
try:
   # cursor.execute(sql1,('hong','332','45'))
    cursor.execute(sql2)
    conn.commit()
    print('hello')
    if cursor.execute(sql,('11','honghuoujun','4','11','zhangli','5')):
        print('successful')
        conn.commit()
except:
        print('failed')
        conn.rollback()

q=cursor.execute('SELECT * FROM students WHERE id>1')

"""result=cursor.fetchall()
print(type(result))
print('\n'.join([str(i) for i in result]),cursor.rowcount)
"""

i=cursor.fetchone()
print(i)
while i!=None:
    print(i)
    i=cursor.fetchone()
print(cursor.rowcount)
conn.close()
'''
