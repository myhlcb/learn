pragma solidity ^0.4.0;
contract structTest4{
    enum code{a,b,c}
    function init() view returns(code){
        return code.b; 
    }
}