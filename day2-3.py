# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

current_age = input("What is your current age? ")

age_int = int(current_age)

remaining_months = 90 * 12 - (age_int * 12)
remaining_weeks = 90 * 52 - (age_int * 52)
remaining_days = 90 * 365 - (age_int * 365)

print(f"you have {remaining_days} days, {remaining_weeks} weeks and {remaining_months} months left.")
