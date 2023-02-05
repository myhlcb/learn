# coding:utf-8
import keyword
from decimal import Decimal
print('hello')
fp=open('./1.txt',"a+")
print("hello world",file=fp)
fp.close()
print("hello\nworld")#//换行
print("hello\tworld")#//空格
print("hello\rworld")#//覆盖
print("hello\bworld")#//退格
print(r"hello\tworld")# //原始符

print(chr(0b100111001011000))
print(keyword.kwlist)
key="hello world"
a=key
print("内存地址",id(key))
print("内存地址",id(a))
print("类型",type(key))
print("值",key)
print(11,0b11,0o11,0x11)
print(Decimal('1.1')+Decimal('2.2'))
c= """
aaaaaaa
"""
print(c)
print(str(111),type(str(111)))
print(int("111"),type(int("111")))
print(float("111"),type(float("111")))

# present=input("想要什么礼物呢")
# print(present)
# a=input("加数1")
# b=input("加数2")
# print(Decimal(a)+Decimal(b))
print(1+1)
print(2*2)
print(11/2)
print(11//2)
print(11%2)
print(2**2)

a =b=[10]
c =[10 ]
print(a==b,a==c) #// 比值
print(a is b, b is c)# // 内存
a,b=1,2
print(a,b)
print(3 & 0,3 &1,3|0)#//按位
print (4 <<1,4>>1)#//移位
print(0b11,0o11,0x11,)
print(bool([]),bool({}),bool(0.0))

print(2 if 2>11 else 3)

if 2>3:
    pass
else:
    print(4)
# range 起始值 結束值 步長 
r = range(1,10,2)
print(list(r),set(r),11,10 in r,9 in r,8 not in r)
for i in range(10):
    print(i)

for item in range(100,1000):
    g=item%10
    s=item//10%10
    b=item//100
    if item==g**3+s**3+b**3:
        print(item)
        
i=0    
while(i<5):
    i+=1
    print(i)
else:
    print('i')
