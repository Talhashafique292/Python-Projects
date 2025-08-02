# Exception Handling

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# except Exception as e:
#     print(f'An unexpected error occurred: {e}')

# try:
#     result = 10 / 2
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# else:
#     print(f"Division successful. Result: {result}")


# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# finally:
#     print("This will always execute.")


# def divide_numbers(a, b):
#     try:
#         result = a / b  # Test this block for errors
#     except ZeroDivisionError:
#         print("Error: Cannot divide by zero!")
#     except TypeError:
#         print("Error: Invalid input type. Numbers required.")
#     else:
#         print(f"Division successful. Result: {result}")
#     finally:
#         print("Operation complete.")


# # Test cases
# divide_numbers(10, 2)  # Successful division
# divide_numbers(10, 0)  # ZeroDivisionError
# divide_numbers(10, "2")  # TypeError
# Calculator

import random
from typing import List, Tuple, Dict
