from collections import deque

water_quantity = int(input())
names_deque = deque()

names = input()

while names != "Start":
    names_deque.append(names)
    names = input()

while True:
    command = input()
    if command.startswith("refill"):
        current_command = command.split()
        water_quantity += int(current_command[1])
    elif command == "End":
        print(f"{water_quantity} liters left")
        break
    else:
        litters = int(command)
        person = names_deque.popleft()
        if litters <= water_quantity:
            print(f"{person} got water" )
            water_quantity -= litters
        else:
            print(f"{person} must wait")
