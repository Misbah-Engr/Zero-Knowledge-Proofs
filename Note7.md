I must write this note now because something interesting happened.

We were given the general rules of multiplicative inverse. Let me drop them.

> General rules of multiplicative inverses in finite field arithmetic:
> - 0 does not have a multiplicative inverse
> - 1 is its own multiplicative inverse
> - Every number (except 0) has exactly one multiplicative inverse (which could be itself)
> - the element of value (p-1) is its own multiplicative inverse. For example in a finite field of p = 103, 1 and 102 are their own multiplicative inverses. In a finite field of p = 23, 1 and 22 are their own multiplicative inverses (the reason why is explained in the upcoming section). Another example: in the finite field modulo 5, 1 is its own inverse, and 4 is its own inverse. 4 x 4 = 16, and 16 (mod 5) 1.

Unfortunately, I was careless about the fourth and final rule. I was carried away by Fermatt's little theorem.

And, in that too I forgot it only works in prime field.

Then, I got this exercise.

> Exercise: What is the multiplicative inverse of 50 in the finite field p = 51 ? You do not need Python to compute this, see the principles described in “General rules of multiplicative inverses.”

I went ahead and started solving the problem with Fermatt's, I got the inverse as 0 using,

```python

p (51) raised to the power of 50 - 2 (48)
51**(48) mod 51

```

I was confused and pressing my head, then it just dawned on me.

Is 51 a prime?
No.
So Fermatt's won't work.

I thought what could be the way out. I searched and searched and I found out we can suffer ourselves and use Euler's.

```solidity
works when gcd(a,n)=1

a raised to power psi * (n) − 1 ≡ a raised to power −1 mod n

Compute psi(51)

Since 51= 3 × 17, and they are distinct primes:
(3−1)(17−1) = 2*16 = 32

32 - 1 = 31
Compute (50 raised to power 31) mod 51

gives the inverse of 50 mod 51
```

It turns out it is 50 itself.
After wasting all these time without reading the last part of the exercise, or to be precise, without thinking a lot about it,

> You do not need Python to compute this, see the principles described in “General rules of multiplicative inverses.

Now, see the last general rule from above,

>  the element of value (p-1) is its own multiplicative inverse. For example in a finite field of p = 103, 1 and 102 are their own multiplicative inverses. In a finite field of p = 23, 1 and 22 are their own multiplicative inverses (the reason why is explained in the upcoming section). Another example: in the finite field modulo 5, 1 is its own inverse, and 4 is its own inverse. 4 x 4 = 16, and 16 (mod 5) 1.

So, since p is 51 and 50 is p-1 in this case, so, 50 must be its own Multiplicative inverse.


Let me get back to study, we will meet in Note 8.
