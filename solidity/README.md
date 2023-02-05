## 结构
```
// https://remix.ethereum.org/
pragma solidity ^0.4.0
contract FunctionName{
    function name() view[pure] public returns(string[uint][bytes1]){
        
    }
}
```
## 函数
### public/internal/external/private 
* public/internal/external三个都可以继承
* public   可以被继承，可以内部调用，可以外部调用
* internal 可以被继承，不能外部调用，可以内部调用
* external 可以被继承，不能内部调用，可以外部调用
* private  不能被继承，不能外部调用，只能内部调用
* public字段实际上生成一个默认的external权限的函数，可以通过this.xx调用。
### pure/view/constant/payable
* pure不能读取全局变量，不能修改全局变量
* constant函数中等于view,全局变量使用int uint string bytes1-bytes32;
* view 读取全局变量，不能修改，不消耗gas
* payable 转账必须加
* 函数内部constant在5.0废弃,作用和view重合。全局变量还有用，防止被修改。
### 其他
* returns(types) 参数不同即可同名(重载); 返回值不同不能重载;
* 作用域:参数定义之后不能重新定义;
* modifier使用(类似装饰器)
* 多重modify 参照koa洋葱模型
```
pragma solidity ^0.4.0;

contract modifierTest{
    address public owner;
    uint public num=1;
    constructor()public {
        owner = msg.sender;
    }
    modifier OnlyOnwer{
        require(owner==msg.sender); //条件判断
        _;
    }
    function changeNum(uint _num)public OnlyOnwer{
        num = _num;
    }
}
```
## 构造函数与继承
* 合约内部使用使用construct(老版本constract同名即可) 
* 合约继承合约
* 合约内部可以new 调用旧合约;
* 合约销毁使用selfdestruct(销毁整个合约，即合约内部方法不能调用);
```
pragma solidity ^0.4.0;

contract A{
    uint public money = 10000;
    uint private money1 = 1000;
    uint public money2 = 100;
    uint internal money3 = 10;
    function addMoney() external returns(uint){
        return money2 + 1;
    }

}
contract B is A{
    function getMoney() view public returns(uint){
        return money;
    }
    function test() view public returns(uint){
       return this.addMoney();
    }
}
```
## 数据类型
* bytes + int/uint(默认256) + bool + string + address + mapping + array + struct + enum;
### bytes 
* bytes  bytes1~bytes16, 新建动态长度bytes new bytes(); 函数内使用加上memory;
* bytes1是固定长度，不能修改; bytes则是可变长度，可以修改;
* bytes() 字符串转byte;
### string
* string没有length，需要使用bytes()强制转换; string()可以转换动态长度为string;
### array
* 固定数组元素可以修改，可以获取长度；不能修改长度，不能push;
* 动态长度数组可以修改，可以获取长度(初始0)，初始空数组;可以修改长度,可以push;类似go切片
* 数组字面量，return根据第一个元素最小匹配
  ```
  returns(unit[2]) return [unit(1),2,3]
  ```
### address
* address 使用unit160存储。使用unit160(address)转换十进制;使用address转换为地址;
* payable开启转账; 默认是wei; 
* this.balance获取合约账户金额; address.balance(获取任意账户金额);
* account.transfer(报错和不报错) 和account.send(bool)
### struct类型
* struct是memory类型
* 函数返回struct有两种方式:1使用元组类型2.使用internal
### mapping
* mapping在结构体中可以不定义
* memory的对象不能操纵struct结构体中的mapping,需要用storage承接;
* 但是函数内部赋值需要使用memory类型,所以需要在函数外部定义
```
pragma solidity ^0.4.0;
contract structTest{
    struct student{
        uint grade;
        string name;
        mapping(int=>string) map;
    }
    student ss; // 默认storage类型; 只能用storeage类型操作memory类型
    function init() view public returns(uint,string,string){
        student memory s = student(10,"zhangs"); // 默认是storage类型，memory类型不能赋值给storage类型
        // s.map[0] = "111";    报错,memory的对象不能操纵struct结构体中的mapping;
        ss = s;
        ss.map[0] = "mapping";
        return (s.grade,s.name,ss.map[0]);
    }
}
```
### enum
* enum必须有成员,enum不能有汉字,不能有重复
* enum用来控制状态转移;
```
pragma solidity ^0.4.0;
contract structTest4{
    enum code{a,b,c}
    function init() view returns(code){
        return code.b; 
    }
}
```
## 全局变量
* block + msg
## 内存引用与持久化
* 值传递是新开辟空间,互不影响
* 函数体内部声明可变长度数组,其类型是storage类型
* struct,可变长度数组,可变长度bytes都是memory类型,不能赋值给storage类型;需要加上memory转换
```
pragma solidity ^0.4.0;
contract structTest{
    struct student{
        uint grade;
        string name;
    }
    function init(){
        student memory s = student(10,'zhangs'); // 默认是storage类型，memory类型不能赋值给storage类型
    }
}
```
### 区块链的值和内存中的值(两者完全独立)
* memory通过指针传递
* 区块链值拷贝
```
pragma solidity ^0.4.0;
// 传递指针
contract structTest{
    struct student{
        uint grade;
        string name;
        mapping(int=>string) map;
    }
    function init() view returns(string){
        student memory s = student(10,"zhangs");
        student memory s2 = s;
        s.name = "lisi";
        return s2.name; //lisi

    }
}
// 区块链值拷贝
contract structTest1{
    struct student{
        uint grade;
        string name;
        mapping(int=>string) map;
    }
    student stu;
    student stu1;
    function init(student storage s) view internal{
        s.name = "zhangs";
    }

    function call() view public returns(string){
        init(stu);
        stu1 = stu;  // zhangs
        stu.name = "lisi";
        return stu1.name; // zhangs
    }
}
// 区块链值拷贝
contract structTest2{
    struct student {
        uint grade;
        string name;
    }
    student stu =  student(100,"lisi");
    student stu2;
    function init(student memory s) internal {
        stu = s;
    }
    function call() view public returns(string){
        student memory s = student(10,"zhangs");
        init(s);
        stu2 = stu;
        s.name = "wangwu";
        stu2.name = "wanfgwu2";// 此处也没有转变为wangwu2,仍旧是zhangs
        return stu.name;  //zhangs
    }
}
// 区块链值拷贝
contract structTest3{
    struct student {
        uint grade;
        string name;
    }
    student stu =  student(100,"zhangs");
    student stu2;
    function init() view returns(string){
        stu2 = stu;
        stu2.name = "lisi"; // memory里面,所以stu还是zhangs; 
        return stu.name; //zhangs
    }
}
// 区块链值拷贝
contract structTest4{
    struct student {
        uint grade;
        string name;
    }
    student stu = student(100,"zhangs");
    student stu2 = stu;
    // stu2.name = "lisi"; // 不能这样赋值 Expected identifier but got '='
    function init() view returns(string){
        stu2.name = "lisi";
        return stu.name; //zhangs
    }
}
```