import random
# create a word list
word_list = ["Apple", "Mango", "Blackberry", "Guava", "Orange"]
# create game lives
num_of_lives = 5
# guess a word and randomise it
guessed_word = random.choice(word_list)
# display empty list of guesses
display = []
#print(guessed_word)
# check the range of guess word and put dash placeholder
for element in range(len(guessed_word)):
    display += '_'
#print(display)
# create a game over variable
game_over = False
# create a input and loop over the number of guessed word 
while not game_over:
    guessed_letter = input("Guess a letter: ").lower()
    if len(guessed_letter) == 1 and guessed_letter.isalpha():
        print("Good guess!")
    else:
        print("Invalid letter guessed. Please, enter a single alphabet")
# Check the guess letter is in the guessed word and validate each position      
    for position in range(len(guessed_word)):
        letter = guessed_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
    print(display)
# link the wrong letter guessed to reduce the number of lives.
# Print Game over.
    if guessed_letter not in guessed_word:
        num_of_lives -= 1
        if num_of_lives == 0:
            game_over = True
            print("You Lose!!!")
        
    if '_' not in display:
        game_over = True
        print("You Win!!!")
