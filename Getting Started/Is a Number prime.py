t=int(input())
while(t>0):
    n=int(input())
    isprime=True
    for i in range(2,n):
        if n%i==0:
            isprime=False
            break
            
    if isprime==True:
        print("prime")
    else :
        print("not prime")
    
    t=t-1
            
    
