numbers = tuple(map(float, input().split()))

final_numbers = {}

for num in numbers:
    if num not in final_numbers:
        final_numbers[num] = final_numbers.get(num, 0)
    final_numbers[num] += 1

for key, value in final_numbers.items():
    print(f"{key} - {value} times")
