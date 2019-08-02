#validating the passwords by given conditions...
#
print("** Password length must be inbetween 6 and 12...\n"
      "** password must be contain one capital,one small, one number and one special(!@#$%^~.&*)...")
#0---------------------------------------------
#pswd=['ABd1234@1', 'aF1#','2w3E*','2We3345']
pswd=input("Enter Password: ")
#method by using regular expressions
import re
if 6<=len(pswd)<=12:
    if not re.search('[A-Z]',pswd):
        print("Not valid")
    elif not re.search('[a-z]',pswd):
        print("Not valid")
    elif not re.search('[0-9]',pswd):
        print("Not valid")
    elif not re.search("[!@#$%^~.&*]",pswd):
        print("Not valid")
    elif re.search('\s',pswd):
        print("Not valid")
    else:
        print(pswd,' is valid password')
else:
    print("Not valid")

#------------------------------
if 6<=len(pswd)<=12:
    if not re.search('[A-Z]',pswd) \
        or not re.search('[a-z]',pswd) \
        or not re.search('[0-9]',pswd)\
        or not re.search("[!@#$%^~.&*]",pswd) \
        or re.search('\s',pswd):
        print("Not valid")
    else:
        print(pswd,' is valid password')
else:
    print("Not valid")
#----------------------------------------------------------------
def f(pswd):
    if 6 <= len(pswd) <= 12:
        spe=['~','!','@','#','$','%','^','&','*','.']
        l=[0,0,0,0]
        for ch in pswd:
            if ch in spe:
                l[0]+=1
            elif ch.isupper():
                l[1]+=1
            elif ch.islower():
                l[2]+=1
            elif ch.isdigit():
                l[3]+=1
            else:
                continue
        if all(l):
            print(pswd,' is valid password')
        else:
            print("Not valid")
    else:
        print("Not valid")
f(pswd)

