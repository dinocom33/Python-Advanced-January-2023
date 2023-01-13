from collections import deque

petrol_pump_numbers = int(input())
petrol_stations = deque()
index = 0
petrol_in_tank = 0

for _ in range(petrol_pump_numbers):
    pump_data = [int(x) for x in input().split()]
    petrol_stations.append(pump_data)

petrol_stations_copy = petrol_stations.copy()

while petrol_stations_copy:
    petrol, distance = petrol_stations_copy.popleft()
    petrol_in_tank += petrol

    if petrol_in_tank < distance:
        petrol_stations.append(petrol_stations.popleft())
        petrol_stations_copy = petrol_stations.copy()
        index += 1
        petrol_in_tank = 0
    else:
        petrol_in_tank -= distance
print(index)
