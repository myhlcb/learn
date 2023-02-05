pragma solidity ^0.4.0;

contract BooleanTest{
    bool a = false;
    int num1 = 100;
    int num2 = 200;
    function getBool() returns(bool){
        return !a;
    }
    function panduan() returns(bool){
        return num1 == num2;
    }
}