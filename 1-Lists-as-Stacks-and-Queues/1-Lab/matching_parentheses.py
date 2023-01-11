text = input()

stack = []

for i in range(len(text)):
    if text[i] == "(":
        stack.append(i)
    elif text[i] ==")":
        start_index = stack.pop()
        print(text[start_index:i + 1])
