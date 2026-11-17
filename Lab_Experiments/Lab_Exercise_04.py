# Simple calculator
import math
print("--- Simple Calculator ---")
print("Operations: +, -, *, /")
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))
if operator == '+':
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif operator == '-':
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif operator == '*':
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid operator entered.")
# area calculation
# Program to calculate the area of a rectangle and a circle

print("--- Area Calculator ---")
# 1. Area of a Rectangle (Area = length * width)
print("\nRectangle:")
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
rect_area = length * width
print(f"The area of the rectangle is: {rect_area}")
# 2. Area of a Circle (Area = π * r^2)
print("\nCircle:")
radius = float(input("Enter the radius: "))
# Using math.pi for accurate Pi value and ** for exponentiation
(squared)
circle_area = math.pi * (radius ** 2)
# Rounding to 2 decimal places for cleaner output
print(f"The area of the circle is: {round(circle_area, 2)}")
