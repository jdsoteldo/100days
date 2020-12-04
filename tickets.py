print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0
if height >= 120:
    print("You can ride")
    age = int(input("How old are u? "))
    if age < 12:
        bill = 5
        print(f"Children pay ${bill}")
    elif age <= 18:
        bill = 7
        print(f"Youth pay ${bill}")
    elif 45 <= age <= 55:
        print("Dont worry, its on us.")
    else:
        bill = 12
        print(f"Adults pay ${bill}")

    photo = input("Do you want a picture?\n")
    if photo.lower()[0] == 'y':
        bill += 3

    if bill > 0:
        print(f"You final bill is ${bill}")
    else:
        print("It's FREE :)")

else:
    print("Sorry :( you can't ride")
