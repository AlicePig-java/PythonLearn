# #关于python的迭代器 iter
# # list = [1,2,3,4,5,6]
# # i1 = iter(list)
# # while True:
# #     try :
# #         print(next(i1))
# #     except StopIteration:
# #         break
#
#
# def func_A():
#     print("被装饰的业务逻辑")
# #装饰器
# def my_deractor(fn):
#     def inner():
#         print("装饰前逻辑：")
#         fn()#需要用到外层的变量
#         print("装饰后逻辑")
#     return inner#返回的是内层函数名
# print(my_deractor(func_A))
# ot = my_deractor(func_A)
# ot()
#
#  #通过语法糖来进行装饰函数
#  # 装饰器函数
#  def outer2(fn):
#      def inner():
#          print("装饰前逻辑")
#          fn()
#      return inner
#  # 被装饰的函数
#  @outer2
#  def study():
#      print("在学习python")
#
#  study()
#
# 通过语法糖来进行装饰函数 带参数
#  装饰器函数
# def outer2(fn):
#     def inner(name):
#         print("装饰前逻辑")
#         print(f"{name}是冰冰的函数")
#         fn(name)
#     return inner
# # 被装饰的函数
# @outer2
# def study(name):
#     print("在学习python")
# study("bingbing")
#
# # 多个参数的装饰器函数
# @outer#语法糖侵入
# def send(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# def outer(fn):
#     def inner(*args,**kwargs):
#         print("登陆。。。")
#         fn(*args,**kwargs)
#     return inner
#
# ot = outer(send)
# ot("123",name = "bingbing",age = 19)
# class Washer:
#
#     def __init__(self,width,height):
#         self.Width = width
#         self.Height = height
#     def wash(self):
#         print("washing...")
#
# washer1 = Washer(600,300)
# print(washer1.Width)
# print(washer1.Height)
# washer1.wash()
#
# washer1.time = 2000
# print(washer1.time)
# print(washer1.__dict__)
# print(Washer.__dict__)
#

class Person:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def study(self):
        print(self.name + " is studying...")

    def eat(self):
        print(self.name +" is eating...")

p1 = Person("bingbing",18,"female")
p2 = Person("xiaoming",22,"male")
print(p1.name,p1.age,p1.sex)
print(p2.name,p2.age,p2.sex)
print()
p1.study()
p1.eat()
print()
p2.study()
p2.eat()


