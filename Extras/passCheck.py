# -*- coding: utf-8 -*-
"""
Dhruv Jain
XI-D
"""

p = input("Enter password: ")
dig=sc=low=up=0
for i in range(len(p)):
    if len(p) >= 8:
        if p[i].isdigit():
            dig += 1
        if p[i].isalnum() == False:
            sc += 1
        if p[i].islower():
            low += 1
        if p[i].isupper():
            up += 1
if len(p) >= 8 and dig>=3 and sc>=2 and low>=2 and up>=1:
    print("Valid")
else:
    print("Invalid")