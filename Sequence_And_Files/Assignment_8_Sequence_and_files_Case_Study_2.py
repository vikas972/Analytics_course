# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 09:08:46 2020
@author: vikas.maurya
"""

'''
Module 2 -Sequenceand File Operations
Case Study1.

'''

'''
What is the output of the following code?
nums =set([1,1,2,3,3,3,4,4])
print(len(nums))
Hint:Set consists unique element.
'''

'''
Output:

{1,2,3,4}
'''
nums =set([1,1,2,3,3,3,4,4])
print(len(nums))
print(nums)


'''
2.What will be the output?

d ={"john":40, "peter":45}
print(list(d.keys()))

Hint:d.keys() is the function which will show keys.
'''
'''
output:
    
['john', 'peter']
    
'''
d ={"john":40, "peter":45}
print(list(d.keys()))


'''
3.A website requires a user to input username and password to register.
Write a program to check the validity of password given by user.
Following are the criteria for checking password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from ["$#@"]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Hint: In case of input data being suppliedto the question, 
it should be assumed to be a console input.
'''
#small=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

small="abcdefghijklmnopqrstuvwxyz"
big="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="0123456789"
spe="$#@"

username=str(input("Enter the username : "))
password=str(input("Enter the Password : "))

sf=0
bf=0
numf=0
spef=0
for i in password:
    if i in small:
        sf=1
    if i in big:
        bf=1
    if i in num:
        numf=1
    if i in spe:
        spef=1
        
size=len(password)
if size<6:
    print("Password Length must be greater than 6 char")
elif size>12:
    print("Password Length must be smaller than 12 char")
elif not sf:
    print("It must contain small alphabet char also")
elif not bf:
    print("It must contain big alphabet char also")
    
elif not numf:
    print("It must contain numbers also")
elif not spef:
    print("It must contain special char also")
else:
    print("Password successfully set")

    



'''
4.Write a for loop that prints all elements of a list and their position in the list.
a = [4,7,3,2,5,9] 
Hint: Use Loop to iterate through list elements.
'''
a=[4,7,3,2,5,9]
for i in range(len(a)):
    print("Position of array element: ",i," ","The element: ",a[i])

'''
5.Please   write   a   program   which accepts  a   string   from   console
and   print   the characters that have even indexes.
Example: If the following string is given as input to the 
program: H1e2l3l4o5w6o7r8l9d
Then, 
the output of the program should be:Helloworld
'''
string=str(input("Enter the string : "))
output=""
for i in range(len(string)):
    if i%2==0:
        output=output+string[i]

print(output)


'''
6.
Please write a program which accepts a string from console and print it
in reverse order.
Example: 
If the following string is given as input to 
the program: rise to vote sir
Then, the output of the program should be:
ris etov ot esir
'''
s=str(input("Enter the the string to reverse :"))
print(s[::-1])


'''
7.Please write a program which count and print the numbers
 of each character in a string input by console.
 Example: 
 If the following string is given as input to the program:
 abcdefgabc
 Then, the output of the 
 program should be:a,2 c,2 b,2 e,1 d,1 g,1 f,1
 '''
freq={}
 
sf=str(input("Enter the string to calculate freq : "))

for i in sf:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

for i in freq:
    print(i,",",freq[i])
 
 
 
 '''
 8.With   two   given   lists  
 [1,3,6,78,35,55]   and   [12,24,35,24,88,120,155],  
 write   a program to make a list whose elements are intersection
 of the above given lists.
'''
a=[1,3,6,78,35,55] 
b=[12,24,35,24,88,120,155]

ans=[]
for i in a:
    if i in b:
        ans.append(i)
print(ans)

#method 2:
    
seta=set(a)
setb=set(b)
print(seta & setb)

'''
9.By using list comprehension, please write a program to print the list
after removing the value 24 in [12,24,35,24,88,120,155].
'''
rem=[12,24,35,24,88,120,155]
remE=int(input("Enter the element to remove :"))

while remE in rem:
    rem.remove(remE)
print(rem)

'''
10.By using list comprehension, please write a program to print the list
after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
'''
remI=[12,24,35,70,88,120,155]

remI.pop(0)
remI.pop(4)
remI.pop(5)

'''
11.By using list comprehension, please write a program to print the list
after removing delete numbers which are divisible by 5 and 7 in
[12,24,35,70,88,120,155].
'''
listdel=[12,24,35,70,88,120,155]

tobeDel=[]
for i in listdel:
    if i%5 == 0 and i%7 ==0 :
        tobeDel.append(i)
for i in tobeDel:
    listdel.remove(i)
print(listdel)

'''
12.Write  a  program  to  compute  1/2+2/3+3/4+...+n/n+1  with  a  given 
n  input  by console (n>0).
Example:If the following n is given as input to the program:5
Then, the output of the program should be:3.55
'''

n=int(input("Enter the n to calculate : "))
an=0
for i in range(1,n+1):
    an=an+(i/(i+1))
print("computed value : ",round(an,2))




