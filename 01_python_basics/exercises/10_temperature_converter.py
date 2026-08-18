'''18_temperature_converter.py

Input Celsius.

Convert to Fahrenheit:

F = (C × 9/5) + 32

Example:

Celsius: 25
Fahrenheit: 77.0'''

celcius = float(input("Enter temperature in celcius: "))
fah = (celcius * 9/5) + 32
print(f"Fahrenheit: {fah}")