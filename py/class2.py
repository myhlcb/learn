class Car:
    def __init__(self,bread,age):
        self.bread = bread
        self.__age = age
    def show(self):
        print(self.bread,self.__age)
    @classmethod
    def cc(cls):
        print('xxxxx')
    @staticmethod
    def ss():
        print('gogogo')

c = Car("宝马",10)
print(c.bread,c.show(),dir(c))
c.cc()
c.ss()
Car.cc()
Car.ss()