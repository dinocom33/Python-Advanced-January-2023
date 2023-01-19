firs_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())

functions = {
    "Add First": lambda x: [firs_sequence.add(int(y)) for y in x],
    "Add Second": lambda x: [second_sequence.add(int(y)) for y in x],
    "Remove First": lambda x: [firs_sequence.discard(int(y)) for y in x],
    "Remove Second": lambda x: [second_sequence.discard(int(y)) for y in x],
    "Check Subset": lambda: print(True) if firs_sequence.issubset(second_sequence) or
                                           second_sequence.issubset(firs_sequence) else print(False),
}

for _ in range(int(input())):
    current_command, *info = [x for x in input().split()]
    command = current_command + " " + info.pop(0)
    if info:
        functions[command](info)
    else:
        functions[command]()

print(*sorted(firs_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")
