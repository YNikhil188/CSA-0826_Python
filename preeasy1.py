principle=int(input("enter the principle amount:"))
time=int(input("enter the time in the years:"))
sc=str(input("say the customer is senior citizen(yes/no):"))
if sc=="yes":
    ROI=12
else:
    ROI=10
si=principle*time*int(ROI)/100
print("the simple intrest is:",si)
    
