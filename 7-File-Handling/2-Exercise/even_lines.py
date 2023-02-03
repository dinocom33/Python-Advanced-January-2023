import os

current_folder = os.getcwd()
print(current_folder)

symbols = ["-", ",", ".", "!", "?"]
try:
    with open(f"{current_folder}/temp/text.txt", "r") as file:
        temp_file = file.readlines()

        for line in range(0, len(temp_file), 2):

            for symbol in symbols:
                temp_file[line] = temp_file[line].replace(symbol, "@")
            print(*temp_file[line].split()[::-1])
except FileNotFoundError:
    print("File not found ot wrong path!!!")
