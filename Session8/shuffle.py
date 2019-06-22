import random
word = input('Enter a word: ')
character = list(word)
random.shuffle(character)
for i in character:
    print("Jumbled word:", i)
