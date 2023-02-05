pragma solidity ^0.4.0;

contract Array{
    uint[5] arr1 = [1,2];
    uint[] arr2 = [2,3,4];

    function getLength() view public returns(uint){
        return arr1.length;
    }
        function getLength1 ()view public returns(uint){
        return arr2.length;
    }
    function changeLength() {
        arr2.length = 2;
        arr2.push(7);
    }
    function getContent() view public returns(uint[]){
        return arr2;
    }
}