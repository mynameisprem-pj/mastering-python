'''
08_rectangle_calculator.py

Input:

length
width

Calculate and print:

area
perimeter
'''

length = float(input("Enter lenght of a rectangle: "))
width = float(input("Enter width of a rectangle: "))

area = length * width
perimeter = 2 * (length + width)

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")