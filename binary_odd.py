'''code for prompting the numbers which contains odd_ones or odd_zeros(or both)
from diffrent combinations of binary format of given number...'''
num=[i for i in str(bin(int(input("Enter a number: "))))]
print("binary format: ",num[2:])
num=num[2:]
sub=[]
while len(num)>=1:
    s=''
    for i in num:
        s+=i
        sub.append(s)
    num=num[1:]
print("Substrings: ",sub)
odd_zeros=[i for i in sub if i.count('0')%2!=0]
odd_ones=[i for i in sub if i.count('1')%2!=0]
print("Odd Zeros: ",odd_zeros)
print("Odd Ones: ",odd_ones)
