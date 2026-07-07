# #拆包
# # turp = (1,2,3,4)
# # print(turp)
# # print(turp[0])
# # a,b,c,d = turp #拆包过程
# # print(a,b,c,d)
# # print("a=",a,"b=",b,"c=",c,"d=",d)
# # for i in turp:
# #     print(i)
#
# # turp = (1,2,3,4)
# # a, *b = turp
# # print(a,b)
# # print(b,type(b))
#
# # # 三目运算符号
# # a = input("请输入a的值：")
# # b = input("请输入b的值：")
# # print("a小于b") if a < b else print("a大于b")
#
#
# # 自定义异常和捕获异常
# def login():
#     pwd = input("请输入你的密码：")
#     if len(pwd) >= 6:
#         return "密码输入成功"
#     else:
#         raise Exception("密码长度小于六位数")
# # print(login())
# try:
#     login()
# except Exception as e:
#     print(e)
#
#

# 导入模块
# import test_module
# print(test_module.name)
# test_module.funa()
# from test_module import funa as test_funa #从某模块导入函数，并用as关键字来
# test_funa()

from pack_01 import *
register.reg()
login.login()
