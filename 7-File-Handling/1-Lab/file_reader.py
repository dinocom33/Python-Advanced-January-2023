with open("numbers.txt", "r") as file:
    total_sum = 0
    for num in file:
        total_sum += int(num)

    print(total_sum)
