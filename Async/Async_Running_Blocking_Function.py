import asyncio
import time

from concurrent.futures import ThreadPoolExecutor


def blocking(msg, t):
    t1 = time.perf_counter()
    print(f"START {msg}: (scheduled: {t}s)")
    time.sleep(t)
    print(f"END {msg}: (elapsed: {time.perf_counter() - t1:.1f}s)")


async def task1(msg, t):
    t1 = time.perf_counter()
    print(f"START {msg}: (scheduled: {t}s)")
    await asyncio.sleep(t)
    print(f"END {msg}: (elapsed: {time.perf_counter() - t1:.1f}s)")


async def task2(msg, t):
    # Fetch the Async Loop Context
    loop = asyncio.get_running_loop()
    
    # Create Thread Pool Executor
    with ThreadPoolExecutor() as executor:
        # # Non Blocking run using Custom thread pool
        future = loop.run_in_executor(executor, blocking, msg,t)
        await future
        # # Blocking Run ( will block main event loop and will not allow other async methods to run)
        # future = executor.submit(blocking, msg, t)
        # future.result()


async def main():
    # Fetch the Async Loop Context
    loop = asyncio.get_running_loop()

    # Create a couple of Blocking tasks
    aws = [
        task1("non-blocking", 1.0), # Blocking needs explicit  loop.run_in_executor else it will block the main event loop
        loop.run_in_executor(None, blocking, "non-blocking executor", 5.0), # Use default pool (non blocking using Async loop context )
        task2("blocking executor", 10.0),
    ]

    # Can use the asyncio.gather
    res = await asyncio.gather(*aws)
    # Or as follows using asyncio.as_completed
    #    for coro in asyncio.as_completed(aws):
    #        await coro


if __name__ == "__main__":
    # Run the Main Async method
    asyncio.run(main())
