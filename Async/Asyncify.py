# Run the Sync function also as Async using anyio package
# https://asyncer.tiangolo.com/

import time
import asyncio
import anyio
from asyncer import asyncify

# Synchronous Function
def do_sync_work(name: str):
    time.sleep(5)
    return f"Hello, {name}"

# Asynchronous Function
async def do_async_work(name: str):
    await anyio.sleep(5)
    return f"Hello, {name}"

# Main Function
async def main():
    # Wrap Sync in the Asyncify wrapper
    t1 = asyncify(do_sync_work)(name="Sync World")
    # Actual Async method
    t2 = do_async_work(name="Async World")
    
    # Gather and Await
    result  = await asyncio.gather(*[t1,t2])
    
    #Print Values
    for value in result:
        print(value)

# Run the main using anyio similar to asyncio
anyio.run(main)