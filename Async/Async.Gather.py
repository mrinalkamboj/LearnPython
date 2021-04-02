import asyncio

from timer import Timer


async def hello1():

    await asyncio.sleep(10)  # Async Sleep for 5 seconds

    print("hello 1")

    return "hello1"


async def hello2():

    await asyncio.sleep(8)  # Async Sleep for 5 seconds

    print("hello 2")

    return "hello2"

async def hello3():

    await asyncio.sleep(7)  # Async Sleep for 5 seconds

    print("hello 3")

    return "hello3"


async def main():

    t = Timer()  # Create Timer

    t.start()  # Start Timer

    # # g1 = asyncio.gather(*[hello1()])
    # # g2 = asyncio.gather(*[hello2()])
    # # g3 = asyncio.gather(*[hello3()])
    # # # g123 = asyncio.gather(*[hello3(),hello1(),hello2()],return_exceptions=True)
    # # groups = asyncio.gather(g2,g3,g1) 
    groupsModified = asyncio.gather(*[hello3(),hello1(),hello2()]) 

    # await groups

    # print(await g1)
    # print(await g2)
    # print(await groups)
    print(await groupsModified)
    # print(await g12)
    
    print("Finished")
    elapsed = t.stop()

    print(elapsed)


if __name__ == "__main__":

    asyncio.run(main())
