# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

numbers = input("Type a two digit number: ")
print(int(numbers[0]) + int(numbers[-1]))
