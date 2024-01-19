import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.
    '''
    def __init__(self):
        '''
            This function performs initialisation
            Initialising the attributes that print the first words.
            This is where all the parameters were also stated.
        '''
        print("Mystery word game has began")
        self.word_list = ["Apple", "Mango", "Blackberry", "Guava", "Orange"]
        self.num_of_lives = 5
        self.guessed_word = random.choice(self.word_list).lower()
        self.display = ['_' for _ in range(len(self.guessed_word))]
        self.game_over = False
        guess_word = self.guessed_word
        print("The guessed mystery word is {guess_word}")

    def ask_for_input(self):
        '''
            This function ask for the user's input.
            The way is works is that it asks the user for a letter and checks two things:
            1. If the letter has already been tried
            2. If the character is a single character
            If it passes both checks, it calls the check_letter method.
        '''
        guessed_letter = input("Guess a letter: ").lower()
        if len(guessed_letter) == 1 and guessed_letter.isalpha():
            print("Good guess!")
            self.check_guess(guessed_letter)
        else:
            print("Invalid letter guessed. Please, enter a single alphabet")7
        return guessed_letter

    def check_guess(self, guessed_letter):
        '''
            Checks if the letter is in the word.
            If it is, it replaces the '_' in the word_guessed list with the letter.
            If it is not, it reduces the number of lives by 1.
        '''
        for position in range(len(self.guessed_word)):
            if self.guessed_word[position] == guessed_letter:
                self.display[position] = guessed_letter
        print(''.join(self.display))

    def check_game_over(self, guessed_letter):
        '''
            This function check how many lives the user have left.
            If the user predict the wrong letter, the num_of_lives reduced by 1
            If the user guessed 5 words wrong, it's game over.
        '''
        if guessed_letter not in self.guessed_word:
            self.num_of_lives -= 1
            print(f"Lives remaining: {self.num_of_lives}")
            if self.num_of_lives == 0:
                self.game_over = True
                print("You Lose!!!")
        elif '_' not in self.display:
            self.game_over = True
            print("You Win!!!")

    def play_game(self):
        '''
            This function play the game by calling the ask_for_input function.
            It also calls the check_game_over functions to check the number of live and end the game.
        '''
        while not self.game_over:
            guessed_letter = self.ask_for_input()
            self.check_game_over(guessed_letter)

# Create an instance of the game and play it
game = Hangman()
game.play_game()
