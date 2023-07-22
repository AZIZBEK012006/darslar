from os import system
system("cls")

dct = dict()

for i in range(10):
    [key,value] = input("qiymat kiriting: ").split()
    dct[key] = int(value)

lst = list(dct.items())
lst.sort(key=lambda tp: tp[1],reverse=True)

print(lst[:5])










