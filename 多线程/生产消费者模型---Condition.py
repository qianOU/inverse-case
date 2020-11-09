import queue
import random
import time
import threading

gMoney = 1000
gTotalTimes = 10
gCondition = threading.Condition()
gtimes = 0

class Producter(threading.Thread):
    def __init__(self,*args,**kwgs):
      super().__init__(*args,**kwgs)
    def run(self):
        global gMoney,gtimes
        while True:
            gtimes += 1
            money = random.randint(100,1000)
            gCondition.acquire()
            gMoney += money
            if gtimes > gTotalTimes:
                print('%s结束！'%threading.current_thread())
                gCondition.release()
                return 
            print('{}生产了{}元，剩余{}元钱!'.format(
              threading.current_thread(),money,gMoney))
            gCondition.notify_all()
            gCondition.release()
            time.sleep(1)
            

class Consumer(threading.Thread):
    def __init__(self,*args,**kwgs):
      super().__init__(*args,**kwgs)
    def run(self):
        global gMoney
        money = random.randint(100,1000)
        while True:
            while money > gMoney:
                if gtimes > gTotalTimes:
                    print('%s结束！'%threading.current_thread())
                    return
                print("%s的钱不足!"%threading.current_thread())
                gCondition.wait()
            gCondition.acquire()
            gMoney -= money
            print('{}消费了{}元，剩余{}元钱!'.format(
            threading.current_thread(),money,gMoney))
            if gtimes > gTotalTimes:
                print('%s结束！'%threading.current_thread())
                gCondition.release()
                return           
            gCondition.release()
            time.sleep(2)
            
            
        

def main():
    for i in range(2):
        
        t = Producter(name='生产者:%s' %i)
        t.start()


    for i in range(3):
        t=Consumer(name="消费者%s"%i)
        t.start()
        

if __name__ =="__main__":
    main()
