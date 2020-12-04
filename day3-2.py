# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.


# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

height = input("enter your height in m: ")
weight = input("enter you weight in kg: ")

bmi = float(weight) / float(height) ** 2
rounded_bmi = round(bmi)

if bmi < 18.5:
    print(f"Your bmi is: {rounded_bmi}. You are underweight")
elif 18.5 <= bmi <= 25:
    print(f"Your bmi is: {rounded_bmi}. Your weight is ideal.")
elif 25 < bmi <= 30:
    print(f"Your bmi is: {rounded_bmi}. You are slighty overweight.")
elif 30 < bmi <= 35:
    print(f"Your bmi is: {rounded_bmi}. You are obese.")
else:
    print(f"Your bmi is: {rounded_bmi}. You are clinically obese.")
