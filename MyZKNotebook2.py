a = 288
p = 311

# Compute the modular inverse
inverse = pow(a, -1, p)

# Validate
assert (a * inverse) % p == 1

print(f"The multiplicative inverse of {a} modulo {p} is {inverse}.")
