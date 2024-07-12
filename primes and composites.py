num = int(input("Enter the number:"))
prime_count = 0
composite_count = 0
for n in range(2, num + 1):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                composite_count += 1
                break
        else:
            prime_count += 1
print("Number of primes:", prime_count)
print("Number of composites:", composite_count)
