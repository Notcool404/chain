// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.11;

contract Sender {
   uint public amount;
   address payable owner;

   constructor (){
     owner = payable(msg.sender); // set the deployer of contract as the owner
   }
   function sendEth(address payable receiver) payable public{
     require(owner == msg.sender, "Only the owner can send funds");
     amount = msg.value;
     receiver.transfer(amount);
}
}
