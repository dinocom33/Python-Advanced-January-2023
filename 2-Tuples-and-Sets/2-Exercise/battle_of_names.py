odd_set = set()
even_set = set()

for row in range(1, int(input()) + 1):
    name = input()
    result = sum(ord(l) for l in name) // row

    if result % 2 != 0:
        odd_set.add(result)
    else:
        even_set.add(result)

if sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=", ")
else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")
