def words_sorting(*words):
    result = dict()

    for word in words:
        sum_of_letters = 0
        for el in word:
            sum_of_letters += ord(el)
        result[word] = result.get(word, 0) + sum_of_letters

    total_letters_sum = sum(result.values())
    final_result = []

    if total_letters_sum % 2 == 0:
        for w, s in sorted(result.items(), key=lambda x: x[0]):
            final_result.append(f"{w} - {s}")
    else:
        for w, s in sorted(result.items(), key=lambda x: -x[1]):
            final_result.append(f"{w} - {s}")

    return "\n".join(final_result)


print(
    words_sorting(
        'cacophony',
        'accolade'
  ))


