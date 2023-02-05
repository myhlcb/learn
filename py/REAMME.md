### 语言特性
id()查看内存
### 数据类型
* 可变类型 List + Set + Dict
* 不可变类型 String + Tunple + Number(int float bool complex)
#### 列表List
* 使用[],内置函数list()或者列表生成式
* 增append添加一个整体/extend添加多个/insert(index,val)/切片=>lis[0:4:2]
* 删 remove移除一个元素/pop()移除index/clear/del/切片
* 改 索引/切片
* 查 索引/获取单个/多个/in(not in)
* 排序 List.sort(reverse=True)/sorted(List,cmp,key,reverse)新建list
#### 集合Set
* 使用{},内置函数set{},集合生成式
* 增 add()一个/update()多个
* 删remove()不存在报错/discard()不存在不报错/pop() set.pop()是随机删除,因为set内容顺序不定/clear()
#### 字典Dict
* 使用{}/dict{}/字典生成式 ===>type({}),type(set({})) //dict和set
* 删 del dict[key]
* 改 dict[key] = val
* 查 dict[key] dict.get(key)
* 判断 in not in
* zip方法
#### 元组Tunple
* 使用() 使用内置函数tunple()
* 遍历 for in 
* 不可变序列
#### 字符串String
* 驻留  数字字母下划线相等;%之类不相等;sys.intern()强制驻留;
* index/rindex 不存在则报错，分别是正查/倒查
* find/rfind  不存在返回-1,分别是正查/倒查
* 字符串 print("我叫%s,今年%d岁" % (name,age))   print("我叫{0},今年{1}岁".format(name,age)) print(f"我叫{name},今年{age}岁")
* upper/lower  center/ljust/rjust  split/join  isidentifier/isdecimal replace  ord/chr  encode/decode
###  函数
* *关键字传参，params位置传参  => def ss(a,b,*,c,d) ss(1,2,3,4) #报错，从*开始必须用关键字传参  ss(1,2,d=3,c=4)
* *args params位置传参; **args必须关键字传参
* global 函数内使用全局作用域
### class面向对象编程
#### @staticmethod 
* 直接使用;也可以实例化对象使用;
* 调用类方法，静态方法可以直接使用
* 调用普通方法需要实例化
* 继承的子类直接使用
#### @classmethod 
* 直接使用;也可以实例化对象使用;
* 调用静态方法
* 调用其他方法，类方法
* 继承
#### 继承多个
### 运算符
### 内置模块

