from collections import deque

green_light_time = int(input())
free_window = int(input())

all_cars = deque()
passed_cars = 0

while True:
    command = input()

    if command == "END":
        break

    if command != "green":
        all_cars.append(command)
    else:
        current_green = green_light_time

        while current_green > 0 and all_cars:
            current_car = all_cars.popleft()
            total_time = current_green + free_window

            if len(current_car) > total_time:
                print("A crash happened!")
                print(f"{current_car} was hit at {current_car[total_time]}.")
                raise SystemExit

            current_green -= len(current_car)
            passed_cars += 1

print("Everyone is safe.")
print(f"{passed_cars} total cars passed the crossroads.")
