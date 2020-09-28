"""if expression:
   statement(s)
   """
var1 = 100
if var1:
   print "1 - Got a true expression value"
   print var1

var2 = 0
if var2:
   print "2 - Got a true expression value"
   print var2
print "Good bye!"
"""if expression:
   statement(s)
else:
   statement(s)"""
var1 = 100
if var1:
   print "1 - Got a true expression value"
   print var1
else:
   print "1 - Got a false expression value"
   print var1

var2 = 0
if var2:
   print "2 - Got a true expression value"
   print var2
else:
   print "2 - Got a false expression value"
   print var2

print "Good bye!"
"""
if expression1:
   statement(s)
elif expression2:
   statement(s)
elif expression3:
   statement(s)
else:
   statement(s)"""
var = 100
if var == 200:
   print "1 - Got a true expression value"
   print var
elif var == 150:
   print "2 - Got a true expression value"
   print var
elif var == 100:
   print "3 - Got a true expression value"
   print var
else:
   print "4 - Got a false expression value"
   print var

print "Good bye!"
"""
if expression1:
   statement(s)
   if expression2:
      statement(s)
   elif expression3:
      statement(s)
   else:
      statement(s)
   elif expression4:
      statement(s)
else:
   statement(s)
   """
var = 100
if var < 200:
   print "Expression value is less than 200"
   if var == 150:
      print "Which is 150"
   elif var == 100:
      print "Which is 100"
   elif var == 50:
      print "Which is 50"
   elif var < 50:
      print "Expression value is less than 50"
else:
   print "Could not find true expression"

print "Good bye!"

var = 100
if ( var == 100 ) : print "Value of expression is 100"
print "Good bye!"

"""
while expression:
   statement(s)
   """
count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1

print "Good bye!"

var = 1
while var == 1 :  # This constructs an infinite loop
   num = raw_input("Enter a number  :")
   print "You entered: ", num
print "Good bye!"


count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"

flag = 1
while (flag): print 'Given flag is really true!'
print "Good bye!"
"""for iterating_var in sequence:
   for iterating_var in sequence:
      statements(s)
   statements(s)

   while expression:
   while expression:
      statement(s)
   statement(s)
   """
i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print i, " is prime"
   i = i + 1

print "Good bye!"

"""BREAK"""
for letter in 'Python':     # First Example
   if letter == 'h':
      break
   print 'Current Letter :', letter
  
var = 10                    # Second Example
while var > 0:              
   print 'Current variable value :', var
   var = var -1
   if var == 5:
      break

print "Good bye!"
"""Continue """
for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print 'Current Letter :', letter

var = 10                    # Second Example
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print 'Current variable value :', var
print "Good bye!"
"""pass"""
for letter in 'Python': 
   if letter == 'h':
      pass
      print 'This is pass block'
   print 'Current Letter :', letter

print "Good bye!"

"""MATHS
abs( x )"""
print "abs(-45) : ", abs(-45)
print "abs(100.12) : ", abs(100.12)
print "abs(119L) : ", abs(119L)
"""Com"""
print "cmp(80, 100) : ", cmp(80, 100)
print "cmp(180, 100) : ", cmp(180, 100)
print "cmp(-80, 100) : ", cmp(-80, 100)
print "cmp(80, -100) : ", cmp(80, -100)
"""import math
math.ceil( x )"""
import math   # This will import math module
print "math.ceil(-45.17) : ", math.ceil(-45.17)
print "math.ceil(100.12) : ", math.ceil(100.12)
print "math.ceil(100.72) : ", math.ceil(100.72)
print "math.ceil(119L) : ", math.ceil(119L)
print "math.ceil(math.pi) : ", math.ceil(math.pi)

"""math.exp( x )"""
import math   # This will import math module

print "math.exp(-45.17) : ", math.exp(-45.17)
print "math.exp(100.12) : ", math.exp(100.12)
print "math.exp(100.72) : ", math.exp(100.72)
print "math.exp(119L) : ", math.exp(119L)
print "math.exp(math.pi) : ", math.exp(math.pi)

