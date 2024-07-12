numbers = list(map(int, input("Enter a list of numbers (separated by space): ").strip().split()))
print("List elements in reverse order: ", end="")
for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i], end=" ")
print()