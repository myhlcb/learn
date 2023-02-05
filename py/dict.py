# key是不可变对象(字符串)
score1 = {"name":"zhangs","age":14}
print(score1)
score = dict(name="zhangs",age=14)
print(score)

print(score1==score,score1 is score,
score.get("name"),score["name"],score.get("names"),"name" in  score)
# score["names"]报错
# del score["name"] 删除key
# print(score)
# score.clear()
# print(score)

print(score.keys(),score.values(),score.items())
l=list(score.items())
print(l,type(l))

list1 = ["fruit","book","other"]
list2 = [96,97,98]
d = {key:val for key,val in zip(list1,list2)}
print(d)