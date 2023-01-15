number_of_guests = int(input())

all_guests = []
guests_who_came = []

for guest in range(number_of_guests):
    current_guest = input()
    all_guests.append(current_guest)

while True:
    command = input()
    if command == "END":
        break
    guests_who_came.append(command)

final_guests = set(all_guests).difference(guests_who_came)

print(len(final_guests))
for guest in sorted(final_guests):
    print(guest)
