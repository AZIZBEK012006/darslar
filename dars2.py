"""
#   Q 1
lst = [1,2,3,"salom",True]

for i in range(len(lst)):
    lst[i] = type(lst[i])
print(lst)

#   Q 2
lst = [[2,15,4],[19,24,11],[7,9,5],[10,3,1]]
for i in range(len(lst)):
    print(**lst[i][0])

#   q 6

lst = [[5,3,7],[1,4,9],[2,8,6]]

caunt = 0

for i in range(len(lst)):
    j = i + 1
    for j in range(len(lst)):


#   Q 7

lst = [2,-1,5,-3,8,-4,6,7,9]
lst1 = [1,6,7,-3,-9,-4,-5]

for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i] == lst1[j]:
            print(lst[i])
            print(lst[j])

#   Q 8

lst = [10,20,[300,400,[5000,6000],500],30,40]

lst.insert[2][2][-1],7000

print(lst)

#   Q 9

lst = int(input("list kiriting: "))

#   Q 10 ishlanmagan

lst = [2,5,1,4,3,2,1,6,8,7,9] 

for i in range(len(lst)):
    for (j) in range(i + 1):
        if lst[i] != lst[j]:
            print(lst[i])

#   Q 11

lst = [11,33,50]

print(*lst)

#   Q 12
lst1 = [1,1,3,4,4,4,5,6,6,7]
lst2 = [0,1,2,3,4,4,5,7,8]

caunt = 0
sam = 0

for i in range(len(lst1)):
    caunt += lst1[i]
for j in range(len(lst2)):
    sam += lst2[j]

a = (caunt + sam) / 2
print(a)
"""


