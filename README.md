# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Game Objective
A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

### Game Outline
The game starts by asking the user to guess a random letter to form a random word.
But before then, the funcion check_guess() check if the guess word is the is one letter, an alphabet and it is in the list.
The function ask_for_input() will then ask the user for his/her input.
the user's input is check to match the randomly selected word letter by letter.

If the letter is correct, the game moves on otherwise, the user lose 1 live when guessed a wrong word.

After the user guessed 5 words wrong, they lose 5 lives and the game is over.

## Learnings
The learning from this project is to create a mini game and showcase how to use logic, psuedocode and outline to create a game using python.


