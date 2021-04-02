import time
import multiprocessing as mp

data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def sleepy(n):
    time.sleep(n)
    return n*2

t1 = time.time()
p = mp.Pool()
final_data = p.map(sleepy, data)
p.close()
p.join()
print(final_data)
print("Finished")
t2 = time.time()
print(t2-t1)