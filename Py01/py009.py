#对于__new__ 方法和__init__方法
# class Person:
#     name = "xiaoming"#类属性
#
#     def __init__(self):
#         self.age = 19#实例属性
#
#     def __new__(cls, *args, **kwargs):
#         print("重写了object中的new方法")#重写new方法必须要手动返回object中的new方法引用，不然会导致对象初始化引用没有获取到
#         return  super().__new__(cls)
#
#     def introduce(self):
#         print(f"{Person.name}:{self.age}")#实例方法
# p1 = Person()
# print("p1:",p1)
# p1.introduce()
#
#
# class Person:
#     def __new__(cls, *args, **kwargs):
#         print("重写了new方法")
#         return super().__new__(cls)
#
#     def __init__(self,name = None):
#         print("名字是：",name)
#
# p1 = Person("xiaomi")
# p2 = Person("xiaohong")

# 单例模式
#通过重写__new__ 方法实现单例模式
# class SingleTon(object):
#     _instance = None
#     def __new__(cls, *args, **kwargs):
#         print("创建单例")
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance
#     def __init__(self):
#         print("init()方法")
#
# s1 = SingleTon()
# print("s1",s1)
# s2 = SingleTon()
# print("s2",s2)
#
#
# # 通过装饰器实现
# def SingleTon1(cls):
#     instance = {}
#     def wrapper(*args,**kwargs):
#         if cls not in instance:
#             instance[cls] = cls(*args,**kwargs)
#         return instance[cls]
#     return wrapper
#
# @SingleTon1
# class User:
#     pass
# a = User()
# b = User()
# print("a",a)
# print("b",b)


# 文件读取操作
# f = open("test.txt")
# try :
#     print(f.read())
#     print(f.closed)
# finally:
#     f.close()
#
# print(f.closed)
# /Users/Admin/Desktop/PythonTest/Test01.rtf

# f = open(r"/Users/Admin/Desktop/PythonTest/晒鸟苹果OS.txt")
# try :
#     print(f.read(4))
#     print(f.closed)
# finally:
#     f.close()
# print(f.closed)
# f = open("test.txt")
# try:
#     while True:
#         text = f.readline()
#         # not 是逻辑非关键字。readline() 读到文件末尾返回空字符串 ''，其布尔值为 False。
#         # if not text: 即判断 text 是否为空，若为空则说明已读到文件末尾，执行 break 结束循环。
#         if not text:
#             break
#         print(text,end="")
# finally:
#     f.close()

# 读取二进制文件操作
# with open("/Users/Admin/Desktop/灰白.png","rb") as file :
#     text = file.read()
#     print(text)
#
# # 将读取到内容写入
# with open("test.png","wb") as f:
#     f.write(text)
#
# name = "bingbing"
# print(type(name))


from collections.abc import Iterator,Iterable
# name = "bingbing"
# print(isinstance(name,Iterable))
# print(isinstance(name,Iterator))
# name1 = iter(name)
# print(isinstance(name1,Iterator))
#
#
#
# # 自定义迭代器
# class MyIterator:
#     def __init__(self):
#         self.x = 1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         a = self.x
#         if a > 10:
#             raise StopIteration("迭代结束")
#         self.x += 1
#         print(a)
# myItrator = MyIterator()
# for i in myItrator:
#     myItrator.__next__()
#
