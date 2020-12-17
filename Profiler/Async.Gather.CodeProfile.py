import asyncio
from codeprofile import profiler
import sys

async def hello1():
    with profiler.profile("Hello1"):
        await asyncio.sleep(2)  # Async Sleep for 5 seconds

        print("hello 1")

        return "hello11"

# @profiler.profile_async_func
async def hello2():
    with profiler.profile("Hello2"):
        await asyncio.sleep(1)  # Async Sleep for 5 seconds

        print("hello 2")

        return "hello22"

# @profiler.profile_async_func
async def main():
    with profiler.profile("Main"):
        g1 = asyncio.gather(*[hello1()])
        g2 = asyncio.gather(*[hello2()])
        groups = asyncio.gather(g2,g1)   

        with profiler.profile("Groups"):   
            await groups

        print(await g1)
        print(await g2)
        print(await groups)


if __name__ == "__main__":
    asyncio.run(main())
    profiler.print_run_stats("Main","Hello1","Hello2","Groups")
