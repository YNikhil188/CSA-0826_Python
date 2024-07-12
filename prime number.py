def simple(prin,time,sen):
    rate = 12 if sen else 10
    return (prin*time*rate)/100
prin=float(input("enter the prin amount:"))
time=float(input("enter the time taken:"))
sen=input("sen citizen? (yes/no):").lower()=="yes"
print("the simple interest is ",simple(prin,time,sen))