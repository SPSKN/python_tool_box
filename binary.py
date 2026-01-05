def decimal_to_binary(n: int) -> str:
    """Convert decimal integer to binary string."""
    return bin(n)[2:]  # Remove '0b' prefix


def get_decimal_input() -> int:
    while True:
        try:
            return int(input("Enter a decimal number: ").strip())
        except ValueError:
            print("Invalid input. Please enter an integer.")


def main():
    """
    Interactive Binary Converter.
    After each conversion, user can:
        - Convert another number
        - Go back to main menu
    """
    while True:
        print("\nBinary Converter\n----------------")
        number = get_decimal_input()
        binary = decimal_to_binary(number)
        print(f"Decimal {number} = Binary {binary}")

        while True:
            again = input("\nConvert another number? (Y/N) or B to go back: ").strip().upper()
            if again == "Y":
                break  # repeat the loop
            elif again == "B" or again == "N":
                print("Returning to main menu...")
                return
            else:
                print("Invalid input. Enter Y, N, or B.")
