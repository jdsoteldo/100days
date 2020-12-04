# You are going to write a program that calculates the sum of all the even numbers from 1 to 100, including 1 and 100.

sum = 0
othersum = 0

for n in range(1, 101):
  if n % 2 == 0:
    sum += n

print(sum)

# Other solution
for x in range(2, 101, 2):
    othersum += x
print(othersum)
