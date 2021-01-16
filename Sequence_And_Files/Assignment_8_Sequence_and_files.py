# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 15:30:23 2020

@author: vikas.maurya
"""

'''
1.Write a program which will find factors of given number 
and find whether the factor is even or odd.
Hint: Use Loop with if-else statements
'''


fact=[]
def factors(num):
    for i in range(1,num+1):
        if(num%i == 0):
            fact.append(i)

def odd_Even():
    for i in fact:
        if i%2 == 0:
            print(i,"is","Even")
        else:
            print(i,"is","Odd")
fact.clear()
factors(10)
odd_Even()


'''
2.Write a code which accepts a sequence of words as input and
prints the words in a sequence after sorting them alphabetically.
Hint: In case of input data being supplied to the question,
it should be assumed to be a console input.
'''


n=int(input("Enter number of element : "))
seq_of_words=list(map(str,input("Enter the strings : ").strip().split()))[:n]

#sorted(seq_of_words)

seq_of_words.sort()

print(seq_of_words)


'''
3.Write a program, which will find all the numbers between 1000 and 3000 
(both included) such that each digit of a number is an even number.
The numbers obtained should be printed in a comma separated sequence 
on a single line.

Hint: In case of input data being supplied to the question,
it should be assumed to be a console input.
Divide each digit with 2 and verify
is it even or not.
'''


def finddig(l,r):
    ans=[]
    for num in range(l,r+1):
        flag=0
        temp=num
        while(num>0):
            rem=num%10
            if(rem%2 == 0):
                flag=1
            else:
                flag=0
                break
            num=num//10
        if flag==1:
            #print(temp),
            ans.append(temp)
            flag=0
    return ans
    
l,r=map(int,input("Enter 2 numbers : ").strip().split())
print(l,r)  

digitNum=finddig(l,r)

print(digitNum)
    

'''
4.Write a program that accepts a sentence and calculate the number
of letters and digits.

Suppose if the entered string is: Python0325
Then the output will be:LETTERS: 6
DIGITS:4
Hint: Use built-in functions of string.
'''

sentence=str(input("Enter the Sentence : "))

l=len(sentence)
count=0
for c in sentence:
    if c.isdigit():
        count=count+1
print("LETTER : ",l-count)
print("DIGITS : ",count)


'''
5.Design a code which will find the given number is Palindrome number or not.
Hint: Use built-in functions of string.
'''

num=int(input("Enter the Number : "))

nums=str(num)
nump=nums[::-1]
if(nums==nump):
    print("Palindrome")
else:
    print("Not Palindrome")

























