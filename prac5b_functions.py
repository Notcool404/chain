
#type of function(view, pure)
pragma solidity ^0.5.0;
contract Test {
int public x=10; //global
int y=90;//state
function f1() public returns(int){
    //read and update is allowed
    x=100;
return x;
}
function f2() public view returns(int){
  //  x=100; //erro beacuse x is global/state
  //we can access but we cannot update state or global variable int view function
return x;
}
function f3() public pure returns(int){
    //we cannot access or update state or global variable in pure function
    int z=80;
return z;
}


}



#function overloading
pragma solidity ^0.5.0;
contract Test {
function getSum(uint a, uint b) public pure returns(uint){
return a + b;
}
function getSum(uint a, uint b, uint c ) public pure returns(uint){
return a + b + c;
}
}

#mathematical function
pragma solidity ^0.5.0;


contract Test {
function callAddMod() public pure returns(uint){
return addmod(4, 5, 3);
}
function callMulMod() public pure returns(uint){
return mulmod(4, 5, 3);
}
}



#cryptographic function 
pragma solidity ^0.5.0;
contract Test {
function callKeccak256() public pure returns(bytes32 result){
return keccak256("ABC");
}
}