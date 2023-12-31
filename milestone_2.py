import random

word_list = ['Mango', 'Guava', 'Orange', 'Pears', 'Banana']

word = random.choice(word_list)
#print(word)

guess = input("Enter a single letter:")

if len(guess) == 1 and not (guess.isnumeric()):
    print("Good guess!")
else:
    print(f"Oops! {guess} is not a valid input.")
pass

print(guess)