print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
count1 = 0
count2 = 0
word1 = 'true'
word2 = 'love'

bothnames = name1 + name2

for i in bothnames.lower():
    if i in word1:
        count1 += 1

for j in bothnames.lower():
    if j in word2:
        count2 += 1

score = str(count1) + str(count2)

if int(score) <= 10 or int(score) >= 90:
    print(f"Your score is {score}. Y'all go like coke and mentos.")
elif 40 <= int(score) <= 50:
    print(f"Your score is {score}. Y'all alright together.")
else:
    print(f"Your score is {score}.")
