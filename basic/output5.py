value1 = eval(input('Please enter a number: '))
value2 = eval(input('Please enter another number: '))
sum = value1 + value2
print(value1, '+', value2, '=', sum)
x, y, z = 3, -4, 0
x = -x
y = -y
z = -z
print(x, y, z)
print(-(4 - 5))
print(10/3, 3/10, 10//3, 3//10)
print(10%3, 3%10)
print(10.0/3.0, 3.0/10.0, 10.0//3.0, 3//10.0)
one = 1.0
one_third = 1.0/3.0
zero = one - one_third - one_third - one_third
print('one =', one, ' one_third =', one_third, ' zero =', zero)
one = 1.0
one_tenth = 1.0/10.0
print('one =', one, ' one_tenth =', one_tenth, ' zero =', zero)
print(-3 + 2)
print(-(3 + 2))
dividend, divisor = eval(input('Please enter two numbers to divide: '))
print(dividend, '/', divisor, "=", dividend/divisor)
value = eval(input('Please enter a number to cut in half: '))
print(value/2)
degreesF = eval(input('Enter the temperature in degrees F: '))
degreesC = 5/9*(degreesF - 32);
print(degreesF, "degrees F =", degreesC, 'degrees C')
seconds = eval(input("Please enter the number of seconds:"))
hours = seconds // 3600 # 3600 seconds = 1 hours
seconds = seconds % 3600
minutes = seconds // 60 # 60 seconds = 1 minute
seconds = seconds % 60
print(hours, "hr,", minutes, "min,", seconds, "sec")
seconds = eval(input("Please enter the number of seconds:"))
hours = seconds // 3600 # 3600 seconds = 1 hours
seconds = seconds % 3600
minutes = seconds // 60 # 60 seconds = 1 minute
seconds = seconds % 60
print(hours, ":", sep="", end="")
tens = minutes // 10
ones = minutes % 10
print(tens, ones, ":", sep="", end="")
tens = seconds // 10
ones = seconds % 10
print(tens, ones, sep ="")
degreesF, degreesC = 0, 0
degreesC = 5/9*(degreesF - 32)
degreesF = eval(input('Enter the temperature in degrees F: '))
print(degreesF, "degrees F =", degreesC, 'degrees C')
x1 = 2
x2 = 2
x1 += 1
x2 -= 1
print(x1)
print(x2)

