import matplotlib.pyplot as p
l1=list()
for i in range(1,50):
    if i%3==0:
        l1.append(i+50)
    else:
        l1.append(i-5)
print(l1)
l2=list()
for i in range(1,50):
    if i%3==0:
        l2.append(i+10)
    else:
        l2.append(i-10)

print(l2)
p.plot([1,2,3],[1,2,33,'bo')
#p.plot(l1,l1)
p.ylabel('Y Range')
p.xlabel('X Range')
p.title("First Plot")
p.show()
