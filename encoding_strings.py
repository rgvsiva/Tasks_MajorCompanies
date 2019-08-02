#Run length encoding is a fast and simple method of encoding strings.
#The basic idea is to represent repeated successive characters as a single count and character.
#EX: for 'AAAABBBCCDAA'-->'4A3B2C1D2A'
st=input("Enter a string to encode: ")
from functools import reduce
def count_logic(st):
    count=1
    if len(st)==st.count(st[0]):
        return str(st.count(st[0]))+st[0]
    elif len(st)>1:
        for i in range(len(st)-1):
            if st[i]==st[i+1]:
                count+=1
            else:
                return str(count)+st[i]
    else:
        return str(count)+st[0]
encoded=count_logic(st)
while True:
    length=reduce(lambda x,y:x+y,[int(val) for val in encoded[::2]])
    if length<len(st):
        encoded+=count_logic(st[length:])
    elif length==len(st):
        break
print("Given String: ", st)
print("Encoded String: ",encoded)
#========================================
'''
s1=''
for i in s:
    if i not in s1:
        if s.count(i)>1:
            s1+=str(s.count(i))+i
        else:
            s1+=i
print(s,s1)
'''