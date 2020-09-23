a=int(input("Enter Number"))
b=int(input("Enter Range"))
#f=1
c=0
for i in range(a,b):
    for j in range(2,i+1):
        if i%j==0:
            c=c+1
    if c==1:
        print(i)
    c=0
    
