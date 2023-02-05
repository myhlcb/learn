pragma solidity ^0.4.0;

contract funcTest{
    uint public num;
    string public name;
    function setParams(uint _num,string _name) public {
        num = _num;
        name = _name;
    }
    function test() public {
        setParams(10,"zhangs");
    }
    function test1() public {
        setParams({_name:"lisi",_num:3});
    }
    function test2(uint a,uint b) view  returns(uint add,uint mul){
        add = a + b;
        mul = a * b;
    }
}