# io_bound/threaded.py
import concurrent.futures
import requests
import threading
import time

data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

thread_local = threading.local()

def sleepy(n):
    time.sleep(n//2)
    return n*2

def ExecuteSleep():
    l = len(data)
    results  = []
    # Map provides the results in same order as I/p therefore no extra mapping like Submit is required
    with concurrent.futures.ThreadPoolExecutor(max_workers=l) as executor:
        resultgenerators = executor.map(sleepy,data)
        for result in resultgenerators:
            results.append(result)
            
    return results

if __name__ == '__main__':
    print("Starting ...")
    t1 = time.time()
    result = ExecuteSleep()
    print(result)
    print("Finished ...")
    t2 = time.time()
    print(t2-t1)