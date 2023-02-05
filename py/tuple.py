# 不可变序列  没有增删改操作 字符串和元祖
# 可变序列  数组 字典 集合

t =(1,2,3)
print(type(t))
t = tuple((1,2,3))
print(t)
t=1,2,3
print(t,type(t))
# 单对象元组，逗号不能省
print(type((10)),type((10,))) 

print([],list(),111,{},dict(),222,(),tuple())

t=(1,[2,3],4)
# t[0]=2 报错,元组不可变

# 遍历
t =(2,3,6,2)
print(t[2])

for item in t:
    print(item)
