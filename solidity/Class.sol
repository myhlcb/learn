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