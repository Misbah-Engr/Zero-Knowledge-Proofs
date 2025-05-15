# Exercise: Verify the claimed square roots in the finite field modulo 11.

# ┌─────────┬──────────────┬───────────────┐
# │ Element │ 1st Root     │ 2nd Root      │
# ├─────────┼──────────────┼───────────────┤
# │   0     │    0         │ n/a           │
# │   1     │    1         │ 10            │
# │   3     │    5         │ 6             │
# │   4     │    2         │ 9             │
# │   5     │    4         │ 7             │
# │   9     │    3         │ 8             │
# └─────────┴──────────────┴───────────────┘

# We'll check that each root squared modulo 11 equals the given element.

p = 11

pairs = [
    (0, 0, None),
    (1, 1, 10),
    (3, 5, 6),
    (4, 2, 9),
    (5, 4, 7),
    (9, 3, 8),
]

for element, r1, r2 in pairs:
    print(f"Element: {element}")
    if r1 is not None:
        print(f"  {r1}² % {p} = {pow(r1, 2, p)}")
        assert pow(r1, 2, p) == element
    if r2 is not None:
        print(f"  {r2}² % {p} = {pow(r2, 2, p)}")
        assert pow(r2, 2, p) == element
