# Rareskills: Find the multiplicative inverse of 3 modulo 5. There are only 5 possibilities, so try all of them and see which ones work.

def find_inverse(a, n):
    for x in range(n):
        if (a * x) % n == 1:
            return x
    return None


a = 3
n = 5
inverse = find_inverse(a, n)

if inverse is not None:
    print(f"The multiplicative inverse of {a} modulo {n} is {inverse}.")
else:
    print(f"No inverse exists for {a} modulo {n}.")

# the range is {0,1,2,3,4}
