def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
A = int(input("Enter the starting number (A): "))
B = int(input("Enter the ending number (B): "))
print("Non-prime numbers between", A, "and", B, "are:")
for num in range(A, B + 1):
    if not is_prime(num):
        print(num, end=" ")
