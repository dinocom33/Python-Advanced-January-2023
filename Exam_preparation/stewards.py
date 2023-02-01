from collections import deque

seats = input().split(", ")
first_numbers = deque(int(x) for x in input().split(", "))
second_numbers = deque(int(x) for x in input().split(", "))

seat_matches = []
rotations_count = 0

while len(seat_matches) != 3 and rotations_count != 10:
    left_number = first_numbers.popleft()
    right_number = second_numbers.pop()
    letter = chr(left_number + right_number)
    current_seat_1 = str(left_number) + letter
    current_seat_2 = str(right_number) + letter

    if  current_seat_1 in seats:
        seat_matches.append(current_seat_1)
        seats.remove(current_seat_1)
    elif  current_seat_2 in seats:
        seat_matches.append(current_seat_2)
        seats.remove(current_seat_2)
    else:
        first_numbers.append(left_number)
        second_numbers.appendleft(right_number)
    rotations_count += 1


print(f"Seat matches: {', '.join(seat_matches)}")
print(f"Rotations count: {rotations_count}")
