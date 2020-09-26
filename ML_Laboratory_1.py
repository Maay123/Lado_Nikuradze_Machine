# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:59:56 2020

@author: Lado(PC)
"""


print((4-pow(2,3))+(5*2)-(3/2))

print(42+3*3/2+4)
print(42+3*3//2+4)


message="whats up doc"
print(message)


a=1
b=4
a,b=b,a
print(a,b)   


x,y=2,6
x,y=y,x+2
print(x,y)


FirstNameUser=input("FirstName: ")
LastNameUser=input("LastName: ")
print(FirstNameUser,LastNameUser)


#11011
a=input("Введите двоичное целое число =") 
print("Двоичное целое число",a, "соответствует десятичному числу", int(a, 2))


MonthTime=int(input("MonthTimeMoney: "))
TimeMoney=int(input("TimeMoney: "))
jami=MonthTime*TimeMoney
print(jami)


num_1=int(input("EnterNum: "))
num_2=int(input("EnterNum: "))
num_3=int(input("EnterNum: "))
lean=[num_1,num_2,num_3]
print(sum(lean)/len(lean))


FirstNameUser=input("FirstName: ")
LastNameUser=input("LastName: ")
Age=int(input("Age: "))
info=[100-Age]
print("\n","FirstName:", FirstNameUser,"\n","LastName:",LastNameUser,"\n","Asi wlis gaxdebi",info,"wlis mere")



Cels=float(input("CelsTemp: "))
Faren=float(input("FarenTemp: "))
infoF=[(Cels*9/5)+32]
infoC=[(Faren-32)*(5/9)]
print(infoF,infoC)





























