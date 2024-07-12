start_num = float(input("Enter the starting number: "))
max_lines = int(input("Max number of lines to print: "))

if max_lines <= 0:
    print("Invalid input. Max number of lines should be a positive integer.")
else:
    for i in range(max_lines):
        line = " ".join([str(start_num + j * 0.1) for j in range(i + 1)])
        print(line)
