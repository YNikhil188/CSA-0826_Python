x=float(input("enter the number1=\n"))
n=float(input("enter the number2=\n"))
choice=int(input("enter the choice 1.pow,2.add,3.sub,4.mul,5.div:"))
if choice==1:
    result=x^n
elif choice==2:
    result=x+n
elif choice==3:
    result=x-n
elif choice==4:
    result=x*n
elif choice==5:
    if n!=0:
        result=x/n
    else:
        print("invalid zero can't be divide with it:")
else:
    print("invalid choice")
print("result=",result)