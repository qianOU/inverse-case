# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 14:56:17 2019

@author: Administrator
"""
import queue
import threading
import random
import time
gtimes=0
gMoney = 1000
gLock=threading.Lock()
gTOtalTimes=10

class Producter(threading.Thread):
    def __init__(self,*args,**kwgs):
        super(Producter,self).__init__(*args,**kwgs)
        
    def run(self):
        global gMoney,gtimes
        while True:
            gtimes += 1
            money = random.randint(100,1000)
            gLock.acquire()
            gMoney += money
            if gtimes > 10:
                print("%s结束！"%threading.current_thread())
                gLock.release()
                break
            print('{}生成了{}元钱，剩余{}元钱'.format(threading.current_thread(),
                money,gMoney))
            gLock.release()
            time.sleep(2)
                    

class Consumer(threading.Thread):
    def __init__(self,*args,**kwgs):
      super().__init__(*args,**kwgs)
    
    def run(self):
        while True:
           global gMoney,gtimes
           money = random.randint(100,1000)
           gLock.acquire()
           if money > gMoney:
                print('剩余金额不足!')
           else:
                gMoney -= money
                print('{}消费了{}元，剩余{}元钱!'.format(
              threading.current_thread(),money,gMoney))
           if gtimes > gTOtalTimes:
               print("%s结束！"%threading.current_thread())
               gLock.release()
               break
           gLock.release()
           time.sleep(1)
            
def main():
    for i in range(3):
        t = Producter(name='生产者%d' %i)
        t.start()
    for i in range(3):
        t = Consumer(name="消费者-%d" %i)
        t.start()
if __name__ == '__main__':
    main()
    
