#This problem was asked by microsoft
#A number is condidered perfect if its digits sum up to exactly 10.
#Given positive integer n, return the n-th perfect number
#Given 1, you should return 19. Given 2 ,you should return 28.
from functools import reduce
def perfect():
    number=int(input("Which perfect number you want: "))
    num=19
    list_perfect = []
    while len(list_perfect)<number:
        if (reduce(lambda x, y: x + y, [int(f) for f in str(num)]))==10:
            list_perfect.append(num)
        num+=1
    print(list_perfect[-1])
perfect()

