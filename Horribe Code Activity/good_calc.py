"""
Calculator w/ good coding practices
Author: Tristan Coleman
"""

def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Return the difference between two numbers."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b

def get_numeric_input(prompt: str) -> float:
    """Safely prompt the user for a numeric value (DRY principle)."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply
    }

    print("Simple Calculator Program")
    num1 = get_numeric_input("Enter the first number: ")
    op = input(f"Choose an operation: ")
    num2 = get_numeric_input("Enter the second number: ")

    if op not in operations:
        print(f"Error: Unsupported operation '{op}'.")
        return

    try:
        result = operations[op](num1, num2)
        print(f"Result: {num1} {op} {num2} = {result}")
    except ValueError as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    main()