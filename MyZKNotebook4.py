# Exercise: use the galois library to check that 3/4\*1/2 = 3/8 in the finite field p = 17.
import galois

# Define the field
GF = galois.GF(17)

# Define elements in the field
a = GF(3) / GF(4)
b = GF(1) / GF(2)
left = a * b

right = GF(3) / GF(8)

# Check equality
print("Left side:", left)
print("Right side:", right)
print("Equal?", left == right)

# Left side: 11
# Right side: 11
# Equal? True
