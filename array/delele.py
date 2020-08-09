import array as arr
a=arr.array('i',[5,6,7,89,0,0,0,4,5,6])
for i in (a):
    print(i,end=" ")
print()
a.pop(3)
for i in (a):
    print(i,end=" ")
print()
a.remove(0)
a.remove(0)
for i in (a):
    print(i,end=" ")
print()
inde=a.index(7)
print(inde)
a[1]=7
inde=a.index(7)
print(inde)

