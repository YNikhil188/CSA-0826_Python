number = int(input("Enter a number to check if it's a happy number: "))
while number != 1 and number!=4:  # 4 is the only unhappy number in the sequence
    number_str = str(number)
    sum_squares = 0
    for digit_char in number_str:
        digit = int(digit_char)
        sum_squares += digit ** 2
        number = sum_squares
if number == 1:
    print("It's a happy number.")
else:
    print("It's not a happy number.")
