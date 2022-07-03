from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor


# def work(name):
#     for i in range(1000):
#         print(name, i)
#
#
# if __name__ == '__main__':
#     p1 = Process(target=work, args=("process1:",))
#     p2 = Process(target=work, args=("process2:",))
#
#     p1.start()
#     p2.start()

def work(name):
    for i in range(1000):
        print(name, i)


if __name__ == '__main__':
    with ProcessPoolExecutor(16) as executor:
        for i in range(4):
            executor.submit(work, f"process{i}:")