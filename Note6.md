Hey guys,

I will not detail my today's learning in this note. It will be in Note7.

When I was learning Finite fields, I learned an interesting theory, Fermatt's Little Theorem and its application in finding the multiplicative inverse of an element of a prie field, so, I tried implementing its function in a solidity contract.

## Note
This is not a secure audited code, it is only done for illustration purpose and the math is correct but it might have issues if it were to be used onchain.

```solidity
// I want to create a function that returns the multiplicative inverse of an element in a prime field.

// Just like Python's pow(a, -1, p) will do

pragma solidity >0.8.19;

contract FinitePlayGround {

function findMul_Inv(uint256 element, uint256 field) public pure returns(uint256) {

    require(element > 0 && element < field && isPrime(field) == true);
    uint256 subRes = field -2;
    uint256 Mul_Inv = (element**(subRes)) % field;

return Mul_Inv;
}

function isPrime(uint256 p) internal pure returns (bool) {
        if (p < 2) return false;
        for (uint256 i = 2; i * i <= p; i++) {
            if (p % i == 0) return false;
        }
        return true;
    }

}


```