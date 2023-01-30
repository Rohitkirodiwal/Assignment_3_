def reverse_string(str):  
    str1 = ""              # empty string to store the reversed string  
    for i in str:  
        str1 = i + str1  
    return str1             # return the reverse string to the caller function  
     
str = "EDYODA1234"          # Given String       
print("The original string is: ",str)  
print("The reverse string is",reverse_string(str))