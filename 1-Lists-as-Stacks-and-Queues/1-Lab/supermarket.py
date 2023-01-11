from _collections import deque

names_deque = deque()

while True:
    command = input()
    if command == "End":
        print(f"{len(names_deque)} people remaining.")
        break
    elif command == "Paid":
        while len(names_deque) > 0:
            customer = names_deque.popleft()
            print(customer)
    else:
        names_deque.append(command)
