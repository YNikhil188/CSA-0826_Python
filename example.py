rows = 5

for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows+i):
        print(" ", end=" ")
    
    # Print numbers
    for k in range(1, i + 1):
        print(k, end=" ")
    
    print()

