import random

class Hangman:
    def __init__(self, word_list, num_of_lives=5):

        self.word_list = word_list
        self.word = self.pick_random_word()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_of_lives = num_of_lives
        self.list_of_guesses = []
