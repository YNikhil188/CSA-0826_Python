l=int(input("enter the limit:"))
c=0
m=2
while c<0:
    for n in range(1,m) :
     a=m*m-n*n
     b=2*m*n
     c=m*m+n*n
    if c>l:
        break
        print( a, b, c)
        m=m+1
        
    
    