print "math.fabs(-45.17) : ", math.fabs(-45.17)
print "math.fabs(100.12) : ", math.fabs(100.12)
print "math.fabs(100.72) : ", math.fabs(100.72)
print "math.fabs(119L) : ", math.fabs(119L)
print "math.fabs(math.pi) : ", math.fabs(math.pi)

print "math.floor(-45.17) : ", math.floor(-45.17)
print "math.floor(100.12) : ", math.floor(100.12)
print "math.floor(100.72) : ", math.floor(100.72)
print "math.floor(119L) : ", math.floor(119L)
print "math.floor(math.pi) : ", math.floor(math.pi)

print "math.log(100.12) : ", math.log(100.12)
print "math.log(100.72) : ", math.log(100.72)
print "math.log(119L) : ", math.log(119L)
print "math.log(math.pi) : ", math.log(math.pi)

print "max(80, 100, 1000) : ", max(80, 100, 1000)
print "max(-20, 100, 400) : ", max(-20, 100, 400)
print "max(-80, -20, -10) : ", max(-80, -20, -10)
print "max(0, 100, -400) : ", max(0, 100, -400)

print "min(80, 100, 1000) : ", min(80, 100, 1000)
print "min(-20, 100, 400) : ", min(-20, 100, 400)
print "min(-80, -20, -10) : ", min(-80, -20, -10)
print "min(0, 100, -400) : ", min(0, 100, -400)

print "math.modf(100.12) : ", math.modf(100.12)
print "math.modf(100.72) : ", math.modf(100.72)
print "math.modf(119L) : ", math.modf(119L)
print "math.modf(math.pi) : ", math.modf(math.pi)

print "math.pow(100, 2) : ", math.pow(100, 2)
print "math.pow(100, -2) : ", math.pow(100, -2)
print "math.pow(2, 4) : ", math.pow(2, 4)
print "math.pow(3, 0) : ", math.pow(3, 0)

print "round(80.23456, 2) : ", round(80.23456, 2)
print "round(100.000056, 3) : ", round(100.000056, 3)
print "round(-100.000056, 3) : ", round(-100.000056, 3)

print "math.sqrt(100) : ", math.sqrt(100)
print "math.sqrt(7) : ", math.sqrt(7)
print "math.sqrt(math.pi) : ", math.sqrt(math.pi)

"""String
var1 = 'Hello World!'
var2 = "Python Programming"
"""
var1 = 'Hello World!'
var2 = "Python Programming"

print "var1[0]: ", var1[0]
print "var2[1:5]: ", var2[1:5]

var1 = 'Hello World!'
print "Updated String :- ", var1[:6] + 'Python'
print "My name is %s and weight is %d kg!" % ('Zara', 21)


para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print para_str

print 'C:\\nowhere'
print r'C:\\nowhere'
print u'Hello, world!'

"""String Functions"""

str = "this is string example....wow!!!"
print "str.capitalize() : ", str.capitalize()

str = "this is string example....wow!!!"
print "str.center(40, 'a') : ", str.center(40, 'a')

str = "this is string example....wow!!!"

sub = "i"
print "str.count(sub, 4, 40) : ", str.count(sub, 4, 40)
sub = "wow"
print "str.count(sub) : ", str.count(sub)

#!/usr/bin/python

Str = "this is string example....wow!!!"
Str = Str.encode('base64','strict')

print "Encoded String: " + Str
print "Decoded String: " + Str.decode('base64','strict')

str = "this is string example....wow!!!"
print "Encoded String: " + str.encode('base64','strict')

str = "this is string example....wow!!!"

suffix = "wow!!!"
print str.endswith(suffix)
print str.endswith(suffix,20)
suffix = "is"
print str.endswith(suffix, 2, 4)
print str.endswith(suffix, 2, 6)

str = "this is\tstring example....wow!!!"
print "Original string: " + str
print "Defualt exapanded tab: " +  str.expandtabs()
print "Double exapanded tab: " +  str.expandtabs(16)

str1 = "this is string example....wow!!!"
str2 = "exam"
print str1.find(str2)
print str1.find(str2, 10)
print str1.find(str2, 40)

