# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 15:59:35 2018

@author: Administrator
"""
import pymongo,copy
client=pymongo.MongoClient(host='localhost',port=27017)
db=client.test
collection=db.students
print(type(collection))
student={
        'id':'20170101',
        'name':'jordan',
        'age':20,
        'gender':'male'
        }
student2={
        'id':'20170103',
        'name':'honghujum',
        'age':30,
        'gender':'female'
        }
students=copy.deepcopy(student)
'''
students['id']='happy'
students['age']=69
result=collection.insert_one(student2)
print(result.inserted_id)
print(result)
print('='*100)
result=collection.insert_many([student,students])
print(result)
print(result.inserted_ids)
'''
result=collection.find_one({'name':'jordan'})
print('='*100+'\n',type(result))
print(result)
result1=collection.find({'name':'jordan'})
print(type(result1))
for i in result1:
    print(i)
print('*'*100)
from bson.objectid import ObjectId
result=collection.find_one({'_id': ObjectId('5c00165f2cf02b2058394feb')})
print(result)
result=collection.find_one({'_id': ObjectId('5c00165f2cf02b2058394fec')})
print(result)
print('*'*100)
resuilts=collection.find({'age':{'$gt':30}})
for i in resuilts:
    print(i)
print(resuilts.count())
print('*'*100)
result=collection.find({'age':{'$lt':60}}).sort('age',pymongo.DESCENDING).skip(16).limit(5)
print([(re['_id'],re['name'],re['age']) for re in result])
from bson.objectid import ObjectId
q=collection.find({'_id':{'$gt':ObjectId('5c0013492cf02b2058394fcb')}}).sort('name',pymongo.ASCENDING)
print('*'*100)
for i in q:
    print(i)
print('*'*100)
condition={'name':'jordan'}
student=collection.find_one(condition)
students['www']='ni'
student['name']='jordan'
print(student)
#result=collection.update(condition,students)
result=collection.update_many(condition,{'$inc':{'age':1}})
print(type(result),result,result.modified_count,result.matched_count)
result=collection.delete_many({'age':{'$gte':30}})
print('$'*50)
print(result.deleted_count,result)
print('^'*70)
result=collection.find_one_and_delete(condition)
print(type(result),result)