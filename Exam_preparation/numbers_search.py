def numbers_searching(*numbers):
    smallest_num = min(numbers)
    biggest_num = max(numbers)
    missing_numbers = []
    duplicate_numbers = []

    for number in range(smallest_num, biggest_num + 1):
        if number not in numbers:
            missing_numbers.append(number)

    for num in numbers:
        if numbers.count(num) > 1 and num not in duplicate_numbers:
            duplicate_numbers.append(num)

    result = []
    for num in missing_numbers:
        result.append(num)
        result.append(sorted(duplicate_numbers))
    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
