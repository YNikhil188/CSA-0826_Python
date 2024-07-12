def find_max(num1, num2, num3):
    max_num = max(num1, num2)
    max_num = max(max_num, num3)
    return max_num
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
max_num = find_max(num1, num2, num3)
print(f"The maximum of {num1}, {num2}, and {num3} is: {max_num}")