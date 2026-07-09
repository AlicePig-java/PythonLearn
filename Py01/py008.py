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

# 私用属性和隐藏属性
class Person:
    name = "菠萝吹雪"
    __age = 19  # 隐藏属性，外部不能通过直接调用age来调用，内部可以，外部如果要强行调用的话，需要使用p._Person__age
    _sex = "人妖"  # 隐藏属性，外部可以调用，但内部不推荐调用，相当于君子协定，外部不推荐调用
    def introduce(self):
        print(f"{self.name}的年龄是{self.__age}")
p = Person()
print(p.name)
print(p._sex)


# 私有方法
class Man:
    name = "Man"
    _age = 19

    def __play(self):
        print("私有方法")
    def func(self):
        print("普通示例方法")
        self.__play()#内部可以直接调用私有方法，外部不能
    def _wash(self):  # 单下滑线方法,实际是君子协定，带有单下滑线的方法外部最好不要调用，然后再导入的时候python也不会将其导入
        print("单下滑线方法")
man = Man()
man.func()
man._wash()