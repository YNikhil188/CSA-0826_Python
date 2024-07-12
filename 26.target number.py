numbers = tuple(map(int, input("Enter a tuple of numbers (separated by comma): ").strip().split(',')))
target_number = int(input("Enter target number: "))
count = sum(1 for num in numbers if num == target_number)
print(f"The count of {target_number} in the given tuple is: {count}")