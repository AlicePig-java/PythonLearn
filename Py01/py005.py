#测试是否能在外部调用函数内部定义的函数
# def study():
#     print("我在学习",end="")
#     def course():
#         print("python")
#     course()
# study()

#
# from py004 import course
#
# def study():
#     print("我在学习",end="")
#     def course():
#         print("python")
#     course()
# study()
#
# course()#无法直接调用内函数，系统会从其他文件中导入同名的函数
#
#

#
# from Test导入覆盖 import study
# def study():
#     print("py005函数")
#
# study()

#后面导入的函数会覆盖原先的函数
#
# def study():
#     print("py005函数")
#
# from Test导入覆盖 import study
# study()
#
#
# a = 120
# def test_a():
#     print(f"a = {a}")
# test_a()
#

# lambda表达式
# def func_a(a,b):
#     return a + b
# print(func_a(1,2))
#
# funa = lambda a,b:a + b
# print(funa(1,2))
#
# # 可变参数lambda
# funb = lambda **kwargs : kwargs
# print(funb(name = "bingbing",age = 18,sex = "female"))
#
# a = 5
# b = 8
# print("a比b小") if a<b else print("a比b大")
#
# coump = lambda a,b : "a比b小" if a < b else "a比b大"
# print(coump(8,5))

#
# print(min(1,2,3))
# print(max(1,2,3))
# print(max("1","2","4"))
# print(max("a","B","c"))
#
# l1 = [1,2,3]
# l2 = ["a","b","c"]
# print(zip(l1,l2))
# for i in zip(l1,l2):
#     print(i,type(i))
# print(list(zip(l1,l2)))

l1 = [1,2,3,4]
def func(a):
    return a**5
miji = map(func,l1)
print(miji)
for i in miji:
    print(i)