str1 = "this is string example....wow!!!"
str2 = "exam"
print str1.index(str2)
print str1.index(str2, 10)
print str1.index(str2, 40)

str = "this2009"  # No space in this string
print str.isalnum()
str = "this is string example....wow!!!"
print str.isalnum()

str = "this"  # No space & digit in this string
print str.isalpha()
str = "this is string example....wow!!!"
print str.isalpha()

str = "123456"  # Only digit in this string
print str.isdigit()
str = "this is string example....wow!!!"
print str.isdigit()

str = "THIS is string example....wow!!!" 
print str.islower()
str = "this is string example....wow!!!"
print str.islower()

str = u"this2009"  
print str.isnumeric()
str = u"23443434"
print str.isnumeric()

str = "       " 
print str.isspace()
str = "This is string example....wow!!!"
print str.isspace()

str = "This Is String Example...Wow!!!"
print str.istitle()
str = "This is string example....wow!!!"
print str.istitle()



str = "THIS IS STRING EXAMPLE....WOW!!!" 
print str.isupper()
str = "THIS is string example....wow!!!"
print str.isupper()

s = "-"
seq = ("a", "b", "c") # This is sequence of strings.
print s.join( seq )

str = "this is string example....wow!!!"
print "Length of the string: ", len(str)


str = "this is string example....wow!!!"
print str.ljust(50, '0')

str = "THIS IS STRING EXAMPLE....WOW!!!"
print str.lower()

str = "     this is string example....wow!!!     "
print str.lstrip()
str = "88888888this is string example....wow!!!8888888"
print str.lstrip('8')

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)
str = "this is string example....wow!!!"
print str.translate(trantab)

str = "this is really a string example....wow!!!"
print "Max character: " + max(str)
str = "this is a string example....wow!!!"
print "Max character: " + max(str)

str = "this-is-real-string-example....wow!!!"
print "Min character: " + min(str)
str = "this-is-a-string-example....wow!!!"
print "Min character: " + min(str)

str = "this is string example....wow!!! this is really string"
print str.replace("is", "was")
print str.replace("is", "was", 3)

str1 = "this is really a string example....wow!!!"
str2 = "is"

print str1.rfind(str2)
print str1.rfind(str2, 0, 10)
print str1.rfind(str2, 10, 0)
print str1.find(str2)
print str1.find(str2, 0, 10)
print str1.find(str2, 10, 0)


str1 = "this is string example....wow!!!"
str2 = "is"
print str1.rindex(str2)
print str1.index(str2)


str = "this is string example....wow!!!"
print str.rjust(50, '0')

str = "     this is string example....wow!!!     "
print str.rstrip()
str = "88888888this is string example....wow!!!8888888"
print str.rstrip('8')


str = "Line1-abcdef \nLine2-abc \nLine4-abcd"
print str.split( )
print str.split(' ', 1 )

str = "Line1-a b c d e f\nLine2- a b c\n\nLine4- a b c d"
print str.splitlines( )
print str.splitlines( 0 )
print str.splitlines( 3 )
print str.splitlines( 4 )
print str.splitlines( 5 )

str = "this is string example....wow!!!"
print str.startswith( 'this' )
print str.startswith( 'is', 2, 4 )
print str.startswith( 'this', 2, 4 )

str = "0000000this is string example....wow!!!0000000"
print str.strip( '0' )

str = "this is string example....wow!!!"
print str.swapcase()
str = "THIS IS STRING EXAMPLE....WOW!!!"
print str.swapcase()

str = "this is string example....wow!!!";
print str.title()

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)
str = "this is string example....wow!!!"
print str.translate(trantab)


from string import maketrans   # Required to call maketrans function.

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)
str = "this is string example....wow!!!"
print str.translate(trantab, 'xm')
str = "this is string example....wow!!!"
print "str.capitalize() : ", str.upper()

str = "this is string example....wow!!!"
print str.zfill(40)
print str.zfill(50)


str = u"this2009"  
print str.isdecimal()
str = u"23443434"
print str.isdecimal()
