s = {'name','age'}
s1 = set({'name','age'})
s2=set({'name','age','name','a','b','c','d'}) #不能重复
print(s,s1,s2,set(range(5)))

# 定义空集合
print(type({}),type(set({}))) #dict set
print("name" in s2)
# 添加
s2.add("address")#添加
print(s2)
s2.update(["name","age","class"])#添加多个
print(s2)

#删除
s2.remove("age")#删除，删除不存在报错
s2.discard("city") #不报错
print(s2,2222222)
s2.pop()#删除第一个
print(s2,1111111)
# list pop删除最后一个  set pop删除随机一个
print([1,2,3,4,5].pop(),111,set({1,2,3,4,5}).pop())

"""两个集合的方法"""

s1 = {1,3,5,7,9}
s2 = {1,2,3,4,5}
s3 = {1,3,5,7,9}

print(s1==s2,s1==s3)
print(s1.issuperset(s3))#子集
print(s1.issuperset(s3))#超集
print(s2.isdisjoint(s1))#是否没有交集  false(有交集)

#数学操作
print(s1.intersection(s2),s1 & s2) #交集
print(s1.union(s2),s1 | s2)#并集
print(s1.difference(s2),s1-s2)#差集
print(s1.symmetric_difference(s2),s1^s2)#对称差集

#生成式
print({i*i for i in range(10)})