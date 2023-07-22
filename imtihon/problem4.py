from os import system
from math import *
system("cls")

def func(son:int) -> int:
    son1 = ""
    for j in str(son):
        son1 += j
    for i in range(2,int((sqrt(int(son1)))+1)):
        if int(son1) % i:
            print("tub son bo'lmaydi")
            break
        else:
            print("tub son bo'ladi")
            break

a = list(map(int,input("uchxonali son kiriting: ").split()))
print(list(filter(func,a)))







