import math

def c_to_f(c):
    return (c * 9 / 5) + 32


def f_to_c(f):
    return (f - 32) * 5 / 9


def get_temperature():
    while True:
        try:
            return float(input("Enter the temperature value: ").strip())
        except ValueError:
            print("Invalid number.")


def main():
    while True:
        print("\nTemperature Converter \n-----------------")
        print("C - Celsius to Fahrenheit")
        print("F - Fahrenheit to Celsius")
        print("B - Back to Main Menu")

        choice = input("> ").strip().upper()

        if choice == "C":
            temp = get_temperature()
            print(f"{temp}°C = {c_to_f(temp):.2f}°F")

        elif choice == "F":
            temp = get_temperature()
            print(f"{temp}°F = {f_to_c(temp):.2f}°C")

        elif choice == "B":
            print("Back to Main Script")
            return # Back to Math.py
        else:
            print("Invalid option.")
