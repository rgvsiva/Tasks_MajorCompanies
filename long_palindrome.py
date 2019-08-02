#This was asked by AMAZON.
#Given a string, find the longest palindromic contiguous substring.
#if there are more than one, prompt the first one.
#EX: for 'aabcdcb'-->'bcdcb'
main_St=input("Enter the main string: ")
st=main_St
palindrome=[st[0]]
while len(st)>1:
    sub=''
    for ch in st:
        sub+=ch
        if (sub==sub[::-1]) and (sub not in palindrome) and (len(sub)>len(palindrome[-1])):
            palindrome=[sub]
    st=st[1:]
print ('Longest palindromic substring: "',palindrome[0],'" at index-',main_St.index(palindrome[0]))

