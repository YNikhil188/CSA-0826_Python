sentence=input("enter the sentence:").split()
c=0
for word in sentence:
    if word in sentence:
        c+=1
print("no of sentences is:",c)
        