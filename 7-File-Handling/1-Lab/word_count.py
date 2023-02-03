def word_count(words_file, text_file):

    with open(words_file, 'r') as f:
        words = [word.lower().split() for word in f]

    word_counts = {}
    with open(text_file, 'r') as f:
        for line in f:
            for word in line.strip().lower().split()[1:-1]:
                if word in words[0]:
                    if word not in word_counts:
                        word_counts[word] = 0
                    word_counts[word] += 1

    # Write results to file
    with open('output.txt', 'w') as f:
        for word, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True):
            f.write(f'{word} - {count}\n')


word_count('words.txt', 'input.txt')
