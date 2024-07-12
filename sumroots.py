y=int(input("enter the year"))
if(y%4==0) and (y%100!=0) or (y%400==0):
    print("given year is leap year the next leapyear:",y+4)
else:
    print("not leap year",)