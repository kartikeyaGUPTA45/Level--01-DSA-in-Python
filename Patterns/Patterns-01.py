n=int(input())


'''Number of rows'''

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end='\t')
    print(end='\n')
