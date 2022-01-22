n=int(input())

a=0
b=1

for x in range(0,n):
    print(a,end='\n')
    c=a+b
    a=b
    b=c
