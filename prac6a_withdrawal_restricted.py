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

//withdrawal acess 
// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.4;

contract SendContract {
    address payable public richest;
    uint256 public mostSent;
    /// The amount of Ether sent was not higher than
    /// the currently highest amount.
    error NotEnoughEther();

    constructor() payable {
        richest = payable(msg.sender);
        mostSent = msg.value;
    }

    function becomeRichest() public payable {
        if (msg.value <= mostSent) revert NotEnoughEther();
        // This line can cause problems (explained below).
        richest.transfer(msg.value);
        richest = payable(msg.sender);
        mostSent = msg.value;
    }
}

//Restricted Access
// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.4;

contract AccessRestriction {
    // These will be assigned at the construction
    // phase, where `msg.sender` is the account
    // creating this contract.
    address public owner = msg.sender;
    uint256 public creationTime = block.timestamp;
    // Now follows a list of errors that
    // this contract can generate together
    // with a textual explanation in special
    // comments.
    /// Sender not authorized for this
    /// operation.
    error Unauthorized();
    /// Function called too early.
    error TooEarly();
    /// Not enough Ether sent with function call.
    error NotEnoughEther();
    // Modifiers can be used to change
    // the body of a function.
    // If this modifier is used, it will
    // prepend a check that only passes
    // if the function is called from
    // a certain address.
    modifier onlyBy(address account) {
        if (msg.sender != account) revert Unauthorized();
        // Do not forget the "_;"! It will
        // be replaced by the actual function
        // body when the modifier is used.
        _;
    }

    /// Make `newOwner` the new owner of this
    /// contract.
    function changeOwner(address newOwner) public onlyBy(owner) {
        owner = newOwner;
    }

    modifier onlyAfter(uint256 time) {
        if (block.timestamp < time) revert TooEarly();
        _;
    }

    /// Erase ownership information.
    /// May only be called 6 weeks after
    /// the contract has been created.
    function disown() public onlyBy(owner) onlyAfter(creationTime + 6 weeks) {
        delete owner;
    }

    // This modifier requires a certain
    // fee being associated with a function call.
    // If the caller sent too much, he or she is
    // refunded, but only after the function body.
    // This was dangerous before Solidity version 0.4.0,
    // where it was possible to skip the part after `_;`.
    modifier costs(uint256 amount) {
        if (msg.value < amount) revert NotEnoughEther();
        _;
        if (msg.value > amount)
            payable(msg.sender).transfer(msg.value - amount);
    }

    function forceOwnerChange(address newOwner)
        public
        payable
        costs(200 ether)
    {
        owner = newOwner;
        // just some example condition
        if (uint160(owner) & 0 == 1)
            // This did not refund for Solidity
            // before version 0.4.0.
            return;
        // refund overpaid fees
    }
}
