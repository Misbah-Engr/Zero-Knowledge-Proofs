## The lesson:
https://www.rareskills.io/post/arithmetic-circuit

## The Practice Problems:

1. Create an arithmetic circuit that takes signals x₁, x₂, …, xₙ and is satisfied if at least one signal is 0.

2. Create an arithmetic circuit that takes signals x₁, x₂, …, xₙ and is satsified if all signals are 1.

3. A bipartite graph is a graph that can be colored with two colors such that no two neighboring nodes share the same color. Devise an arithmetic circuit scheme to show you have a valid witness of a 2-coloring of a graph. Hint: the scheme in this tutorial needs to be adjusted before it will work with a 2-coloring.

4. Create an arithmetic circuit that constrains k to be the maximum of x, y, or z. That is, k should be equal to x if x is the maximum value, and same for y and z.

5. Create an arithmetic circuit that takes signals x₁, x₂, …, xₙ, constrains them to be binary, and outputs 1 if at least one of the signals is 1. Hint: this is tricker than it looks. Consider combining what you learned in the first two problems and using the NOT gate.

6. Create an arithmetic circuit to determine if a signal v is a power of two (1, 2, 4, 8, etc). Hint: create an arithmetic circuit that constrains another set of signals to encode the binary representation of v, then place additional restrictions on those signals.

7. Create an arithmetic circuit that models the Subset sum problem. Given a set of integers (assume they are all non-negative), determine if there is a subset that sums to a given value. For example, given the set {3,5,17,21} and k = 22, there is a subset {5, 17} that sums to 22. Of course, a subset sum problem does not necessarily have a solution.
Hint: Use a “switch” that is 0 or 1 if a number is part of the subset or not.
8. The covering set problem starts with a set `S = {1, 2, …, 10}` and several well-defined subsets of S, for example: {1, 2, 3}, {3, 5, 7, 9}, {8, 10}, {5, 6, 7, 8}, {2, 4, 6, 8} and asks if we can take at most k subsets of S such that their union is S.
In the example problem above, the answer for k = 4 is true because we can use {1, 2, 3}, {3, 5, 7, 9}, {8, 10}, {2, 4, 6, 8}. Note that for each problems, the subsets we can work with are determined at the beginning. We cannot construct the subsets ourselves. If we had been given the subsets {1, 2, 3}, {4, 5}, {7, 8, 9, 10} then there would be no solution because the number 6 is not in the subsets.

On the other hand, if we had been given S = {1, 2, 3, 4, 5} and the subsets
{1}, {1, 2}, {3,4}, {1, 4, 5} and asked can it be covered with k = 2 subsets, then there would be no solution. However, if k 3 then a valid solution would be {1, 2}, {3,4}, {1,4,5}.
Our goal is to prove for a given set S and a defined list of subsets of S, if we can pick a set of subsets such that their union is S. Specifically, the question is if we can do it with k or fewer subsets. We wish to prove we know which k (or fewer) subsets to use by encoding the problem as an arithmetic circuit.

## The Solution:
### 1: logically what this question is asking me is an arithmetic circuit that is satisfied if:

```
(x₁ == 0) OR (x₂ == 0) OR ... OR (xₙ == 0)
```

Let me do some trick and see,

```
prod = x₁ * x₂ * ... * xₙ
```
If at least one xᵢ = 0, then prod == 0.
But if all xᵢ ≠ 0, then prod ≠ 0.

... If the product is not 0, it means all inputs are non-zero, so we can flip that:

The circuit:

```
(x₁ * x₂ * ... * xₙ) === 0

```

### 2: we want 
```
(x₁ == 1) AND (x₂ == 1) AND ... AND (xₙ == 1)
```

each condition is,
```
xᵢ - 1 == 0

```

then, using sum of squares

```
∑ (xᵢ - 1)² == 0

```
because If any xᵢ ≠ 1, then (xᵢ - 1)² > 0, so the sum > 0 → circuit not satisfied and all xᵢ == 1, then each (xᵢ - 1)² = 0.

### 3: 
Step 1: each color will be either 0 or 1

for every vertex i,

```
color_i * (color_i - 1) == 0
```

we need different color on each edge:

```
c_i ≠ c_j   for every edge (i, j)
```

aha, let us translate it

```
(c_i - c_j)² == 1
```
The Circuit:

```

// For each vertex i ∈ V

c_i * (c_i - 1) == 0

// For each edge  (i,j) ∈ E:

(c_i - c_j)² == 1

```

### 4:

So, we are here looking fo k = max(x, y, z)

Let us plan,

s₁ = 1 if x is the max, 0 otherwise

s₂ = 1 if y is the max, 0 otherwise

