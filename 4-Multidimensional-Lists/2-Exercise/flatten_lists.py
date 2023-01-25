numbers = input().split("|")

matrix = []

for nums in reversed(numbers):
    matrix.extend(nums.split())

print(*matrix)
