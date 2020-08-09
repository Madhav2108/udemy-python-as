import array as arr
a=arr.array('i',[1,2,3])
for i in range (0, 3): 
    print (a[i], end =" ") 
print()
a.insert(2,6)
for i in (a):
    print(i,end=" ")
print()
a.append(78)
for i in (a):
    print(i,end=" ")
print()
print(a[2])
