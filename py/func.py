def ss(a,b):
    print(a,111,b)
ss(*(1,2))
ss(b=10,a=3) #按照关键字名字传参
    
#不确定参数个数
def ss(*args):
    print(args)
ss(1,2,3)
ss(*[1,2,3])
ss(*(1,2,3))
# 关键字传参
def ss(**args):
    print(args)
ss(a=10,b=20)

def ss(*args1,**args2):
    print(args1,111,args2)
ss(1,2,3,a=1,b=2)

def ss(a,b,*,c,d):
    print(a,b,c,d,)
# ss(1,2,3,4) #报错，从*开始必须用关键字传参
ss(1,2,d=3,c=4)

def ss(k):
    global l  #相当于全局作用域
    l = 10
    print(k,111,l)
ss(1)
print(l)
