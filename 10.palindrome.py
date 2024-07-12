import random

def is_palindrome(value):
    if isinstance(value, str):
        return value == value[::-1]
    elif isinstance(value, int):
        return str(value) == str(value)[::-1]
    else:
        raise ValueError("Invalid input type. Please provide a string or integer.")
check_type = random.choice([True, False])

if check_type:
    value = input("Enter a string: ")
else:
    value = int(input("Enter a number: "))

is_palindrome_result = is_palindrome(value)

if check_type:
    print("Is the given string a palindrome? ", is_palindrome_result)
else:
    print("Is the given number a palindrome? ", is_palindrome_result)