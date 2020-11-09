# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 15:58:18 2018

@author: Administrator
"""

from redis import StrictRedis as SR,ConnectionPool
#redis=SR(host='localhost',port=6379,db=0,password='13262523878')
pool=ConnectionPool(host='localhost',port=6379,db=0,password='13262523878')
#print(redis.get('name').decode('utf-8'))
url='redis://:13262523878@localhost:6379/0'
pool=ConnectionPool.from_url(url)
redis=SR(connection_pool=pool)
redis.set('name','bob')
redis.set('gender','male')
redis.set('age',12)
q=redis.exists('name')
redis.rename('age','teenagers')
"""
print(type(q),q)
print(redis.type('name'))
print(redis.keys('g*r'))
print(redis.keys())
print(redis.randomkey())
print(redis.dbsize())
print(redis.expire('teenagers',2))
print(redis.ttl('gender'),redis.ttl('teenagers'))
print(redis.get('teenagers'))
print(redis.getset('name','bmb'))
print(redis.get('name'))
print(redis.mget('name','gender','teenagers'))
print(redis.setex('new',1,'happy'))
print(redis.append('new','ok'))
print(redis.substr('new',1,-1))

q=redis.lpush('list',1,2,3,4)
z=redis.ltrim('list',1,-1)
print(z)
print(redis.llen('list'))
print(redis.lrange('list',0,-1))
print(redis.mget('new','name'))
redis.sadd('tags','ha','ha')
print(redis.scard('tags'))
print(redis.smembers('tags'))
print(redis.srandmember('tags'))
print(redis.zadd('grade',{'mike':100,'size':50,'bob':79}))
"""
redis.zadd('grade',{'mike':67,'bob':54,'aimy':100})
print(redis.zrevrange('grade',0,2,withscores=True))
print(redis.zincrby('grade',-2,'bob'))
print(redis.zrank('grade','mike'))
print(redis.zcard('grade'))
"""
redis.hset('price','cake',5)
redis.hsetnx('price','orange',6)
print(redis.hmget('price',['orange','cake']))
print('**'*40)
print(redis.hlen('price'))
print(redis.hkeys('price'))
print(redis.hvals('price'))
q=redis.hgetall('price')

print(*[{i.decode('utf-8'):q[i].decode('utf-8')} for i in q.keys()])
print('*'*80)
redis.hdel('price','orange','cake')
print(redis.hlen('price'))
print(type(redis.hkeys('price')))
print(redis.hvals('price'))
print(redis.hgetall('price'))
"""