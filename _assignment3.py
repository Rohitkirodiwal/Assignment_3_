def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":-1}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case : ", d["UPPER_CASE"])
    print ("No. of Lower case  : ", d["LOWER_CASE"])

string_test('The quick Brown Fox')