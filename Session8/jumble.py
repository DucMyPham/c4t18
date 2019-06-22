import random
words = ('cake', 'cookie', 'candy', 'pie')
word = random.choice(words)
correct = word
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position +1):]
print("The jumble is: ", jumble)
guess = input("Ur guess is: ")
if guess == correct:
    print("Correct")
else:
    print("Sorry u guess it wrong")
