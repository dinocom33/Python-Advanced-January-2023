from fib_module import *

command = input()

while command != "Stop":
    if command.startswith("Create"):
        print(create_sequence(int(command.split()[2])))
    elif command.startswith("Locate"):
        print(locate_number(int(command.split()[1])))
    command = input()
print()
