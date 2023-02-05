pragma solidity ^0.4.0;

contract HelloWorld{
    string Myname = "zhangs";

    function getName() view public  returns(string)
    {
        return Myname;
    }
    function changeName(string newName) public {
        Myname = newName;
    }
    function pureTest(string newName) pure public returns(string){
        return newName;
    }
}
