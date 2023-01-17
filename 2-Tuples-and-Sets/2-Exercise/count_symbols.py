all_characters = dict()

for ch in input():
    all_characters[ch] = all_characters.get(ch, 0) + 1

for key, value in sorted(all_characters.items()):
    print(f"{key}: {value} time/s")
