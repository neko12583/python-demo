from threading import Thread
import time
import random

tikets=[]
for j in range(501):
    item="T"+str(j)
    tikets.append(item)
tikets.reverse()

def sell(i):
    while tikets:
        w="W"+str(i+1)
        w_time=random.randrange(5)
        time.sleep(w_time)
        try:
            tiket=tikets.pop()
        except:
            print(w,"表示票卖完了,还有人要买")
            break
        print(w,"卖出",tiket)
        time.sleep(0.1)

jobs=[]
for i in range(10):
    t = Thread(target=sell,args=(i,))
    jobs.append(t)
    t.start()

for item in jobs:
    item.join()

