a="Python"
b="JAVA"
c="C++"
#a,b,c="Python","JAVA","C++"
#a,b,c="PYTHON"
print(a)# Output:Python
print(a*3)# Output:PythonPythonPython
print("%s"%a)# Output:Python
print ("Lang1 is %s ,Lang2 is %s Lang3  is %s" % (a,b,c)) #output:Lang1 is Python ,Lang2 is JAVA Lang3  is C++
print("{},{},{}".format(a,b,c))# Output:Python,JAVA,C++
print("{1},{2},{0}".format(a,b,c))# Output:JAVA,C++,Python
print("{2},{0},{1}".format(a,b,c))# Output:C++,Python,JAVA
print('Hello {lang1}, {lang2}'.format(lang1 = 'C++', lang2= 'JAVA'))# Output:Hello C++, JAVA
print('Hello {lang2}, {lang1}'.format(lang1 = 'C++', lang2= 'JAVA'))# Output:Hello JAVA, C++
print(1,2,3,4)# Output: 1 2 3 4
print(1,2,3,4,sep='*')# Output: 1*2*3*4
print(1,2,3,4,sep='#',end='&')#Output: 1#2#3#4&
print()
t=(5,8,3,9)
print(t,sep='#',end='&')#Output: (5, 8, 3, 9)&
print() 
str="""Strings are amongst the most popular types in Python."""
print(str)





