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

L5=[4,7,1,8,3]
L5.sort()
L5
L5.insert(3, 5)
L5
L5 + L5
L6 = list(range(15))
L6
L7=L6[4:12]
L7
L7[-2]
L7[::-1] #reverse list


#set - Heterogeneous, no duplicacy
#unindexed, not changeable, ordered 
s1= {2,5,7,3,6,9,10}
for i in s1:
     print(i)
     
s2 = {'f', 'sad', 'ere', 'po'}
s2
'ere' in s2
s2.add('dshd')
s2
s2.update([34,756,34]) #to add more than one element
s2
len(s2)
s2.remove('sad') #gives error if not present
s2
s2.discard('er') #won't give error
s2.pop() #no indexing inside, gives FIRST element
s3 = {'f', 45, 23, 'ere', 'assasin'}
s2.union(s3)
s2.intersection(s3)
s2.difference(s3)


#dictionary - mutable, key-value paired
#unordered, collection, curly brackets
stu = {'roll':1, "name":"aaaa"}
stu['name']
stu.get('roll')
stu['name']='khikhi'
stu
for i in stu:
    print(i) #returns only key
stu.keys()
stu.values()
for i in stu.values():
    print(i)
stu.items()
for i,j in stu.items():
    print( 'student is ', i, 'info is ', j)
if('name' in stu):
    print('do khikhikhi') #for key only
stu.pop(1)
stu.pop('roll')
stu
stu1 = {'rno':list(range(1,11)), 'marks':list(range(40,60))}
stu1['rno'][4]
stu1 #first key with 10


#tuple - unmutable, collection
#ordered, round bracket
t1 = ()
type(t1)
t1=(1,5,7,3,23)
print(t1)
t1.append(2) #cannot change or remove


#enumerate - can call only once
LE1 = ['ds','ss','rer']
LE1
e1=enumerate(LE1)
e1
for i in e1:
    print(i) #automatically assigns index
e2=enumerate(LE1, start=69)
for i in e2:
    print(i)
le2=list(range(1,100))
e3=enumerate(le2)
j=0
for i in e3:
    print(i)
    if(j==30):
        break
    j+=1
for i in e3:
    print(i)


#frozenset - cannot change
fz1= frozenset([1,3,52,2])
fz1  
fz1.add(56) #doesn't add
s7={67,23,3.4}
fz1.union(s7)
for i in fz1:
    print(i)
    

#zip - map the similar index of multiple containers so that they can be used just using as single entity
name=['jack','ang', 'lee']
marks = [4,6,7]
sex = ['m','f','m']
z1 = zip(name,marks,sex)
for i in z1:
    print(i) #returns 3 tuples
for i,j,k in z1:
    print(i,j,k) #returns 3 diff elements
a,b,c = zip(*z1) #unzip
a,b,c
