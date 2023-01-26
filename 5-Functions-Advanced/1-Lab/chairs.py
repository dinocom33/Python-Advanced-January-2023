from itertools import combinations

names = input().split(", ")
number_of_chairs = int(input())

for combination in combinations(names, number_of_chairs):
    print(", ".join(combination))
