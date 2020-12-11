# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
random_coin = random.randint(0, 1)

if random_coin == 0:
    print("Tails")
else:
    print("Heads")

print(random.getstate())
