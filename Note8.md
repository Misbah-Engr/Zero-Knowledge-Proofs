I read some Groth16 Audit Reports including Mysten Fastcrypto.
 report of October 2023. They all cited this paper. These ugly tables are the first frightening things I saw when I started reading the most cited ZK paper: On the Size of Pairing Based Non Interactive Arguments.
I will break down what it is for you. 🧵

## Table 1

```ASCII
+------------------+--------------------+-----------------+-------------------+-------------+-----+
|                  | CRS size           | Proof size      | Prover comp.      | Verifier comp. | PPE |
+------------------+--------------------+-----------------+-------------------+-------------+-----+
| [DFGK14]         | 2m+n-2l G1, m+n-l G2 | 3 G1, 1 G2     | m+n-l E1, 6 P     | l M1, 3 P   | 3   |
| This work        | 3m+n G1, m G2      | 2 G1, 1 G2     | n E1              | m, 3 P      | 1   |
+------------------+--------------------+-----------------+-------------------+-------------+-----+
```

Caption: Comparison for boolean circuit satisfiability with l-bit statement, m wires and n fan-in 2 logic gates. 
Notation: G means group elements, M means multiplications, E means exponentiations and P means pairings with subscripts indicating the relevant group. 
It is possible to get a CRS size of m+2n elements in G1 and n elements in G2, but we have chosen to include some precomputed values in the CRS to reduce the prover’s computation, see Sect. 3.2.

## Table 2:

```
+------------------+--------------------+-----------------+-------------------+-------------+-----+
|                  | CRS size           | Proof size      | Prover comp.      | Verifier comp. | PPE |
+------------------+--------------------+-----------------+-------------------+-------------+-----+
| [PHGR13]         | 7m+n-2l G          | 8 G             | 7m+n-2l E         | l E, 11 P   | 5   |
| This work        | m+2n G             | 3 G             | m+3n-l E          | l E, 3 P    | 1   |
| [BCTV14a]        | 6m+n+l G1, m G2    | 7 G1, 1 G2     | 6m+n-l E1, m E2   | l E1, 12 P  | 5   |
| This work        | m+2n G1, n G2      | 2 G1, 1 G2     | m+3n-l E1, n E2   | l E1, 3 P   | 1   |
+------------------+--------------------+-----------------+-------------------+-------------+-----+
```

Caption: Comparison for arithmetic circuit satisfiability with l-element statement, m wires, n multiplication gates. 
Notation: G means group elements, E means exponentiations and P means pairings. 
We compare symmetric pairings in the first two rows and asymmetric pairings in the last two rows.

The tables compare different ZK-SNARK Schemes with the scheme of this paper
1. DFGK14 (Square Span Programs with Applications to Non Interactive ZK Arguments)
2. PHGR13 (Pinocchio: Nearly Practical Verifiable Computation)
3. BCTV14a (Scalable Zero Knowledge via Cycles of Elliptic Curves)

Table 1 is specifically for Boolean Circuit Satisfiably and of course Table 2 does the opposite, Compares schemes for arithmetic Circuit Satisfiability.

For table 1. m is the number of wires in the circuit. n is number of fan in 2 logic gates. l is the size of the statement (measured in bits).

For table 2. m is of course the number of wires. n is the number of multiplication gates. And l the size of public inputs/outputs of the statement.

CRS size is the common reference string size. Before anyone can create or check proofs, there is a one-time setup that generate some public parameters. This is the CRS. It is the rules that prover and verifier agree to use.
- the size of CRS tells you you much data this setup occupies.
- G: The rep. Elements from elliptic curve group.
- m, n, l: these relate to the size and complexity of the problem you are proving as defined for each table.

A small CRS is better because it means less data to generate, store and distribute initially. E.g 3m + 2l G2 means the CRS contains 3m + 2l elements from G1.

Proof size: This is how much data the prover needs to send to the verifier.
It is an important metric for SNARKS. Succint meas the proof should be very small regardless of how much complex the original problem was. This is to make proofs cheap to transmit and store.
E.g 2G1 and 1G2 means the proof consists of 2 elements from G1 and 1 element from G2. This is very small.

Prover computation:
This measures how much work the prover has to do to generate proof.
E- Exponentiations. Exponentiation is expensive. Even with less powerful hardware a prover can create proof if E is very small. As exponentiation needed to create the proof get higher the computation gets higher.

m + 3n - l E1 means the prover needs to roughly do m + 3n - l exponentiations in group G1.

Verifier computation.
Similar to prover computation but for verifier. P stands for pairings, they are computationally intensive operations linking elements from G1 to G2 to an element of target group called G_T.
M1 - number of multiplications in G1
l is as noted before the size of the statement in bits for Boolean or number of elements in arithmetic Circuit statement.

Therefore, lm1, P means the verifier does l multiplications and 3 pairing operations.

Finally, PPE stands for "Pairing Product Equations." It counts how many complex equations involving pairings the verifier needs to check.
Pairings are the most expensive part of verification for these schemes. Fewer PPEs usually mean faster verification. 
In table 1 (for Boolean circuits), DFGK14 verifier needs 3 PPE, while in this paper verifier needs only 1 PPE.
