'''
Input marks for three subjects:

Python
Math
English

Calculate the average.

Then print whether the average is:

>= 40

as True or False.'''

python = float(input("Enter mark for python: "))
math = float(input("Enter mark for math: "))
english = float(input("Enter mark for english: "))

avg = (python + math + english) / 3
print(f"Average: {avg}")
print(avg >= 40)

