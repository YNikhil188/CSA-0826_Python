num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
and_result = num1 & num2
print("Bitwise AND in binary format: ", bin(and_result))
or_result = num1 | num2
print("Bitwise OR in binary format: ", bin(or_result))
xor_result = num1 ^ num2
print("Bitwise XOR in binary format: ", bin(xor_result))
left_shift = num1 << 2
print("Left shift by 2 in binary format: ", bin(left_shift))
right_shift = num2 >> 3
print("Right shift by 3 in binary format: ", bin(right_shift))