'''Input marks obtained in five subjects.

Calculate:

total
average
percentage

Assume each subject is out of 100.'''

social = float(input("Marks (0-100): "))
english = float(input("Marks (0-100): "))
math = float(input("Marks (0-100): "))
nepali = float(input("Marks (0-100): "))
science = float(input("Marks (0-100): "))

total = social + english + math + nepali + science
avg = total / 5
percentage = (total / 500) * 100

print(f"Total: {total}")
print(f"Average: {avg}")
print(f"Percentage: {percentage}")

