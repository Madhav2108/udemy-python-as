def add(a,b):
    c=a+b
    print(c)
def sub(a,b):
    c=a-b
    print(c)
def mul(a,b):
    c=a*b
    print(c)
def div(a,b):
    c=a/b
    print(c)
for i in range(1,5,1):
    a=int(input("Enter Value of a: "))
    b=int(input("Enter Value of b: "))
    n=int(input("1 for add,2 for sub,3 for div,4 for mul: "))
    if n==1:
        add(a,b)
    elif n==2:
        sub(a,b)
    elif n==3:
        div(a,b)
    elif n==4:
       mul(a,b)
    else:
        print("Not a Valid Input")