s₃ = 1 if z is the max, 0 otherwise

then, 
```
k = s₁ * x + s₂ * y + s₃ * z
```

```
// Boolean constraints
s₁ * (s₁ - 1) == 0  
s₂ * (s₂ - 1) == 0  
s₃ * (s₃ - 1) == 0

// selector
s₁ + s₂ + s₃ == 1

// Maximum selection logic
k == s₁ * x + s₂ * y + s₃ * z

// Enforce correct selection
s₁ * (y - x) == 0  
s₁ * (z - x) == 0

s₂ * (x - y) == 0  
s₂ * (z - y) == 0

s₃ * (x - z) == 0  
s₃ * (y - z) == 0


```

### 5
Force each input to be 0 or 1:

```
x_i * (x_i - 1) == 0   for all i
```

At least one is 1

```
¬x_i = 1 - x_i
```

Now,

```
If all x_i = 0  ⇒ all (1 - x_i) = 1  ⇒ product = 1
If any x_i = 1  ⇒ some (1 - x_i) = 0 ⇒ product = 0
```

### Circuits

Input constraints:

```
For all i:
    x_i * (x_i - 1) == 0
```

NOT:

```
not_x_i = 1 - x_i
```

Product of all not_x_i:

```
p = not_x_1 * not_x_2 * ... * not_x_n
```

Final:

```
out = 1 - p

out = (1 - (not_x_1 * not_x_2 * ... * not_x_n))
```


### 6

Let b₀, b₁, ..., bₙ₋₁ ∈ {0,1} represent the bits of v:

```
bᵢ * (bᵢ - 1) == 0   for all i  (force binary)

```
Lets reconstruct:

```
v == ∑ (bᵢ * 2ⁱ)  for i = 0 to n-1
```

enforce only one bit,

```
∑ bᵢ == 1
```

```
If bits = [b₀, b₁, ..., bₙ₋₁]

For all i:      bᵢ * (bᵢ - 1) == 0
Sum(bits) == 1
v == ∑ (bᵢ * 2ⁱ)

```
### 7

```
// For each i=1…n:
    s_i * (s_i - 1) == 0          // s_i ∈ {0,1}

// And the core sum constraint:
    (s₁·a₁ + s₂·a₂ + … + sₙ·aₙ) == k

```

## 8
Let me write a contract for this:

```
contract CoveringVerifier {
    // Verify that there exists ≤k subsets whose union is {1..N}
    // m    number of candidate subsets
    // N    size of the ground set S={1..N}
    // b    m×N matrix (flattened as uint[][]), b[i][j]∈{0,1} indicates if subset i contains element j+1
    // k    maximum number of subsets allowed
    // s    selector bits (length m), s[i]∈{0,1} chooses subset i
    // d    bits of the binary decomposition of (k - sum s[i]) to enforce sum s[i] ≤ k
    function verify(
        uint m,
        uint N,
        uint[][] memory b,
        uint k,
        uint[] memory s,
        uint[] memory d
    ) public pure returns (bool) {
        if (b.length != m) return false;
        if (s.length != m) return false;

        // Enforce s[i] ∈ {0,1} and compute T = ∑ s[i]
        uint T = 0;
        for (uint i = 0; i < m; i++) {
            if (s[i] > 1) return false;        // s_i*(s_i-1)==0
            T += s[i];
        }

        // Enforce T ≤ k via binary decomposition of (k-T)
        if (k < T) return false;
        uint diff = k - T;
        uint sumD = 0;
        for (uint ℓ = 0; ℓ < d.length; ℓ++) {
            uint bit = d[ℓ];
            if (bit > 1) return false;         // d_ℓ*(d_ℓ-1)==0
            sumD += bit << ℓ;                  // reconstruct diff = ∑ 2^ℓ * d_ℓ
        }
        if (sumD != diff) return false;

        // Coverage constraints
        for (uint j = 0; j < N; j++) {
            // quick length check per row
            // (skip if you know b[i].length==N off‐chain)
            // if any row is shorter, revert
            for (uint i = 0; i < m; i++) {
                if (b[i].length != N) return false;
            }

            uint p = 1;
            for (uint i = 0; i < m; i++) {
                // b[i][j] must be 0 or 1
                if (b[i][j] > 1) return false;
                // term = 1 - s[i]*b[i][j]
                uint term = 1 - (s[i] * b[i][j]);
                p = p * term;
            }
            if (p != 0) {
                // p==1 means element j+1 is not covered by any chosen subset
                return false;
            }
        }

        // All constraints passed
        return true;
    }
}

```

## See you in finite fields: https://www.rareskills.io/post/finite-fields
