#given an array of integers,write a function to determine whether array could become non-decreasing by modifying at most one element.
#Ex: for [10,5,7]-->True(by changing 10), for [10,5,2]-->False
from array import *
#element=[int(i) for i in input("Enter elements for array by giving spaces:").strip().split()]
arr=array('i',[int(i) for i in input("Enter elements for array by giving spaces:").strip().split()])
print(arr)
pos=0
for i in range(len(arr)//2):
    if arr[i]>arr[i+1]:
        pos=i
        break
    elif arr[-i-2]>arr[-i-1]:
        pos=-i-2
        break
arr.remove(arr[pos])
if arr==sorted(arr):
    print("--It's a non-decreasing array after changing at most one element at index--",pos)
else:
    print("--It's not a non-decreasing array even though we change at most one element--")

