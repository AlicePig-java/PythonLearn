

"""
age = int(input("请输入求职者的年龄："))
female = int(input("请输入求职者的性别:"))
if age < 18 :
    print("年龄过小，不符合要求")
elif age >= 45 :
    if female == 1:
        print("年龄过大，不符合要求")
elif age >= 45 :
    if female == 0:
        print("年龄大，女生，保留意见")
else :
    print("适龄简历，进入人才库")


#一次性输入多个参数
name1,name2,name3 = input("请输入三个姓名：").split()
print(name1)
print(name2)
print(name3)
"""
"""
# 循环练习
var1 = 100
while var1 > 0:
    print("好好学习，天天向上 %d次数" %var1)
    var1 -= 1

while False:
    print("我真傻，冬天来了。。。。")
"""
#
# # 嵌套循环
# i = 3
# while i >= 1:
#     print(f"这是第{i}次外循环")
#     j = 3
#     while j >= 1:
#         print(f"这是第{i}次外循环的第{j}次内循环")
#         j -= 1
#     i -= 1


# fruits = ["apple","banana","pear","watermelen"]
# for i in range(len(fruits)):
#     print(fruits[i])
#
# for i in fruits:
#     print(fruits)
#
# sum = 0
# for i in range(1,101):
#     print(i)
#     sum += i
# print(sum)

#
# name1 = "小猪"
# name2 = "佩奇"
# print(name1,name2,sep="")
# print(name1,name2,sep=" ")
#
# st = "abcdefghjk"
# print(st[0:])
# print(st[-1:0])
#
# print(st[-1:-5:-1])


# print("\a")#响铃声音

mystr= "xiaoziwoxihuanni"
print(mystr[-1::-1])

#replace函数
str1 = "好好学习，天天向上"
print(str1)
str2 = str1.replace("天","时")
print(str2)