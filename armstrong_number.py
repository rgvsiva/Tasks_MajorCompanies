no=int(input("Enter number upto which you need armstrong numbers: "))
print("Armstrong numbers: ",[i for i in range(no) if i==sum([int(num)**3 for num in str(i)])])
#-------------------------
l=[]
for i in range(1000):
    num=[int(num)**3 for num in str(i)]
    if i==sum(num):
        l.append(i)
print("Armstrong numbers: ",l)

