class ValueCannotBeNegative(Exception):
    pass

for num in range(5):
    try:
        number = int(input())
        if number < 0:
            raise ValueCannotBeNegative
    except:
        print("Value cannot be negative")


