pragma solidity ^0.4.0;

contract HelloWorld{
    bytes9 Myname = 0xe9a9ace4ba9ae8be89;
    bytes name = new bytes(2);
    bytes32 name1 = 0x7a68;
     function changeBytes16() view public returns(bytes12){
        return Myname;
    }
    function fixBytes() view public returns(bytes){
        // 函数内部声明需要memory
        bytes memory newName = new bytes(Myname.length);
        for(uint i = 0;i<Myname.length;i++){
            newName[i] = Myname[i];

        }
        return newName;
    }
    function init(){
        name[0]=0x7a;
        name[1]=0x68;
    }
    function changeToString() view public returns(string){
        bytes memory newName = new bytes(name1.length);
        for(uint i=0;i<name1.length;i++){
            newName[i] = name1[i];
        }
        return string(newName);

    }
}
