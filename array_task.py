'''This was asked by Uber...
Given an array of integers, return  a new array such that
each element at index i of the new array is the product of
all the numbers in the original array except the one at i.'''
#[1,2,3,4,5]-->[120,60,40,30,24]
from array import array
from functools import reduce
arr=array('i',[int(i) for i in input("Enter elements for array by giving spaces:").strip().split()])

#first method
res_arr=[]
for i in range(len(arr)):
    res_arr+=[reduce(lambda x, y: x * y, arr[:i]+arr[i+1:])]
print("Result array: ",res_arr)

#another method in single line....
print("Result array: ",[reduce(lambda x, y: x * y, sub) for sub in [arr[:i]+arr[i+1:] for i in range(len(arr))]])
