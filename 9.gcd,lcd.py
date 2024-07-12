import math
import functools
def gcd(a, b):
    return math.gcd(a, b)
def lcm(numbers):
    return abs(functools.reduce(gcd, numbers)) * functools.reduce(lambda x, y: x * y, numbers)
n = int(input("Enter the number of numbers: "))
numbers = [int(input(f"Enter number {i + 1}: ")) for i in range(n)]
gcd_result = gcd(numbers[0], numbers[1])
for num in numbers[2:]:
    gcd_result = gcd(gcd_result, num)
lcm_result = lcm(numbers)
print("GCD of the given numbers: ", gcd_result)
print("LCM of the given numbers: ", lcm_result)