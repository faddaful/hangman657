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
        #for letter in word_list:
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
#print("Guessed word:", word_list)


class Hangman:
    def __init__(self, word_list, num_of_lives=5):

        self.word_list = word_list
        self.word = self.pick_random_word()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_of_lives = num_of_lives
        self.list_of_guesses = []
    
    def pick_random_word(self):

        return random.choice(self.word_list)
    
hangman_game = Hangman(['apple', 'banana', 'orange', 'strawberry', 'guava', 'mango'])

# Print initial attributes
print("Word:", hangman_game.word)
print("Word Guessed:", hangman_game.word_guessed)
print("Number of Letters:", hangman_game.num_letters)
print("Number of Lives:", hangman_game.num_of_lives)
print("List of Guesses:", hangman_game.list_of_guesses)