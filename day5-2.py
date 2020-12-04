# You are going to write a program that calculates the highest score from a List of scores.
# Not allowed to use min() nor max()

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

big_score = 0

for x in student_scores:
    if x > big_score:
        big_score = x

print(f"This highest score is: {big_score}")
