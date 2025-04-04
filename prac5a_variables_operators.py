#types of variable
pragma solidity ^0.5.0;
contract Pract1{
int x=15; //state var
int public y=10;//global
function getValue(int z) public{
y=y+z;
}

function show() public view returns (int)
{
return x;
}
}

#relational operators
pragma solidity ^0.5.0;
contract Pract2{
bool public a=true;
bool  public b=false;
bool public  r1or=a||b;
bool public r2and=a&&b;
bool public r3not=!b;
}

#for loop
pragma solidity ^0.5.0;
contract Pract3{
function test(int s, int e) public view returns(int)
{
int i;
int sum=0;
for(i=s;i<=e;i++)
{
sum+=i;  //sum=sum+i;
}
return sum;
}
}

#while loop
pragma solidity ^0.5.0;
contract Pract3{
function test(int s, int e) public view returns(int)
{
int i;
int sum=0;
i=s;
while(i<=e)
{
sum+=i;  //sum=sum+i;
i++;
}
return sum;
}
}

#do while loop
pragma solidity ^0.5.0;
contract Pract3{
function test(int s, int e) public view returns(int)
{
int i;
int sum=0;
i=s;
do
{
sum+=i;  //sum=sum+i;
i++;
}while(i<=e);
return sum;
}
}

#if else
pragma solidity ^0.5.0;
contract Pract4{
function test(int x) public view returns(string memory)
{
if(x%2==0)
return "Number is even";
else
return "Number is odd";
}
}
#string
pragma solidity ^0.5.0;
contract Pract4{
function test(int x) public view returns(string memory)
{
if(x%2==0)
return "Number is even";
else
return "Number is odd";
}
}

#array
contract Types {
uint[5] data;
 constructor() public
{
    data = [uint(10), 20, 30, 40, 50];
}
function array_example() public view returns (uint,uint)
{


return (data[0],data[4]);
}
function array_example2() public view returns (uint [5] memory)
{


return data;
}
}



#enum
pragma solidity ^0.5.0;
contract Types {
enum week_days
{
Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,
Sunday
}
week_days choice;
function set_value() public {
choice = week_days.Thursday;
}
function get_choice() public view returns (week_days) {
return choice;
}
}



# arithmetic operations
pragma solidity ^0.5.0;
// Creating a contract
contract SolidityTest {
// Initializing variables
uint16 public a = 20;
uint16 public b = 10;
// Initializing a variable
// with sum
uint public sum = a + b;
// Initializing a variable
// with the difference
uint public diff = a - b;
// Initializing a variable
// with product
uint public mul = a * b;
// Initializing a variable
// with quotient
uint public div = a / b;
// Initializing a variable
// with modulus
uint public mod = a % b;
// Initializing a variable
// decrement value
uint public dec = --b;
// Initializing a variable
// with increment value
uint public inc = ++a;
}

#structure
pragma solidity ^0.5.0;
contract test {
struct Book {
string title;
string author;
uint book_id;
}
Book book;


function setBook() public {
book = Book('Learn Java', 'TP', 1);
}
function getBookId() public view returns (uint) {
return book.book_id;
}
function getBookDetail() public view returns (string memory, string memory,uint) {
return (book.title, book.author, book.book_id);
}


}






