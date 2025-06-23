# This is simple calculator to perform operation on numbers as mentioned by user in CLI.

from argparse import ArgumentParser

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

parser = ArgumentParser()

parser.add_argument("operation", type=str,
                    choices=["add", "subtract", "multiply", "divide"],
                    help="The operation to run on the given arguments.")
parser.add_argument("num_one", type=float, help="The first number.")
parser.add_argument("num_two", type=float, help="The second number.")

args = parser.parse_args()
operation = args.operation
num_one = args.num_one
num_two = args.num_two

# default value assigned.
result = None
if operation == "add":
    result = add(num_one, num_two)
elif operation == "subtract":
    result = subtract(num_one, num_two)
elif operation == "multiply":
    result = multiply(num_one, num_two)
else:
    result = divide(num_one, num_two)

# f as formatter
print(f"Result: {result}")