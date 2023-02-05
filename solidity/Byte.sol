pragma solidity ^0.4.0;

contract IntTest{
    bytes1 public num1 = 0x1;
    bytes12 ss = 0x1;
    uint public nnum = 10;
    uint public aa = 0x1;
    bytes name = new bytes(4);
    function getLength() view public returns(uint){
        return ss.length;
    }
    function getLength1() pure public returns(uint){
        bytes13 sss = 12;
        return sss.length;
    }
    function getss() view public returns(bytes1){
        return num1;
    }
    function init() public {
        name[0]=0x9;
        name[1]=0x7a;
        name.push(0x2);
        name.push(0x3);
    }
     function change() view public returns(bytes) {
        return name;
    }
}