# io_bound/threaded.py
import concurrent.futures as futures
import requests
import threading
import time

data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

thread_local = threading.local()

def sleepy(n):
    time.sleep(2)
    return n*2

def ExecuteSleep():
    l = len(data)
    results = []
    # Submit needs explicit mapping of I/p and O/p
    # Output may not be in the same Order
    with futures.ThreadPoolExecutor(max_workers=l) as executor:
        result_futures = {d:executor.submit(sleepy,d) for d in data}
        results = {d:result_futures[d].result() for d in data}
    
    return results

if __name__ == '__main__':
    print("Starting ...")
    t1 = time.time()
    result = ExecuteSleep()
    print(result)
    print("Finished ...")
    t2 = time.time()
    print(t2-t1)