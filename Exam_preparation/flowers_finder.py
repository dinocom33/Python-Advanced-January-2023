from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())

words = {
"rose": [x for x in "rose"],
"tulip": [x for x in "tulip"],
"lotus": [x for x in "lotus"],
"daffodil": [x for x in "daffodil"]
}
found_word = None

while vowels and consonants and not found_word:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for letter in (vowel, consonant):
        for key, word in words.items():
            while word.count(letter):
                word.remove(letter)
                if not word:
                    found_word = key

if found_word:
    print(f"Word found: {found_word}")
else:
    print(f"Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
