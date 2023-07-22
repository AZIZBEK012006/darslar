"""
#   K 1
lst = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

count = 0

for i in range(len(lst)):
    print(lst[i])
    count += sum(lst[i])
print(count)
#   Q 12

lst = [1,'abcd',3,1.2,4,'xyz',5,'pqr',7,-5,-12.22]

sum = 0

for i in range(len(lst)):
    if type(lst[i]) == int:
        sum += 1
print(sum)

#   Q 13
lst = [1,'abcd',3,1.2,4,'xyz',5,'pqr',7,-5,-12.22]

max = lst[0]

for i in range(len(lst)):
    if type(lst[i]) == int:
        if max < lst[i]:
            max = lst[i]
print(max)

#   Q 14
lst,natija = [9,9,9,9],0
for i in lst:
    natija = natija * (10 ** len(str(i))) + i
natija = natija + 1
natija = (" ".join(str(natija))).split()
print(f"{natija}")

#   Q 15
lst = list(map(int,input("son kiriting: ").split()))
map = 0
mat = 0
for i in lst:
    if i > map:
        map = i
        mat += 1
if mat == len(lst):
    print("tartib bilan joylashgan")
else:
    print("tartibsiz joylashgan")

#   Q 16
lst = [(),(),(""),('a','b'),('a','b','c'),('d')]
lst = [i for i in lst if i]
print(lst)
"""





