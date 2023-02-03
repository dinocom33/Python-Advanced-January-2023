from string import punctuation

with open("text.txt", "r") as file:
    text = file.readlines()
    output = open("output.txt", "w")

    for line in range(len(text)):
        letters = 0
        punctuations = 0

        for symbol in text[line]:
            if symbol.isalpha():
                letters += 1
            elif symbol in punctuation:
                punctuations += 1

        output.writelines(f"Line {line + 1}: {''.join(text[line][:-1])} ({letters})({punctuations})\n")

output.close()
