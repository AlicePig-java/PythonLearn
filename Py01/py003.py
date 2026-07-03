# my_list = [1,2,3]
# list2 = ["a","b","c"]
# # my_list.extend(4)
# # 上一行代码会报错，因为extend函数后面必须是可迭代的类型，比如说字符串或者集合那些
# my_list.extend(list2)#list2 是可迭代的类型数据
# print(my_list)
#
#
# # list可以直接通过下标的方式直接修改list中的元素
# list2[2] = 1
# print(list2)
#
# # 直接判断是否存在还是不存在
# print('a' in list2)
# print(2 in list2)
from itertools import count
from subprocess import check_output

# name = input("请输入您的昵称：")
# list_cc = ["小王","小红","小李子"]
# if name not in list_cc:
#     print("对不起，您有没有权限查看")
# else :
#     print("欢迎回来")

# pop（）函数会删除列表的最后一个元素
# list_remove = ["a","b","c","d","b"]
# print(list_remove)
# list_remove.remove("b")
# print(list_remove)
# try:
#     list_remove.remove("t")
# except:
#     print("不存在该元素")
#
# # remove只会删除第一个出现的元素
# list_while_remove = ["a","b","c","d","b"]
# print(list_while_remove)
# while "b" in list_while_remove:
#     list_while_remove.remove("b")
# print(list_while_remove)

#
# li = []
# [li.append(i) for i in range(1,6)]
# print(li)

# [li.pop() for i in range(len(li))]
# print(li)
#
# [li.remove(i) for i in range(len(li) + 1) if i % 2 != 0]
# print(li)

#
# # 列表嵌套
# list_test = [1, 2, 3, 4, [5, 6, 7]]
# print(list_test)
# for i in range(len(list_test)):
#     # 判断当前元素是否为列表，如果是则使用内层循环遍历
#     if isinstance(list_test[i], list):
#         for j in range(len(list_test[i])):
#             print(list_test[i][j])
#     else:
#         # 如果不是列表（如整数），则直接打印该元素
#         print(list_test[i])
#
#
#
# 元组1 = (1,2,3,4,5)
# 元组2 = (1)
# print(type(元组1))
# print(type(元组2))#因为单元素下必须要在末尾加上，符号，否则会被识别为整数
#
# dict = {"name": "bingbing","age" : "18","name":"xiaolizi"}
# print(dict)
#
# # 新增字典元素
# dict["remark"] = "我是大好人"
# print(dict)
# #如果已经存在则会直接修改元素
# #修改字典元素
# dict["remark"] = "我是舔狗"
# print(dict)
# #通过key去修改元素
# dict.pop("name")
# print(dict)

#删除操作
# dict = {"name": "bingbing","age" : "18","name":"xiaolizi","female":"woman","hobbys":"coding"}
# print(dict)
# 删除最后一个
# dict.popitem()
# print(dict)

# clear函数  直接清空
# dict.clear()
# print(dict)
#
# # pop函数
# try:
#     dict.pop("xiaozhi")#不存在会报错
# except:
#     print("键不存在")
# dict.pop("name")
# print(dict)
#
#
# print("字典的长度为：" + str(len(dict)))
# print(dict.keys())
# print(dict.values())
#
# #items可以获取所有的键值对，并且以元组的形式返回
# print(dict.items())
# for i in dict.items():
#     print(i,type(i))

# 集合
set = {1,2,3,4,5,6,'1','3',7,2,3,4}
print(set)


set1 = {'1','2','3','4','5','1'}
print(set1)