pragma solidity ^0.4.0;

contract HelloWorld{
    string Myname = "中国";

    function getName() view public  returns(string)
    {
        return Myname;
    }
    function getLength() view public returns(uint){
        // return Myname[0];
        // return Myname.length;
        return bytes(Myname).length;
    }
            function getLength1() view public returns(bytes1) {
        // return Myname[0];
        // return Myname.length;
        return bytes(Myname)[1];
    }
        function getLength2() view  public returns(bytes) {
        // return Myname[0];
        // return Myname.length;
        return bytes(Myname);
    }
}
