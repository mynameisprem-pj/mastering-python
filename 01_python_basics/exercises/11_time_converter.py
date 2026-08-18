'''19_time_converter.py

Input total minutes.

Convert into hours and remaining minutes.

Example:

Enter minutes: 135


Hours: 2
Minutes: 15

Hint: You'll need / or // and %. Try to figure it out yourself first.'''

mins = float(input("Enter total minutes: "))
hrs = mins // 60
remaining_mins = mins % 60

print(f"Hours: {hrs}")
print(f"Minutes: {remaining_mins}")