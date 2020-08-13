
def fib(limit): 
	a, b = 0, 1
	while a < limit: 
		yield a 
		a, b = b, a + b 
x = fib(5) 
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print("\nUsing for in loop") 
x=int(input())
for i in fib(x): 
	print(i) 
