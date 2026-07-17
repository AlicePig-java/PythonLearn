#匹配规则测试
import re
res = re.match(r'\w*', "xiaomingyaochifan")
print(res.group())
"""
* 表示匹配前一个字符0次或者无数次
+ 表示匹配前一个字符至少匹配一次
？ 表示匹配前一个字符出现1次或者0次
{m} 匹配前一个字符出现m次
{m,n} 表示匹配前一个字符 m-n次
"""
res1 = re.match(r"\d*","123bingbing")
print(res1.group())

res2 = re.match(r"\d{2}","123bingbing")
print(res2.group())

res3 = re.match(r"\w{4,10}","bingbingnihaoma")
print(res3.group())
