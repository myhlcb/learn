#字符串驻留(数字字母下划线+单独%)
import sys
s1=''
s2=''
print(s1 is s2)
s1='%'
s2='%'
print(s1 is s2)
s1='123%'
s1='123%'
print(s1 is s2)
s1=sys.intern(s2)#强制驻留
print(s1 is s2,1111111)
s1 = 'abc'
s2='a'+'bc'
s3=''.join(['a','bc'])
print(s1 is s2,s1 is s3)

#查询
s1 = 'abcdabc'
s1.index('a'), #index不存在则报错
print(s1.rindex('a'),22222),
print(s1.find('w'),1111111),# find不存在不报错
print(s1.rfind('a'),3333333333333)

#转换
s1 = 'aBc,ABC'
#全大 全小 大小交换 首大
print(s1.upper(),111,
s1.lower(),222,
s1.swapcase(),333,
s1.capitalize(),44, #//第一个字母开头大写
s1.title())#所有字母开头大写

s = "hello World"
# 居中，左右 不够返回原字符
print(s.center(20,'*'))
print(s.ljust(2,'*'))
print(s.rjust(20,'*'))

#分割
s='he|ll|o Wo|rld'
print(s.split(),11,s.split('|'),22,s.split(sep='|',maxsplit=2),33,s.split('|',2))

#是否合法(数字字母下划线)
s= 'hello World'
print(s.isidentifier(),111,s.isalpha())

#替换与合并
s= 'hello Python'
print(s,11,s.replace('Python','Java'))
print(''.join(['abc','def']))

#比较
print(ord('马'),chr(39532))

##占位符
name="zhangs"
age=10
print("我叫%s,今年%d岁" % (name,age))
print("我叫{0},今年{1}岁".format(name,age))
print(f"我叫{name},今年{age}岁")
print("%10.3f" %(3.14)) #宽度10，小数点后3位

##编码
s="吃喝玩儿乐"
print(s.encode('GBK'),111,s.encode('UTF-8'))
b = s.encode('GBK')
print(b.decode('GBK'))