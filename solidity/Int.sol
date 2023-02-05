pragma solidity ^0.4.0;

contract IntTest{
    int num1 = 100; // int256 = int
    uint num2 = 200; // uint256 = uint
    function add(uint a, uint b) pure public  returns(uint){
        return a + b;
    }
    function change(uint a,uint b) pure public returns(uint){
        return a & b;
    }
        function change1(uint a,uint b) pure public returns(uint){
        return a | b;
    }
    function change2(uint a,uint b) pure public returns(uint){
        return a ^ b;
    }
    function change3(uint8 a) pure public returns(uint){
        return ~a;
    }
     function change4(uint8 a) pure public returns(uint){
        return a>>1;
    }
    function flow() pure public returns(uint){
        uint8 mm = 255;
        mm++;
        return mm;
    }
    function ss() pure public returns(uint){
        uint num = 11111111111111111111111111111111111111111111111111111111111111111;
        return num;
    }

}