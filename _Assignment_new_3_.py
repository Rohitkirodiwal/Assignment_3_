# Write a Python function that accepts a string and calculate the number of 
# upper case letters and lower case letters.

# ﻿Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

string = "The Quick Brown Fox"
Uppercase = 0
Lowercase = 0
for i in string:
    if i.isupper():
        Uppercase += 1
    elif i.islower():
        Lowercase += 1
print("Upper count : ",Uppercase)
print("Lower count : ",Lowercase)