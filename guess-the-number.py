import os
import random

guessed = False
lives = 0
choice = random.randint(0, 101)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'hard':
    lives = 5
else:
    lives = 10


while not guessed and lives > 0:
    print(f"You've got {lives} attemps remaining.")
    guess = int(input("Make a guess: "))
    if guess != choice:
        lives -= 1
        if lives == 0:
            print("You ran out of lives :(")
        if guess > choice:
            print("Too high")
        elif guess < choice:
            print("Too low")
        print("Guess again.")

    else:
        print(f"You've got it! the answer is: {choice}")
        guessed = True
