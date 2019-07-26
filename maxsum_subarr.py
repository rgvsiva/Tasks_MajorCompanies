#This was asked by 'AMAZON'
#Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
#for [34,-50,42,14,-5,86]-->sum=137([42,14,-5,86]),for [-5,-1,-8,-9]-->sum=0
#arr=[34,-50,42,14,-5,86]
#arr=[-5,-1,-8,-9]
from array import *
arr=array('i',[int(i) for i in input("Enter elements for array by giving spaces:").strip().split()])
print("Given array of elements: ",arr)
maxsum=0
while len(arr)>=1:
    sum=0
    for i in arr:
        sum+=i
        if sum>maxsum:
            maxsum=sum
    arr=arr[1:]
if maxsum>0:
    print("Maximum sum of any contagiuous subarray of given array: ",maxsum)
else:
    print("Maximum sum: ",maxsum)