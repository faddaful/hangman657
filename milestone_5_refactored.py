import random

class Hangman:
    def __init__(self):
        self.word_list = ["Apple", "Mango", "Blackberry", "Guava", "Orange"]
        self.num_of_lives = 5
        self.guessed_word = random.choice(self.word_list).lower()
        self.display = ['_' for _ in range(len(self.guessed_word))]
        self.game_over = False

    def ask_for_input(self):
        guessed_letter = input("Guess a letter: ").lower()
        if len(guessed_letter) == 1 and guessed_letter.isalpha():
            print("Good guess!")
            self.check_guess(guessed_letter)
        else:
            print("Invalid letter guessed. Please, enter a single alphabet")
        return guessed_letter

    def check_guess(self, guessed_letter):
        for position in range(len(self.guessed_word)):
            if self.guessed_word[position] == guessed_letter:
                self.display[position] = guessed_letter
        print(''.join(self.display))

    def check_game_over(self, guessed_letter):
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
        while not self.game_over:
            guessed_letter = self.ask_for_input()
            self.check_game_over(guessed_letter)

# Create an instance of the game and play it
game = Hangman()
game.play_game()
