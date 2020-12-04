# You are going to write a program that automatically prints the solution to the FizzBuzz game
# if x % 3 == 0 print Fizz, elif x % 5 == 0 print Buzz if x % 5 and % 3 print fizzbuzz
# else print x

for x in range(1, 101):
    if x % 5 == 0 and x % 3 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
