# Write a Python program to reverse a string.

# ﻿Sample String : "1234abcd"

# Expected Output : "dcba4321"

def reverce(string):
    string=string[::-1]
    return string
string = input("Enter your string : ")
print("sample string : ", string)
print("The output : ",reverce(string))