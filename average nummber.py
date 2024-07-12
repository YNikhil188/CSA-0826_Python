def average_number(num):
    total=sum(num)
    average=total/len(num)
    return average
num=input("enter the number")
avg=average_number(num)
print("the average is",avg)
