import asyncio

from timer import Timer


async def hello1():

    await asyncio.sleep(3)  # Async Sleep for 5 seconds

    print("hello 1")

    return "hello11"


async def hello2():

    await asyncio.sleep(3)  # Async Sleep for 5 seconds

    print("hello 2")

    return "hello22"


async def main():

    t = Timer()  # Create Timer

    t.start()  # Start Timer

    g1 = asyncio.gather(*[hello1()])
    g2 = asyncio.gather(*[hello2()])
    groups = asyncio.gather(g2,g1)   

    await groups

    print(await g1)
    print(await g2)
    print(await groups)
   
    elapsed = t.stop()

    print(elapsed)


if __name__ == "__main__":

    asyncio.run(main())
