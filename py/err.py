# 错误捕获
try:
    num=input("请输入")
    num1 = input("请输入")
    print(int(num)/num1)
except TypeError:
    print('0b11')
except ZeroDivisionError:
    print('22222')
except SyntaxError:
    print(3333)
except ValueError:
    print(444)
else:
    print("计算完毕")
finally:
    print(2222222)