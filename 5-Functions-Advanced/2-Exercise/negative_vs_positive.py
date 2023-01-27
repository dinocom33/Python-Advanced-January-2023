def negatives(numbers):
    negative_sum = sum([num for num in numbers if num < 0])
    return negative_sum


def positives(numbers):
    positive_sum = sum([num for num in numbers if num > 0])
    return positive_sum


numbers = list(map(int, input().split()))


print(negatives(numbers))
print(positives(numbers))

if abs(negatives(numbers)) > positives(numbers):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
