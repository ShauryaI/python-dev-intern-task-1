# python-dev-intern-task-1
Python Developer Internship Task 1 (Calculator CLI App)

## Python Version ##
Python 3.13.5

## Library used ##
1. ArgumentParser class has been used from argparse library for parsing CLI options/arguments.
2. add_argument function has been called with positional arguments.
3. Format of function: 
    - function_name(argument_name, argument_type, valid_choices_to_be_supplied_by_user, help_text_displayed_for_command_help)
4. Another function parse_args has been used to get the arguments.

## How to run (to be ignored) ##
1. Open terminal in IDE (If CMD then navigate to project directory)
2. Write python calculator.py
 - Error as it was called without arguments 
 - usage: calculator.py [-h] {add,subtract,multiply,divide} num_one num_two
 - calculator.py: error: the following arguments are required: operation, num_one, num_two
3. Call it this way
    - python calculator.py add 5 3
    - python calculator.py subtract 5 3
    - python calculator.py multiply 5 3
    - python calculator.py divide 5 3
    - python calculator.py divide 5 0
4. CLI for this is not as per task description. Rename file to _calculator

## Code ##

1. We have separate function for all the 4 mathematical operations.
2. whenever calculate.py is called, main function gets executed which calls another function calculate.
3. Calculate function gets the input from CLI, handles error if wrong input is provided and then prints the result after calculation.
4. Control go back to main function again which ask user for performing another calculation.
5. If user mention yes, the loop for getting an input, validating, calculating and printing the result repeats, otherwise it's an exit.

## How to run as per task description ##

1. Open terminal in IDE (If CMD then navigate to project directory)
2. Write python calculator.py
3. It will ask for first number, second number, operation sequentially and then prints the result.
