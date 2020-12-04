#Step 1
import random
from hangman_words import *
from hangman_art import *


guesses = []
# Randomly choose a word from the word_list
chosen_word = random.choice(word_list)
print(logo)
lives = 6
display = []
guesses = []
word_length = len(chosen_word)

for char in range(word_length):
    display += '_'


while '_' in display:
    # check to see if user repeated the letters
    guess = input("Guess: ").lower()
    guesses += guess
    if guess in display:
        print(f"already inputted {guess}")


    # check if letter in chosen word
    for i in range(word_length):
        if guess == chosen_word[i]:
            display[i] = chosen_word[i]


    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed: {guess}, thats not in the word")

        if lives == 0:
            print(f"You lose, the word was: {chosen_word}")
            quit()

    print(f"{' '.join(display)}\n")
    # print the ASCII art from 'stages' according to amount of lives
    print(stages[lives])

    if '_' not in display:
        print("You've Won!!")
