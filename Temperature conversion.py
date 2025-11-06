# Write a program to convert temperature back and forth between Celsius(c) and Fahrenheit(f)
# Equation for conversion :
# f = ((9*c)/5)+32
# c = ((f-32)*5)/9

unit = input("Enter the known unit of temperature (C/F) : ")
reading = float(input("Enter the temperature value : "))

if unit.lower() == "c":
    f = ((9*reading)/5) + 32
    print(f"The temperature in Fahrenheit is {f:.1f}°F")
elif unit.lower() == "f":
    c = ((reading-32)*5)/9
    print(f"The temperature in Celsius is {c:.1f}°C")
else:
    print("Unit not valid! Please enter only 'C' or 'F'.")