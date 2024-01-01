# Import random to randomise the word list
import random

# Create a fruit word list and randomise it
word_list = ["Apple", "Mango", "Banana", "Pears", "Strawberry", "Guava", "Orange"]
word_list = random.choice(word_list)

class Hangman:
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
            if len(guess) == 1 and guess.isalpha(): #and guess not in self.list_of_guesses:
                #self.list_of_guesses.append(guess)
                break
            else:
                print ("Invalid letter. Please, enter a single alphabetical character.")

        print("Valid guess! ", guess)
        #self.check_guess(guess)

    # Calling the function
    ask_for_input()
    #print("Guessed word:", word_list)

    def __init__(self, word_list, num_of_lives=5):

        self.word_list = word_list
        self.word = self.pick_random_word()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_of_lives = num_of_lives
        self.list_of_guesses = []
    
    def pick_random_word(self):

        return random.choice(self.word_list)
    
    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")

            # Loop through each letter in the word
            for i, letter in enumerate(self.word):
                # Check if the letter is equal to the guess
                if letter == guess:
                    # Replace the corresponding "_" in word_guessed with the guess
                    self.word_guessed[i] = guess

            # Reduce num_letters by 1
            self.num_letters -= 1
        else:
            self.num_of_lives -= 1

            print(f"Sorry, '{guess}' is not in the word. Try again.")
            print(f"You have {self.num_of_lives} lives left.")

    def play_game(self):
        num_lives = 5
        game = Hangman(word_list, num_lives)

        while True:
            if game.num_lives == 0:
                print("You lost!")
                break
            elif game.num_letters > 0:
                game.ask_for_input()
            else:
                print("Congratulations. You won the game!")
                break
    
hangman_game = Hangman(word_list)


print("Word:", hangman_game.word)
print("Word Guessed:", hangman_game.word_guessed)
print("Number of Letters:", hangman_game.num_letters)
print("Number of Lives:", hangman_game.num_of_lives)
print("List of Guesses:", hangman_game.list_of_guesses)
