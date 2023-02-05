# 多态
class A:
    def eat(self):
        print("吃")
class B(A):
    def eat(self):
        print("吃鱼")

class C(A):
    def eat(self):
        print("吃肉")

def fun(cl):
    cl.eat()

fun(A())
fun(B())
fun(C())
a = 1
b =2
print(a+b,a.__add__(b))
class Student:
    def __init__(self,name):
        self.name = name
    def __add__(self,other):#实现str相加
        return self.name + other.name
    def __str__(self): #//重写str
        return 'xxxx'
s1 = Student('zhangs')
s2 =Student('lisi')
print(s1+s2,s1.__add__(s2))
print(s1)
