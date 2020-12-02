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

for z in L1:
    if z=='c':
        print(z, "yes")
        break
    print(z, "noo")
for z in L1:
    if z=='c':
        print(z, "yes")
        continue #skips next steps for this iter
    print(z, "noo")
'''for z in L1:
    if z=='c':
        print(z, "yes")
        pass 
    print(z, "noo")'''

#functions
s=23; t=35
def oper():
    print("this is func")
    print(s+t)
    print(s*t)
oper()
def oper1(s=8,t=4): #default val cannot precede non default
    print(s+t)
    print(s*t)
    print(s-t)
    print(s/t)
oper1(3,6)
M=int(input("Enter first no"))
N=int(input("Enter second no"))
oper1(M, N)
oper1()
def reverse(s):
    return(s[::-1])
reverse('swaroop')


import random as rd

li=[1,23,4,56,7]
print(random.choice(li))
random.randint(20, 100)
lis=range(1,100)
rd.choices(lis,k=10)
se={2,4,7,1,5,9}
#convert to tuple from set, dict to use random
weights=rd.choices(tuple(se), k=5)
print("Random from set ", weights)

for i in range(3):
    rd.seed(5) #freezes a random number
    print(rd.randint(65, 600))
    
