# io_bound/threaded.py
import concurrent.futures as futures
import requests
import threading
import time
import asyncio

# Input Data Points
data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# Blocking Sleepy Function
def sleepy(n):
    time.sleep(n//4)
    return n*2

# Async method to call the blocking sleepy function using running loop executor
async def ExecuteSleep():
    
    loop = asyncio.get_running_loop()     
    l = len(data)    
    results = []
    
    # Submit needs explicit mapping of I/p and O/p
    # Output may not be in the same Order
    # Run the sleepy methods using loop.run_in_executor, otherwise it will block other Async IO calls
    with futures.ThreadPoolExecutor(max_workers=l) as executor:
        # if executor is not supplied orn supplied as None then it will be default Threadpool
        result_futures = {d:loop.run_in_executor(executor, sleepy,d) for d in data}
        # await to fetch the result
        results = {d:await result_futures[d] for d in data}
    
    return results

if __name__ == '__main__':
    print("Starting ...")
    t1 = time.time()
    # Running ExecuteSleep() using asyncio.run
    result  = asyncio.run(ExecuteSleep())
    print(result)
    print("Finished ...")
    t2 = time.time()
    print(t2-t1)