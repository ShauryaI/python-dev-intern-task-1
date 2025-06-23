# This is simple calculator to perform operation on numbers as mentioned by user in CLI.

def add(num1: float, num2: float) -> float:
    # sum seems to be a reserved name
    addition = num1 + num2
    return addition

def subtract(num1: float, num2: float) -> float:
    difference = num1 - num2
    return difference

def multiply(num1: float, num2: float) -> float:
    product = num1 * num2
    return product

def divide(num1: float, num2: float) -> (float | str):
    if num2 == 0:
        print("Error: Divide by zero error")
        return "Infinity"
    quotient = num1 / num2
    return round(quotient, 2)

# Function to perform the calculation on inputs provided by user in CLI.
def calculate():
    # There is no do while loop in Python
    global number_1, number_2

    valid_input = False
    while not valid_input:
        number_1 = input("Enter first number: ")
        try:
            number_1 = float(number_1)
            valid_input = True
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    valid_input = False
    while not valid_input:
        number_2 = input("Enter second number: ")
        try:
            number_2 = float(number_2)
            valid_input = True
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    valid_input = False
    while not valid_input:
        operation = input("Enter the operation (+, -, *, /): ")
        allowed_operations = ["+", "-", "*", "/"]
        if operation in allowed_operations:
            valid_input = True
            if operation == "+":
                result = add(number_1, number_2)
            elif operation == "-":
                result = subtract(number_1, number_2)
            elif operation == "*":
                result = multiply(number_1, number_2)
            elif operation == "/":
                result = divide(number_1, number_2)
            else:
                result = "Error: Invalid operation"

            print(f"Result: {result}")
        else:
            print("Error: Please enter a valid symbol for operation.")

def main():
    while True:
        calculate()
        another_calculation = input("Perform another calculation? (yes/no): ").lower()
        if another_calculation != 'yes':
            break
    print("Exit calculator.")

if __name__ == "__main__":
    main()