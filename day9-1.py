# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.

# Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. The final version of the student_grades dictionary will be checked.

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#1: Create an empty dictionary called student_grades.
student_grades = {}

#2: Write your code below to add the grades to student_grades.👇
for name, grade in student_scores.items():
    if 90 < grade <= 100:
        student_grades[name] = 'Outstanding'
    elif 80 < grade <= 90:
        student_grades[name] = 'Exceeds Expectations'
    elif 70 < grade <= 80:
        student_grades[name] = 'Acceptable'
    elif grade <= 70:
        student_grades[name] = 'Fail'


# 🚨 Don't change the code below 👇
print(student_grades)
