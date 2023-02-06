def check_indexes(row, coll):
    if 0 <= row < SIZE and 0 <= coll < SIZE:
        return True
    return False


SIZE = 6
trows = 3
total_points = 0
prize = None

matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(SIZE)]

for trow in range(trows):
    row, column = [int(x) for x in input()[1:-1].split(", ")]
    if check_indexes(row, column):
        if matrix[row][column] == "B":
            matrix[row][column] = 0
            for r in range(SIZE):
                total_points += matrix[r][column]

if total_points < 100:
    print(f"Sorry! You need {100 - total_points} points more to win a prize.")
else:
    if 100 <= total_points <=199:
        prize = "Football"
    elif total_points <= 299:
        prize = "Teddy Bear"
    elif total_points >= 300:
        prize = "Lego Construction Set"
    print(f"Good job! You scored {total_points} points, and you've won {prize}.")
