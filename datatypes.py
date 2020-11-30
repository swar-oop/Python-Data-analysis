# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 20:05:41 2020

@author: swaroop
"""

#List, tupple, dictionary, set, frozen set
#heterogeneous, mutable or changeable, ordered, indexed

#Heterogeneous
L1 = [10, 2.34 , "Star", True]
print(L1)
print(L1[3])
#Mutable or changeable
L1[1] = L1[0]/3
L1

for i in L1:
    print(i)
print("out") #TAB function only

r1= range(100,150,6)
r2= range(3,12)
r1
lr1=list(r1)
lr1
lr2= list(r2)
for i in lr2:
    print(i)
   #print(lr2)
len(lr2)

