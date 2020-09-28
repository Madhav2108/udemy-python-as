# a=5
# b=6
a=int(input("Enter Value of a :"))
b=int(input("Enter Value of b :"))
c=int(input("Enter Value of c :"))
if a>b and a>c:
    print(a," is G")
elif b>a and b>c:
    print(b," is G")
else:
    print(c ," is G")