a=int(input("Enter Number"))
b=int(input("Enter Range"))
max=0
min=a
for i in range(a,b):
    if max<i:
        max=i
    if min>i:
        min=i
print(max)
print(min)