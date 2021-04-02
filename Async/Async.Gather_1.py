import asyncio

from timer import Timer
data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

async def sleepy(n):
    await asyncio.sleep(n)
    return n*2

async def main():

    t = Timer()  # Create Timer

    t.start()  # Start Timer

    sleeparr = [sleepy(n) for n in data]
    
    groupsModified = asyncio.gather(*sleeparr) 
   
    print(await groupsModified)
    
    print("Finished")
    elapsed = t.stop()
    print(elapsed)


if __name__ == "__main__":
    asyncio.run(main())
