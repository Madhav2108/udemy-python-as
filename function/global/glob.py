def f(): 
    global s 
    print(s) 
    s = "new added"
    print(s)  
s = "before added" 
f() 
print(s) 