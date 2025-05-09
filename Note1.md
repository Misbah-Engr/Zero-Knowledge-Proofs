## Introducing myself to ZK and zk proofs

I became interested in ZK after learning it needs heavy math. I am an Electrical Engineering student. So, we do a lot of math in Uni. ZK crypto projects could have subtle flaw in underconstraining or overconstraining inputs which will lead to critical vulnerabilities I will be interested in as a security researcher.


## Checking what ZK findings look like:
I filtered Solodit findings and read some OpenZeppelin findings in ZKSync audits.

https://solodit.cyfrin.io/?b=false&f=&fc=gte&ff=&fn=1&i=HIGH&p=1&pc=&pn=zksync&r=all&s=&t=

In the following report they asked the team to check a paper:
https://solodit.cyfrin.io/issues/missing-subgroup-check-for-g2-points-openzeppelin-none-zksync-crypto-precompile-audit-markdown

This is the paper: Co-factor clearing and subgroup membership testing on pairing-friendly curves: https://eprint.iacr.org/2022/352.pdf

I started reading and later uploaded it to Google AI studio and asked my silly questions to understand what it wanted to show:
The tldr: 
> The paper deals with pairing-friendly curves (often BLS curves).
These curves have cofactors that need to be "cleared" to ensure points are in the correct prime-order subgroup (G1 or G2). The paper shows faster ways to clear these cofactors.
Membership in G1 or G2 can be tested efficiently using endomorphisms (like the Frobenius or related ones) by checking if a point is an eigenpoint for a specific eigenvalue. The paper provides a more rigorous and generalized framework for these tests, ensuring they are correct even when cofactors are present.

This sparked my interest into deeply learning this subject. I moved ahead to take this course and it refreshed me.

https://www.udemy.com/course/web3-academy-masterclass-zero-knowledge-proofs-essentials/

Yesterday I started the RareSkills ZK Book and I finished the 1st chapter and I finished half of the second (Arithmetic Circuits).
https://www.rareskills.io/zk-book

## Conclusion

I will be opening new note md files in this repo and share my learning journey to mastery
