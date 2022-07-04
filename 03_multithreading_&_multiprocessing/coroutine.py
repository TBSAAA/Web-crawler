import asyncio
import time


# async def work():
#     print("work")
#
# if __name__ == '__main__':
#     f = work()
#     # option 1: run directly
#     # asyncio.run(f)
#     # option 2: run in event loop
#     event_loop = asyncio.get_event_loop()
#     event_loop.run_until_complete(f)
#     event_loop.close()

# python 3.10 version or after
#     event_loop = asyncio.get_event_loop()
#     event_loop.run_until_complete(main())
#     event_loop.close()


# The following is the routine writing of the coroutine.

async def func1():
    print("this is func1, start")
    # wait for the task to finish and continue execution from here.
    await asyncio.sleep(4)
    print("this is func1, end")


async def func2():
    print("this is func2, start")
    await asyncio.sleep(5)
    print("this is func2, end")


async def func3():
    print("this is func3, start")
    await asyncio.sleep(2)
    print("this is func3, end")


# All tasks that need to be processed are handled here.
async def main():
    # encapsulate tasks as task objects.
    task1 = asyncio.create_task(func1())
    task2 = asyncio.create_task(func2())
    task3 = asyncio.create_task(func3())

    # wait for all tasks to complete.
    tasks = [task1, task2, task3]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    time_start = time.time()
    asyncio.run(main())
    time_end = time.time()
    print(f"time: {time_end - time_start}")
