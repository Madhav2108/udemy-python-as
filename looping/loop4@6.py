a=int(input("Enter Number"))
b=int(input("Enter Range"))
f=0
c=0
for i in [a,b]:
    for j in range(2,i+1):
        if i%j==0:
            c=c+1
    if c!=1:
        f=0
        print("invalid")
        break
    else:
        f=1
    c=0
if f==1:
    if a-b==2 or a-b==-2:
        print("Twin Prime") 
    else:
        print("prime but not twin") 
