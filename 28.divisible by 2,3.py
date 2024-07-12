number = int(input("Enter a number: "))
if number % 2 == 0 and number % 3 == 0:
    print(f"{number} is divisible by both 2 and 3.")
elif number % 2 == 0:
    print(f"{number} is divisible by 2, but not by 3.")
elif number % 3 == 0:
    print(f"{number} is divisible by 3, but not by 2.")
else:
    print(f"{number} is not divisible by both 2 and 3.")