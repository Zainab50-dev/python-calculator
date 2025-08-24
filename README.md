This is a simple calculator built using Python. The program runs continuously in a while loop until the user types "exit".

# Key features of the project:
# Exit condition:
The first number is initially taken as a string to check if the user wants to exit. If "exit" is entered, the program terminates gracefully.
# Operator input:
The user can choose an operator to perform the desired calculation.
# Type conversion: 
Numbers are later converted into floats to handle decimal inputs.
# Functions for operations: 
Each operation has its own function, which is called based on the chosen operator.
# Error handling:
try and except blocks are used to handle invalid inputs and prevent the program from crashing.
# Invalid operator check:
If the user enters an unsupported operator, the program displays an appropriate error message.

Division by zero is specifically handled with a ZeroDivisionError check.
