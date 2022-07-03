from threading import Thread
from concurrent.futures import ThreadPoolExecutor


# Simplest two-thread
# def work():
#     for i in range(100):
#         print("thread: ", i)
#
#
# if __name__ == '__main__':
#     # work()
#     t = Thread(target=work)  # create a thread
#     t.start()  # start the thread
#
#     for i in range(100):
#         print("main: ", i)


# Created 3 threads to complete the work
# def work(name):
#     for i in range(100):
#         print(name, i)
#
#
# if __name__ == '__main__':
#     # pass parameters to thread
#     t1 = Thread(target=work, args=("thread1",))
#     t1.start()
#
#     t2 = Thread(target=work, args=("thread2",))
#     t2.start()
#
#     t3 = Thread(target=work, args=("thread3",))
#     t3.start()


# Create a thread pool to complete the work
def work(name):
    for i in range(100):
        print(name, i)


if __name__ == '__main__':
    # create a thread pool
    with ThreadPoolExecutor(16) as executor:
        for i in range(4):
            executor.submit(work, f"thread{i}:")
