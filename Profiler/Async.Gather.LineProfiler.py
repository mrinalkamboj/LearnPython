import asyncio
import sys
from LineProfiler import do_profile

@do_profile(follow=[asyncio.sleep])
async def hello1():
   
    await asyncio.sleep(2)  # Async Sleep for 5 seconds

    print("hello 1")

    return "hello11"


@do_profile(follow=[asyncio.sleep])
async def hello2():
    
    await asyncio.sleep(1)  # Async Sleep for 5 seconds

    print("hello 2")

    return "hello22"


@do_profile()
async def main():
    
    g1 = asyncio.gather(*[hello1()])
    g2 = asyncio.gather(*[hello2()])
    groups = asyncio.gather(g2,g1) 
           
    await groups

    print(await g1)
    print(await g2)
    print(await groups)


if __name__ == "__main__":
    asyncio.run(main())
