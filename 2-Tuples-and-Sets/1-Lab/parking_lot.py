number_of_cars = int(input())

parking_lot = []

for _ in range(number_of_cars):
    direction, car_plate = input().split(", ")
    if direction == "IN":
        parking_lot.append(car_plate)
    elif direction == "OUT":
        parking_lot.remove(car_plate)

if parking_lot:
    print("\n".join(set(parking_lot)))
else:
    print("Parking Lot is Empty")
