import galois
GF7 = galois.GF(7) # GF7 is a class that wraps 7

one_half = GF7(1) / GF7(2)
one_third = GF7(1) / GF7(3)
five_over_six = GF7(5) / GF7(6)

sum = one_half + one_third 

assert sum == five_over_six

print(sum)
