#生成器函数
# def countDown(n):
#     while n > 0:
#         yield n
#         n -= 1
# gen = countDown(5)#获得生成器对象
# for i in range(3):
#     print(next(gen))
#
# def count(n):
#     list = []
#     while n > 0:
#         list.append(n)
#         n -= 1
#     return list
#
# print(count(5))
# 使用生成式迭代器实现斐波那契数列
# import sys
# def feibonaxi(n):
#         a,b,counter = 0,1,0
#         while True:
#             if counter > n:
#                 return
#             yield a
#             a,b = b,a + b
#             counter += 1
# f = feibonaxi(10)
# while True:
#     try :
#         print(next(f),end=" ")
#     except StopIteration:
#         sys.exit()
import threading
from time import process_time_ns

# #多线程学习
# import threading
# import time
# def printNums():
#     for i in range(5):
#         time.sleep(1)
#         print(i)
# thread1 = threading.Thread(target=printNums())
# thread1.start()
# thread1.join()

# 多个线程之间竞争
l1 = []
def wtData():
    for i in range(5):
        l1.append(i)
    print("正在写入数据:",l1)
def rdData():
    print("正在读取数据:",l1)
if __name__ == "__main__":
    t1 = threading.Thread(target=wtData())
    t2 = threading.Thread(target=rdData())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("程序结束")
