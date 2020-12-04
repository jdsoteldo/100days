print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

price = 0
small_price = 15
medium_price = 20
large_price = 25

if size.lower() == 's':
    price = small_price
elif size.lower() == 'm':
    price = medium_price
elif size.lower() == 'l':
    price = large_price
else:
    print("Invalid size")

if add_pepperoni.lower() == 'y':
    if size.lower() == 's':
        price += 2
    else:
        price += 3

if extra_cheese.lower() == 'y':
    price += 1

print(f"Your bill is ${price}")
