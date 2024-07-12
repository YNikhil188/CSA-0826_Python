num1=int(input("enter the number1:"))
num2=int(input("enter the number2:"))
num3=int(input("enter the number3:"))
if num1>=num2 and num1>=num3 :
    print("largest number is",num1)
elif num2>=num1 and num2>=num3:
    print("largest number is",num2)
else:       
    print("largest number is",num3)  