# -*- coding: utf-8 -*-
"""
Spyder Editor
comment: '''  ''' OR #
This is a temporary script file.
"""

print("HI")
print("Hi","Swaroop", sep=' :) ', end = '***')
print("Ok bye")
#!pip list

import pandas as pd
pd.__version__

s1= input()
s2=input("Enter age")
print(s2)
print(f"My name is {s1} and My age is {s2}")

a = 10 #assignment variable
#type casting or type conversion
f_to_i = int(12.54)
f_to_i
stoi = int('420')
type(stoi)
i_s = str(323)
i_s

chr(67) #convert to ASCII
chr(99)
ord('s')

x=4
x +=1
y= x % 3 #modulo
y
z=10
print(x+2, x-2, x*2, x**2, x/2, x%2, x==2)
print(True or False)
print(x and z)
print(x or z)
print(not x)

fname = "swaroop"
lname=" sahoo"
name = fname + lname
print(name)
print(name.capitalize())
print(name.upper())
print(name.rjust(30))
print(name.ljust(5))
print(name.center(30))
new = name.replace('sahoo', 'smart')
new
n="     hello    "
print(n.strip())


