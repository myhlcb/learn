# 切片
lis=[1,3,5,7,9]
print(id(lis[1]),lis.index(3),id(lis[lis.index(3)]))
print(lis[-3],lis[0:4:2],lis[0::2])#//切片
print(lis[::-1],lis[0:5:-1],lis[5:0:-1])#//负数
## 添加元素
lis=[1,3,5]
lis.append([7,9])
lis.extend([7,9])
lis.insert(1,90)#//索引，要添加的值
print(lis,11111111111111)
# 删除元素
lis.remove(7)#//删除val
print(lis,id(lis))
lis.pop(1)#//删除index
print(lis,id(lis))
lis.clear()#//清空列表
print(lis)
del lis #//删除列表
# print(lis) #//未定义
lis =[1,3,5,9,7]
lis.sort()#//默认升序排列
print(lis,id(lis))
lis.sort(reverse=True)#//降序排列
print(lis,id(lis),1111)
print(sorted(lis),id(sorted(lis,reverse=True)))

lis = [i*i for i in range(10)]
print(lis,list([3,5]))
