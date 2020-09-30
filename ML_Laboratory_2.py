# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 19:00:02 2020

@author: Lado(PC)
"""

#1
    
a = int(input("EnterNum: "))
if a>0:
  print("Enter Num is a positevi",a)  

#2

a = int(input("EnterNum: "))
b = a % 10
c = b // 2 
if a % 10 != c:
    print("Ricxvi ar bolovdeba 0-it",a)
else:
    print("Ricxvi bolovdeba 0-it",a)

#3

a1 = int(input("EnterNum: "))
a2 = int(input("EnterNum: "))
b = a1
c = a2 
if a1>10 and a2>10:
    res=[a1,a2]
    print("Sashualo",(sum(res)/2))
else:
    print("Namravli",a1*a2)

#4

a = int(input("EnterNum: "))
if   a>0:
    print("Enter Num is a positevi",a)
elif a<0:
    print("Enter Num is a negative",a)
else:
    print("Enter Num is a Zero",a)   

#5

n = int(input("EnterNum: "))
a = n % 10
print("bolo ricxvi:",a)

##############################################
#1



















