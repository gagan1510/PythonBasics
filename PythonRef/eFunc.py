import math

x = 90
eval('print(math.sin(x))') # eval() evaluates the string which is passed to it
exec('for i in range(1, 11):print(i)')
# exec(open('funcAdv.py').read()) # this executes the file 'funcAdv.py'

print("\nThis is the part which is executed by the compile function")
a = 10
b = 20
str = 'print(3*a , 4*b)'
c1 = compile(str, '', 'exec')
exec(c1)
