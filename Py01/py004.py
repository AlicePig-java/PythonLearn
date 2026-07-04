# print(str("-1.8"))


"""
# 深拷贝和浅拷贝
# 导入拷贝模块
import copy

li = [1,2,3,4,[1,2,3]]
print(f"li:{li}")
print(id(li))
# 打印嵌套列表内层列表的地址 发现内层列表的地址是一致的，因为嵌套列表只会拷贝第一层，内层的还是共享的
print(id(li[4]))
print()
l2 = copy.copy(li)
print(f"l2:{l2}")
print(id(l2))
print(id(li[4]))

print("添加元素后")
li.append(8)
print(f"li:{li}")
print(f"l2:{l2}")

print("修改内层列表的值")
li[4][0] = 'a'
print(f"li:{li}")
print(f"l2:{l2}")

# 深拷贝
l3 = copy.deepcopy(li)
print(f"l3:{l3}")



def say_hello():
    return("你好呀，勇敢的冒险家")
str = say_hello()
print(str,type(str))

def print_line():
    return "我喜欢","小白"
print(print_line(),type(print_line()))


# 传参数
def add(x,y):
    return x + y
print(add(200,50))


#可变参数需要注意*args
def func(*args):
    print(args)
func(1,2,3)#会以元组的形式接收

def func1(args):#如果没有加*号就是普通的参数
    print(args)
func1(1)
"""

#关键参数
def func_a(**kwargs):
    if "name" in kwargs:
        print("hello " + kwargs["name"])
    if kwargs.__contains__("age"):
        print("age " + str(kwargs["age"]))
    print(kwargs)
func_a(name = "bingbing",age = 18,sex = "female")



#函数嵌套调用
def study():
    print("在学习",end="")
def course():
    study()
    print("python")
course()