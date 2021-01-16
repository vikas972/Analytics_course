# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 17:14:51 2021

@author: vikas.maurya
"""


#Module3–Deep Dive -Functions, OOPs, Modules, Errors and Exceptions


#Case Study 1.
'''
A Robot moves in a Plane starting from the origin point (0,0).
 The robot can move toward UP, DOWN, LEFT, RIGHT. 
 The trace of Robot movement is as given following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after directions are steps.  
Write a program to compute the distance current position after sequence of movements.
 
 Hint: Use math module.
 '''
startPos=[0,0]
endPos=[]
 
x=0
y=0
def up(x,y,val):
     y=y+val
     return y
def down(x,y,val):
     y=y-val
     return y
def left(x,y,val):
     x=x-val
     return x
def right(x,y,val):
     x=x+val
     return x

def calc(x,y):    
    y=up(x,y,5)
    y=down(x,y,3)
    x=left(x,y,3) 
    x=right(x,y,2)
    endPos.append(x)
    endPos.append(y)

calc(x,y)
endPos
import math
dir(math)
print(math.dist(startPos,endPos))


p=startPos
q=endPos

ans=math.sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))
print(ans)
 
 
 
 '''
 2.Data of XYZ company is stored in sorted list. 
 Write a program for searching specific data from that list.
 Hint: Use if/elif to deal with conditions.
 '''
CompanyData=[15,2,4,19,25,55,12,88]
CompanyData.sort()
input_tofind=int(input("Enter the number to find in sorted list : "))
flag=0
for i in CompanyData:
    if(i==input_tofind):
       
        flag=1
        break
 
if(flag):
    print("Found")
    
else:
    print("Not Found")
    
    
    
 '''
 3.Weather forecasting organization wants to show is it day or night.
 So, write a program for such organization to findwhether is it dark outside or not.
 Hint: Use time module.
 '''
 
 
from datetime import datetime


def get_part_of_day(hour):
    return (
        "light" if 5 <= hour <= 18
        else
        "dark"
    )


h = datetime.now().hour

print(f"Its {get_part_of_day(h)}  right now.")
 
 
 
 '''
 4.Write a program to find distance between two locations when their latitude and longitudes 
 are given.Hint: Use math module.
 '''
 
from math import radians, sin, cos, acos

print("Input coordinates of two points:")
slat = radians(float(input("Starting latitude: ")))
slon = radians(float(input("Ending longitude: ")))
elat = radians(float(input("Starting latitude: ")))
elon = radians(float(input("Ending longitude: ")))

dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
print("The distance is %.2fkm." % dist)
 
 
 
 
 
 
 '''
 5.Design a software for bank system. There should be options like cash withdraw,
 cash credit and change password. According to user input, the software should provide
 required output.Hint: Use if else statements and functions.
 '''
def CashWithdrawal():
    PIN=input('Enter ATM or CARD PIN to proceed:')
    if PIN==123:
        print('***Thank You For Banking With Us***')
    else:
        print('You Have Enterd Invalid PIN. Try Again')

def CashCredit():
    PIN=input('Enter ATM or CARD PIN to proceed:')
    if PIN==123:
        AMT=input('Enter Amount That You Wish to Credit To Bank:')
        print('***Thank You For Banking With Us***')
    else:
        print('You Have Enterd Invalid PIN. Try Again')

def ChangePassword():
    PIN=input('Enter ATM or CARD PIN to proceed:')
    if PIN==123:
        OLD_PWD=raw_input('Please Enter Your Old Password:')
        print('***Thank You For Banking With Us***')
    else:
        print('You Have Enterd Invalid PIN. Try Again')

def Main():
    print('Welcome to XYZ Bank\nChoose from below options')
    print('1. Case withdrawal\n2. Cash credit\n3. Change password')
    opt=input('Enter your option:')
    if opt==1:
        CashWithdrawal()
    if opt==2:
        CashCredit()
    if opt==3:
        ChangePassword()

Main()
 
 '''
 6.Write a program which will find all such numbers which are divisible by 7 but are not
 a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be
 printed in a comma-separated sequence on a single line.
 '''
nl=[]
for x in range(2000, 3200):
    if (x%7==0) and not (x%5==0):
        nl.append(str(x))
print (','.join(nl))
 
 
 
 
 '''
 7.Write a program which can 
 compute the factorial of a given numbers. Use recursion to find it. Hint: Suppose the 
 following input is supplied to the program:8 Then, the output should be:40320
 '''
n=int(input("Enter the number whose factorial to be calculated: "))
 
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
print(fact(n))
 
 '''
 8.Write a program that calculates and prints the value according to the given
 formula:Q = Square root of [(2 * C * D)/H]
 Following are the fixed values of C and H: C is 50. H is 30.D  is  the  variable 
 whose  values  should  be  input  to  your  program  in  a  comma-separated sequence. 
 Example:Let  us  assume  the  following  comma  separated  input  sequence  is  given 
 to  the program:100,150,180 The output of the program should be:18,22,24
 '''
 C=50
 H=30
 from math import sqrt
 D=int(input("Enter the input of D: "))
 ans=sqrt((2*C*D)/H)
 
 print(int(ans))
 
 '''
 9.Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
 The element value in the i-th row and j-th column of the array should be i*j.Note:
 i=0,1.., X-1; j=0,1,¡-Y-1.
 Example:Suppose the following inputs are given to the program:3,5
 Then, the output of the program should be:[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
 '''
row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]= row*col

print(multi_list)
 
 '''
 10.Write a program that accepts a comma separated sequence of words as input and 
 prints the words in a comma-separated sequence after sorting them alphabetically.
 Suppose the following input is supplied to the program:without,hello,bag,world
 Then, 
 the output should be:bag,hello,without,world
 '''
 List=list(map(str, input("Enter the strings: ").split(',')))
 
 List.sort()
 print(List)
 
 
 '''
 11.Write a program that accepts sequence of lines as input and prints the lines after
 making all characters in the sentence  capitalized. Suppose the following inputis 
 supplied to the program:Hello world Practice makes perfect
 Then, 
 the output should be:HELLO WORLDPRACTICE MAKES PERFECT
 '''
string=str(input("Enter the string: "))
print(string.upper())
 
 
 '''
 12.Write a program that accepts a sequence of whitespace separated words as input and 
  prints   the   words   after   removing   all   duplicate   words   and   sorting   
  them alphanumerically. 
  Suppose the following input is supplied to the program:
      hello world and practice makes perfect and hello world again
      Then,the output should be:again and hello makes perfect practice world
  '''

L=list(map(str, input("Enter the strings: ").split()))

setl=set(L)
ans=list(setl)
ans.sort()
print(ans)
  
  
  
  '''
  13.Write  a  program  which  accepts  a  sequence  of  comma  separated  4  digit  
  binary numbers  as  its  input  and  then  check  whether  they  are  divisible  by
  5  or  not.  The numbers that are divisible by 5 are to be printed in a comma separated 
  sequence.
 
  Example:0100,0011,1010,1001
  Then the output should be:1010
  '''
  
ilist=list(map(str, input("Enter the strings: ").split(',')))


ans=[]
for i in ilist:
    p=int(i,2)
    if p%5 ==0:
        ans.append(i)
        
print(ans)
  
  
  
  
  
  '''
  14.Write  a  program  that  accepts  a  sentence  and  calculate  the  number  of
  upper  case letters and lower case letters.Suppose the following input is supplied to
  the program:Hello world!Then, the output should be:UPPER CASE 1 LOWER CASE 9
  '''
string=str(input("Enter the string to calculate : "))
upper=0
lower=0
for i in string:
    if i.isupper():
        upper=upper+1
    if i.islower():
        lower=lower+1
print("Number of Upper Case char : ",upper)
print("Number of Lower Case char : ",lower)
  
  '''
  15.Give example of fsum and sum function of math library.
  '''
 
import math
 
print(math.fsum(range(1,10)))

a=[10,20,30,40,50] 

print(math.fsum(a))

print(sum(a))

print(sum(a,10))
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 