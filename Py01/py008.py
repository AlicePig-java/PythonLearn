#封装
# class Person:
#     name = "bigbing"
#     __age = 18#隐藏属性，外部不能通过直接调用age来调用，内部可以
#     def introduce(self):
#         print(f"{Person.name}的年龄是{Person.__age}")
# p = Person()
# print(p.name)
# p.introduce()
#
#
from gettext import dgettext
from pprint import pprint
from time import process_time_ns


# 私用属性和隐藏属性
# class Person:
#     name = "菠萝吹雪"
#     __age = 19  # 隐藏属性，外部不能通过直接调用age来调用，内部可以，外部如果要强行调用的话，需要使用p._Person__age
#     _sex = "人妖"  # 隐藏属性，外部可以调用，但内部不推荐调用，相当于君子协定，外部不推荐调用
#     def introduce(self):
#         print(f"{self.name}的年龄是{self.__age}")
# p = Person()
# print(p.name)
# print(p._sex)
#
#
# # 私有方法
# class Man:
#     name = "Man"
#     _age = 19
#
#     def __play(self):
#         print("私有方法")
#     def func(self):
#         print("普通示例方法")
#         self.__play()#内部可以直接调用私有方法，外部不能
#     def _wash(self):  # 单下滑线方法,实际是君子协定，带有单下滑线的方法外部最好不要调用，然后再导入的时候python也不会将其导入
#         print("单下滑线方法")
# man = Man()
# man.func()
# man._wash()


# python是允许多继承的，java只允许继承，但是能实现多个接口，这是为了避免砖石问题
# class Father:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def eat(self):
#         print(f"{self.name}的eat方法")
#     def sleep(self):
#         print(f"{self.name}的sleep方法")
#
# class Son(Father):
#     def study(self):
#         print("son在学习")
#     pass
#
# class Dauther(Father):
#     def dance(self):
#         print("daughter在跳舞")
#     pass
#
# son1 = Son("xiaoming",28)
# print(son1.name)
# print(son1.age)
# print()
# son1.eat()
# son1.sleep()
# print()
#
# son1.study()
# print()
#
# dauther1 = Dauther("xiaomei",26)
# print(dauther1.name)
# print(dauther1.age)
#
# print()
# dauther1.eat()
# dauther1.sleep()
#
# print()
# dauther1.dance()
# print()
#
# class grandson(Dauther,Son):
#     pass
#
# grandson1 = grandson("sunzi",2)
# print(grandson1.name)
# print(grandson1.age)
#
# class Father:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def eat(self):
#         print(f"{self.name}的eat方法")
#     def sleep(self):
#         print(f"{self.name}的sleep方法")
#
# class Son(Father):
#     def study(self):
#         print("son在学习")
#     def eat(self):
#         print("重写的子类吃饭方法")
#     pass
# son1 = Son("xiaomi",23)
# son1.eat()

#多台接口，可以gju传入的对象选择不同的方法
class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f"{self.name}" + "在吃饭")
class Cat(Animal):
    def eat(self):
        print(f"{self.name}"+"在吃猫粮")

class Dog(Animal):
    def eat(self):
        print(f"{self.name}" +"在吃猪饲料")

class Mouse(Animal):
    def hide(self):
        print(f"{self.name}" + "躲起来")
cat = Cat("cat")
dog = Dog("dog")
mouse = Mouse("mouse")
# 会根据闯入的类型有没有重写方法，来调用对应的方法
def test(Object):
    Object.eat()
test(cat)
test(dog)
test(mouse)
mouse.hide()