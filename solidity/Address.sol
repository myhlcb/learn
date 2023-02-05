pragma solidity ^0.4.0;
contract addressTest{
    address public account = 0x5B38Da6a701c568545dCfcB03FcB875f56beddC4;
    // 0x26a77595Aa80350af52A14116E197E53b8B92601

  function changeInt() view public returns(uint160){
      return uint8(0x5B);
  }
  function changeAddr() view public returns(address){
      return address(uint160(account));
  }
  function getAddr(address _addr) view public returns(address,address,address){
    return (_addr,msg.sender,this);
  }
}
