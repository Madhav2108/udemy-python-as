List = [] 
print(List) 
List.append(1) 
List.append(2) 
List.append(4) 
print(List) 
for i in range(1, 4): 
	List.append(i) 
print(List) 
List.append((5, 6)) 
print(List) 
List2 = ['For', 'Geeks'] 
List.append(List2) 
print(List) 
List.insert(3, 12) 
List.insert(0, 'Geeks') 
print(List) 
List.extend([8, 'Geeks', 'Always']) 
print(List) 
List.remove(8) 
List.remove(12)
print(List)
List.pop() 
print(List)
List.pop(2)
print(List)
Sliced_List = List[::-1] 
print("\nPrinting List in reverse: ") 
print(Sliced_List)
list.sort()
print(list)

