import threading
import time
print("test")
def myloop(rangenum:int):
    for i in range(rangenum):
        print(i)
        time.sleep(1)
        if i== rangenum-1:
            print("I AM Finished")
t1=threading.Thread(target=myloop,args=(10,))
t2=threading.Thread(target=myloop,args=(20,))
t1.start()
t2.start()