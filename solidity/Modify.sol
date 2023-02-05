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