#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.
print("Welcome to tip calculator")
pretotal = float(input("How much was the bill?\n"))
tip = float(input("What percentage of tip?\n"))
people = float(input("how many people to split the bill?\n"))

tip_percentage = tip * 0.01
each_tip = pretotal * tip_percentage / people
print(each_tip)
pay = (pretotal / people) + each_tip
print("Each person should pay: $" "%.2f" % pay)
