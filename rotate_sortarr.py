#This problem was asked by microsoft.
#Taking an array and rotated in clockwise by unknown amount.
#And prompting index of asked number if it there.

from array import array
arr=array('i',[int(i) for i in input("Enter elements for array by giving spaces:").strip().split()])
n=int(input("Enter no of rotations: "))
arr_rotate=arr[-n%len(arr):]+arr[:-n%len(arr)]
print('Before Rotation: ',arr)
print('After Rotation: ',arr_rotate)
ask=int(input("Enter number you want to find in rotated array: "))
if ask in arr_rotate:
    print("Found in rotated array and Index of your number is-->",arr_rotate.index(ask))
else:
    print("Not Found and Index is-->",-1)