# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 17:10:20 2021

@author: vikas.maurya
"""
'''
Case Study III
Domain –Telecomfocus –Optimization
Business challenge/requirement Life Tel Telecomis the latest entrant in the highly 
competitive Telecom market of Singapore.  
It issues SIM to the verified users.  Till now verification was manual through the 
photocopy of approved id card document. However,government has recently introduced
Social ID called Reference ID which is mapped to fingerprint of user.LifeTel should
now verify user against the fingerprint and Reference ID.
Key issues:
Build a system where
when user enters Reference ID it is encrypted, so that hackers cannot view the mapping
of Reference ID and finger print Considerations.
System should be secure.
Data volume-NA
Additional information-NA
Business benefits
Company will be able to quickly issue SIM to
user and expected gain in volume is approximately 10 times as the manual process of
verification is replaced with secure automated system

Approach to Solve
You have to use fundamentals of Python taught in module 1
1.Read the input from command line –Reference ID
2.Check for validity –it should be 12 digits and allows on number and alphabet.
3.Encrypt the Reference ID and print it for reference.
Enhancements for code You can try these
enhancements in code1.Allow some special characters in ReferenceID2.Give the option for decryption to user 

'''

refID=str(input("Enter the Reference ID : "))
if len(refID) !=12:
    print("Reference ID should be 12 characters")
small="abcdefghijklmnopqrstuvwxyz"
big="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="0123456789"
spe="$#@"

allowedChar=small+big+num
allowedChar

isval=True

for i in refID:
    if i not in allowedChar:
        isval=False
        break

print("Is Validated the Reference ID",isval)

if not isval:
    print("Reference ID should contain alphabet and number only")


LETTERS=small+big+num
def encrypt(message, key):
    encrypted = ''
    for chars in message:
        if chars in LETTERS:
            num = LETTERS.find(chars)
            num += key
            encrypted +=  LETTERS[num]

    return encrypted

def decrypt(message, key):
    decrypted = ''
    for chars in message:
        if chars in LETTERS:
            num = LETTERS.find(chars)
            num -= key
            decrypted +=  LETTERS[num]

    return decrypted

if isval:
    de=encrypt(refID,2)
    
print(de)

print("If want to decrypt the string then use key use to encrypt")
print(decrypt(de,2))