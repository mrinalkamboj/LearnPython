import asyncio

from timer import Timer


async def hello1():

    await asyncio.sleep(7)  # Async Sleep for 5 seconds

    print("hello 1")


async def hello2():

    await asyncio.sleep(5)  # Async Sleep for 5 seconds

    print("hello 2")


async def main():

    t = Timer()  # Create Timer

    t.start()  # Start Timer

    task1 = asyncio.create_task(hello1())  # Start Async Task

    task2 = asyncio.create_task(hello2())  # Start Async Task

    await task1  # Await Task1 to finish

    await task2  # Await Task 2 to finish

    elapsed = t.stop()

    print(elapsed)


if __name__ == "__main__":

    asyncio.run(main())
