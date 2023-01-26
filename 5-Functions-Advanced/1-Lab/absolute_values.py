numbers = list(map(float, input().split()))

result = list(map(lambda x: abs(x), numbers))

print(result)