import os
current_folder = os.getcwd()
print(current_folder)

command = input()

while command != "End":
    action, file_name, *info = command.split("-")

    if action == "Create":
        file = open(f"{current_folder}/temp/{file_name}", "w")
        file.close()
    elif action == "Add":
        content = info[0]
        with open(f"{current_folder}/temp/{file_name}", "a") as file:
            file.write(f"{content}\n")
    elif action == "Replace":
        old_string, new_string = info
        try:
            with open(f"{current_folder}/temp/{file_name}", "r") as file:
                text = file.readlines()
            for line in range(len(text)):
                text[line] = text[line].replace(old_string, new_string)
            with open(f"{current_folder}/temp/{file_name}", "w") as file:
                file.write("".join(text))
        except FileNotFoundError:
            print("An error occurred")
    elif action == "Delete":
        try:
            os.remove(f"{current_folder}/temp/{file_name}")
        except FileNotFoundError:
            print("An error occurred")

    command = input()
