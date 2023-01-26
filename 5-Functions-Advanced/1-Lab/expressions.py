from itertools import permutations, chain

numbers = list(input().split(", "))
n = len(numbers)

permutations = set(permutations(["-"] * n + ["+"] * n, n))

for permutation in permutations:
    expr = "".join(chain(*zip(permutation, numbers)))
    result = eval(expr)
    print(f"{expr}={result}")
