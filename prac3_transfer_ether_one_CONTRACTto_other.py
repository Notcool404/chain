pragma solidity ^0.8.0;
contract sendEther{
function getBalance() external view returns(uint)
{
    return address(this).balance;
}
receive() external payable { }
}
