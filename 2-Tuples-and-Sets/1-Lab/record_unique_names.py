number_of_names = int(input())

all_names = []

for _ in range(number_of_names):
    name = input()
    all_names.append(name)

print("\n".join(set(all_names)))
