pragma solidity ^0.4.0;

contract mappintTest{
    mapping(address=>uint) idmapping;
    mapping(uint=>string) namemapping;
    uint sum= 0;
    function register(string name) public {
        address account = msg.sender;
        idmapping[account] = sum;
        sum++;
        namemapping[sum] = name;

    }
    function getSum() view public returns(uint){
        return sum;
    }

      function getIdByName(address account) view public returns(uint){
        return idmapping[account];

    }
    function getNameById(uint id) view public returns(string){
        return namemapping[id];
    }
}