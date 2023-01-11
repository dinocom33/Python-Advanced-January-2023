text = list(input())

reverse_stack = []

for i in range(len(text)):
    reverse_stack.append(text.pop())

print("".join(reverse_stack))
