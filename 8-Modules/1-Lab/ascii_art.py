import pyfiglet

def ascii_art(text):
    result = pyfiglet.figlet_format(text)

    return result

text = input()
print(ascii_art(text))
# print(pyfiglet.print_figlet(text))