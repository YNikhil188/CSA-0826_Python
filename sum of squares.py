N = int(input("Enter the value of N: "))
sum_of_squares = sum(i**2 for i in range(12, N+1))
print("The sum of squares from 12 to", N, "is:", sum_of_squares)
