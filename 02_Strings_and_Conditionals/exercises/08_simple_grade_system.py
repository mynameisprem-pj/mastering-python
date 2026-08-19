'''Write a program to ask the user for their exam marks (out of 100) 
and output their grade based on the following criteria:  
- Marks >= 90: Grade A   
- 80 <= Marks < 90: Grade B   
- 70 <= Marks < 80: Grade C   
- Marks < 70: Grade D   '''

marks = float(input("Enter total exam marks: "))

if marks >= 90:
    print("Congrats! Grade A")
elif 80 <= marks < 90:
    print("Grade B")
elif 70 <= marks < 80:
    print("Grade C")
elif marks < 70:
    print("Grade D")


