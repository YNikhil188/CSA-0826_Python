# Initialize counters
uppercase_count = 0
lowercase_count = 0
digit_count = 0

# Read characters until '*' is encountered
while True:
    char = input("Enter a character (enter '*' to stop): ")
    if char == '*':
        break
    
    # Count uppercase letters, lowercase letters, and digits
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isdigit():
        digit_count += 1

# Display counts
print("\nSummary:")
print("Uppercase letters:", uppercase_count)
print("Lowercase letters:", lowercase_count)
print("Digits:", digit_count)
