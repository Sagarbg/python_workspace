# Randomly choose the word

import random

# import hangman_words
from hangman_words import word_list

# import hangman_art as stages
from hangman_art import stages, logo

# word_list = ["aardvark", "baboon", "camel"]

lives = 6

# Printing the hangman logo
print(logo)

# Generate random word from the word list
chosen_word = random.choice(word_list)

print("Selected word is: ", chosen_word)

# Generate as many blanks as the letters in the word
placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

# Ask the user to guess a letter until the game over

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)


    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"*************IT WAS {chosen_word}! YOU LOSE*************")

    if "_" not in display:
        game_over = True
        print("*************YOU WIN*************")

    
    print(stages[lives])