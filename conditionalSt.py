# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 19:03:34 2020

@author: swaroop
"""

a=10
if(a>5):
    print("a is greater than 5")
b=int(input("enter b  ")) #convert input to integer
c=int(input("enter c  "))
if(c>b):
    print("c great")
else:
    print("b great")
a<b
a!=b

Marks=int(input("Enter marks"))
if(Marks>85):
    print("Grade A")
elif(Marks<85 and Marks >=75):
    print("Grade B")
elif(Marks<70 and Marks >= 50):
    print("Grade C")
else:
    print("Grade Fail")
    
x=3; y=4;z=5
if x<y and y<z:
    print("both true")
    
L1=['a','b','c','d','e']
for i in range(len(L1)):
    print("Index ", i, "have element " ,L1[i])
for j in range(1,11):
    print("2 * ",i," = ", 2*j)
#nested loops
for k in range(1,11):
    for l in range(1,11):
        print(k," * ",l, " = ", k*l)
