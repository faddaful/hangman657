# Import random to randomise the word list
import random

# Create a fruit word list and randomise it
word_list = ["Apple", "Mango", "Banana", "Pears", "Strawberry", "Guava", "Orange"]
word_list = random.choice(word_list)

# Function to check the guess word
def check_guess(guess):
    #Convert the guess word to lower case
    guess = guess.lower()

    # Check if the guess word is in the word list
    if guess in word_list:
        for letter in word_list:
            print(f"Good guess! , '{guess}' is in the word list")

    else:
        print(f"Sorry, '{guess} 'is not in the word. Try again.")

# Function to ask for the user's input of guessed word
def ask_for_input():
    while True:
        guess = input("Enter a single letter: ")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print ("Invalid letter. Please, enter a single alphabetical character.")

    print("Valid guess! ", guess)
    
    check_guess(guess)

# Calling the function
ask_for_input()
print("Guessed word:", word_list)