class Student:
    def __init__(self):
        self.addr="china"
    def eat(self):
        print(self.addr)
    @staticmethod
    def method():
        print("静态方法")
    @classmethod
    def cm(cls):
        cls.method()
        Student.method()
        print(cls)
stu = Student()
print(stu.addr)
stu.eat()
Student.eat(stu)#需要参数
stu.cm()
stu.method()
print(11111111111)
Student.cm()#自动加参数
Student.method()
