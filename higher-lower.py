# Higher Lower Game
from higher_lower_data import data
from higher_lower_art import *
import random
import os

def game():
    game_over = False
    score = 0
    a = random.randint(0, len(data) - 1)
    b = random.randint(0, len(data) - 1)

    while not game_over:

        followers_a = data[a]['follower_count']
        followers_b = data[b]['follower_count']
        name_a = data[a]['name']
        name_b = data[b]['name']
        desc_a = data[a]['description']
        desc_b = data[b]['description']
        country_a = data[a]['country']
        country_b = data[b]['country']

        if a == b:
            b = random.randint(0, len(data) - 1)



        print(logo)
        print("Compare A: " + name_a, 'a', desc_a, 'from', country_a)
        print(vs)
        print("Compare B: " + name_b, 'a', desc_b, 'from', country_b)

        choice = input('Who has more followers: A or B: ')
        os.system("clear")

        if choice.lower() == 'a' and followers_a > followers_b or choice.lower() == 'b' and followers_b > followers_a:
            score += 1
            a = b
            b = random.randint(0, len(data) - 1)
            print(f"You are right, your score is: {score}")
        else:
            game_over = True

    print(f"Your final score is: {score}")


game()
