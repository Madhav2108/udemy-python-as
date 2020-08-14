x = 15
def change(): 
    global x 
    x = x + 5 
    print("change inside", x) 
change() 
print("after change", x) 