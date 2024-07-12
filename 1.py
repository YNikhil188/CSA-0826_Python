def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_non_prime_numbers(A, B):
    non_prime_numbers = []
    for num in range(A, B+1):
        if not is_prime(num):
            non_prime_numbers.append(num)
    print(", ".join(map(str, non_prime_numbers)))

# Sample Input
A = 12
B = 19

print("Non-Prime numbers between {} and {}:".format(A, B))
print_non_prime_numbers(A, B)