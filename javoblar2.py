from os import system
system("cls")

#   2 variant 1 savol

# dct = dict()

# for i in range(10):
#     [key, value] = input("gap kiriting: ").split()
#     dct[key] = int(value)

# lst = list(dct.items())
# lst.sort(key=lambda tp: tp[1],reverse=True)

# print(lst[:5])

#   2 misol

# st = input("gap kiriting: ").split()
# st[0] = st[0][::-1]
# st[-1] = st[-1][::-1]
# print(st)

#   3 misol

# a = int(input("son kiriting: "))
# st = ""
# if not a % 2 == 0:
#     for i in range(a + 1):
#         for j in range(1,i + 1):
#             print(j, end="")
#             if j != i:
#                 print("+",end="")
#             else:      
#                 print("=",end=f"{sum(list(range(1,j+1)))}\n")

#   4 misol
from math import *

def func(son:int) -> int:
    son1 = ""
    for j in str(son):
        son1 += j
    for i in range(2,int((sqrt(int(son1)))+1)):
        if int(son1) % i:
            return 
        return son1

a = list(map(int,input("uchxonali son kiriting: ").split()))
print(list(filter(func,a)))














