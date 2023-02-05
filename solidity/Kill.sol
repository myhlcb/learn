pragma solidity ^0.4.0;
contract killTest{
    uint public money = 100;
    address public owner;
    constructor()public{
        owner = msg.sender;
    }
    function  increMoney() public{
        money+=10;
    }
    function kill() public{
        if(owner == msg.sender){
            selfdestruct(owner);
        }
    }
}