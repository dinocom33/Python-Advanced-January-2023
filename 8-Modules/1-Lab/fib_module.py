sequence = []


def create_sequence(number):
    sequence.clear()
    if number < 0:
        return "Incorrect input"
    else:
        sequence.append(0)
        sequence.append(1)
        for i in range(number - 2):
            sequence.append(sequence[-1] + sequence[-2])

    return " ".join(map(str, sequence))


def locate_number(number):
    if number in sequence:
        return f"The number - {number} is at index {sequence.index(number)}"
    else:
        return f"The number {number} is not in the sequence"