# # r
# file = open('1.txt','r')
# print(file.readline())
# file.close()
# # w
# file2 = open('2.txt','a')
# file2.write('python')
# file.close()
# # rd
# file = open('1.jpg','rb')
# file2 = open('2.jpg','wb')
# file2.write(file.read())
# file.close()
# file2.close()

# # 使用with 无需close
# print(22222)
# with open('2.txt','r') as file:
#     print(1111,file.read())

class OpenFile(object):
    def show(self):
        print("调用show方法")
    def __enter__(self):
        print("调用enter方法")
    def __exit__(self,exc_type,exc_val,exc_tb):
        print("调用exit方法")

    
with OpenFile() as ff:
    print(ff.show())