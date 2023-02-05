pragma solidity ^0.4.0;

contract payTest{
    function pay() payable{

    }
    function getBalance() view public returns(uint){
        return this.balance;
    }
        function getBalance1(address account) view public returns(uint){
        return account.balance;
    }
    function trtansfer () payable{
        this.transfer(msg.value);
    }
        function trtansfer1 () payable{
            address account = 0x4B20993Bc481177ec7E8f571ceCaE8A9e22C02db;
        account.transfer(10 ether);
    }
    function() payable{

    }
}