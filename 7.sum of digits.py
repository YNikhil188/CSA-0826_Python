def sum_of_digits(n):
    sum_of_digits = 0
    num = n
    while num >= 10:
        while num > 0:
            sum_of_digits += num % 10
            num = num // 10
        num = sum_of_digits
        sum_of_digits = 0
    return num
n = int(input("Enter N value: "))
num = int(input(f"Enter {n}-digit number: "))
sum_result = sum_of_digits(num)
print(f"Sum of {n}-digit number: {sum_result}")