import random

rock = '''

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors = '''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

images = [rock, paper, scissors]

choice = input("What do you choose? 1 for Rock, 2 for Paper, 3 for Scissors. ")
print(images[int(choice)])

computer = random.randint(1, 3)
print('Computer choose:\n', images[computer - 1])

if choice == '1' and computer == 2:
    print('You Lose :(')
elif choice == '1' and computer == 3:
    print('You Win :)')
elif choice == '2' and computer == 1:
    print('You Win :)')
elif choice == '2' and computer == 3:
    print('You Lose :(')
elif choice == '3' and computer == 1:
    print('You Lose :(')
elif choice == '3' and computer == 2:
    print('You Win :)')
else:
    print('Tie -_-')
