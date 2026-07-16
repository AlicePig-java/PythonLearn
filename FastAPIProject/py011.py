#进程间的通信是靠队列queue来进行的
# from queue import Queue
#
# q = Queue(3)
# q.put("飞机1号")
# q.put("飞机2号")
# q.put("飞机3号")
# print(q.get())
# print(q.get())
# print(q.empty())
# print(q.get())
# print(q.empty())


#互斥锁的实现
# import time
# import threading
# from threading import Thread
# from time import sleep
#
#
# def sing():
#     print("啦啦啦在唱歌")
#     time.sleep(2)
#     print("唱完歌了")
#
# def dance():
#     print("ttt在跳舞")
#     time.sleep(2)
#     print("ttt跳完了")
# if __name__ == "__main__":
#     t1 = Thread(target=dance)
#     t2 = Thread(target=sing)
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#     sleep(2)
#     print("表演完美谢幕")
# import time
# from greenlet import greenlet
# def sing():
#     print("啦啦啦在唱歌")
#     # time.sleep(2)
#     g1.switch()
#     print("唱完歌了")
#
# def dance():
#     print("ttt在跳舞")
#     # time.sleep(2)
#     g2.switch()
#     print("ttt跳完了")
# # 定义主程序入口
# if __name__ == "__main__":
#     g1 = greenlet(sing)
#     g2 = greenlet(dance)
#
#     g1.switch()#switch 切换到g1执行，这个是程序员的手动切换运行，只有自己手动switch的时候协程才会执行
#     g2.switch()

# import time
# import gevent
# def sing():
#     print("啦啦啦在唱歌")
#     gevent.sleep(3)
#     print("唱完歌了")
#
# def dance():
#     print("ttt在跳舞")
#     gevent.sleep(2)
#     print("ttt跳完了")
# if __name__ == "__main__":
#     # 创建协程对象
#     g1 = gevent.spawn(sing)
#     g2 = gevent.spawn(dance)
#
#     # 阻塞等待协程执行结束
#     g1.join()#等待g1执行结束
#     g2.join()

# 匹配正则表达式
import re
# #验证是否符合电子邮箱格式
# pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
# email = "2901280@qq.com"
# if re.match(pattern,email):
#     print("有效的邮箱地址")
# else:
#     print("无效的邮箱地址")
res = re.match(r"\d+","23hello,hello")
print(res.group())