# Solidity
# 6a
pragma solidity ^0.5.0;
contract SolidityTest {
uint storedData; // State variable
uint public a=10;
constructor() public {
storedData = 10;
}
function getResult(uint c) public view returns(uint){
uint a = 1; // local variable
uint b = 2;
uint result = a + b;
return result; //access the state variable
}
}
