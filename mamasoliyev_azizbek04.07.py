import os
from math import*
os.system(("cls"))

#   R 1---------------------------------------------

# lst = [1,2,3,4,5,6,7,8]
# print(list(map(lambda son: float(son),lst)))
#   R 3---------------------------------------------
# lst = [("karimov sardor","12.02.2002",4000000),("mamasoliyev azizbek","04.01.2006",6000000)]
# lst1 = list(map(lambda a : a[0],lst))
# lst2 = list(map(lambda a : a[1],lst))
# lst3 = list(map(lambda a : a[2],lst))
# print(lst1)
# print(lst2)
# print(lst3)

#   R 4---------------------------------------------
# def otqaz(lst1: list,lst2:list):
#     for i in lst1:
#         if i in lst2:
#             lst1.remove(i)
#     return lst1
# lst1 = [1,2,3,4,5,6,7,8,9,10]
# lst2 = [2,4,6,8]

# print(otqaz(lst1,lst2))
#   R 5----------------------------------------------
# func = ["instagram","facebook","telegram","tik-tok","radigram"]
# search = "gram"
# print(list(filter(lambda a: search in a, func)))

#  amaliyot 2 masala

# lst = [3.2, -1.5, 2.6, -4.5, 6.8, 5.8, -9.2, 2.4]
# print(list(map(lambda a : ceil(a) if a > 0 else a, lst)))

#   3 masala
# lst = [ -4.5, 6.8, 5.8, -9.2, 2.4, 4.8]
# print(map(lambda a : floor(a) if a > 0 else a, lst))

#   4 masala
# lst = list(map(lambda a : 0 - int(a) if int(a) > 0 else int(a)*2, input().split()))
# print(lst)

















