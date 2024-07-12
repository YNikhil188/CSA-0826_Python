principle=int(input("enter the principle amount :"))
time=int(input("enter the time in years:"))
senior_citizen=str(input("check the customer is senior citizen (yes/no):")).lower()
if senior_citizen=="yes":
    rate_of_intrest=12
else:
    rate_of_intrest=10
intrest=principle*time*rate_of_intrest/100
print("the intrest is :",intrest)