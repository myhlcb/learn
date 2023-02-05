class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student():
    def __init__(self,info):
        self.info = info

p = Person('zhangs',10)
print(p.name,p.age)
s = Student('xxxx')
print(s.info)
# //继承多个
class A(Person,Student):
    def __init__(self, name, age,info):
        Person.__init__(self,name, age)
        Student.__init__(self,info)

a = A('zhangs', 10,'xxx')
print(a.name,a.age,a.info)
