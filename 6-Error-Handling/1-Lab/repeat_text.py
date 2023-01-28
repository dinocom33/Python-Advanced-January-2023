text = input()


try:
    number = int(input())
    print(text * number)
except:
    print("Variable times must be an integer")
