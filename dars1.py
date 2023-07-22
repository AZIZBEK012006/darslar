"""
#   C 2 ishlanmagan




#   if 1
a = int(input("butun son kiriting: "))

if a > 0:
    print(a + 1)
else:
    print(a)

#   if 2
a = int(input("son kiriting: "))
if a > 0:
    print(a + 1)
else:
    print(a + 2)

#   if 3
a = int(input("son kiriting: "))

if a > 0:
    print(a + 1)
elif a < 0:
    print(a + 2)
elif a == 0:
    print(a = 10)

#   if 4

a = int(input("1 - sonni kiriting: "))
b = int(input("2 - sonni kiriting: "))
c = int(input("3 - sonni kiriting: "))
    
caunt = 0

if a > 0:
    caunt += 1
if b > 0:
    caunt += 1
if c > 0:
    caunt += 1
print(caunt)

#   if 5

a = int(input("1 - sonni kiriting: "))
b = int(input("2 - sonni kiriting: "))
c = int(input("3 - sonni kiriting: "))

sam = 0
sum = 0

if a > 0:
    sam += 1
if a < 0:
    sum += 1
    
if b > 0:
    sam += 1
if b < 0:
    sum += 1
if c > 0:
    sam += 1
if c < 0:
    sum += 1

print(sam, "ta musbat ")
print(sum, "ta manfiy ")

#   if 6
a = int(input("1 - sonni kiriting: "))
b = int(input("2 - sonni kiriting: "))

if a > b:
    print(a)
else:
    print(b)

#   if 7
a = int(input("1 - sonni kiriting: "))
b = int(input("2 - sonni kiriting: "))

if a > b:
    print(2)
else:
    print(1)

#   if 8
a = int(input("1 - sonni kiriting: "))
b = int(input("2 - sonni kiriting: "))

if a > b:
    print(a,b)
else:
    print(b,a)

#   if 9
a = float(input("1 - haqiqiy sonni kiriting: "))
b = float(input("2 - haqiqiy sonni kiriting: "))

if a > b:
    b = (b + a)
    print(a,b)
else:
    print(a,b)

#   if 10
a = int(input("a ga qiymat bering: "))
b = int(input("b ga qiymat bering: "))

if a == b:
    a = a + b
    b = a
    print(a,b)
else:
    a = 0
    b = 0
    print(a,b)

#   vazifa 1
n = 800
i = 1
for i in range(n + 1):
    print(i)

#   vazifa 2

for i in range(1000,0,-1):
    print(i)

#   vazifa 3

for i in range(400,500 + 1):
    print(i)

#   vazifa 4
for i in range(300,150-1,-1):
    print(i)

#   vazifa 5
for i in range(-400,250 + 1):
    print(i)

#   vazifa 6
for i in range(200,-500-1,-1):
    print(i)

#   vazifa 7

for i in range(1,140+1):
    if i % 2 == 0:
        print(i)

#   vazifa 8

for i in range(100,240):
    if i % 2 != 0:
        print(i)

#   vazifa 9

for i in range(40,180):
    if i % 7 == 0:
        print(i)

#   vazifa 10

for i in range(50,440):
    if i % 11 == 0:
        print(i)

#   vazifa 10

for i in range(90,210):
    if i % 25 == 0:
        print(i)

#   vazifa 11

for i in range(25,690):
    if i % 5 == 0 and i % 9 == 0:
        print(i)

#   vazifa 12

for i in range(1,4000):
    if i % 11 == 0 and i % 3 == 0 and i % 9 == 0:
        print(i)

#   vazifa 13

for i in range(20,420):
    if i % 5 == 0 and i % 10 != 0:
        print(i)

#   vazifa 14

n = int(input("son kiriting: "))

for i in range(n + 1):
    print(i * i)

#   vazif 15
#   ishlanmagan



#   G 53 ishlanmagan
n = 5

for i in range(1,n + 1):
    print("* " * i)
    




#   P 1 ishlanmagan



#   P 2
caunt = 0
a = int(input("5 xonali son kiriting: "))

for i in range(5):
    c = a % 10
    a //= 10

    caunt += c
print(caunt)

#   P 3
n = int(input("son kiriting: "))

for i in range(n):
    if i % 2 == 0:
        print(i)

#   P 4
#   ishlanmagan


#   P 5----------------------------------------------------------
n = 1000

for i in range(n):
    if n // i == 9:
        print(i)

#   P 6
n = 100

for i in range(n):
    if i == 3 or i % 10 == 3 or i // 10 == 3:
        print(i)


#   P 7 ishlanmagan-----------------------------------------------
son = 100
check = True
boluvchi = 2

for i in range(son):
    if not (son % boluvchi):
        check = False
        break
    boluvchi += 1

    if check:
        if str(i) == str(i)[::-1]:
            print(i)

#   P 8 ishlanmagan-------------------------------------------------------



#   P 9

a = 50000
for i in range(1,a+1):
    sum = 0
    sam = 0

    for j in range(1,i):
        if i % j == 0:
            sum += j
    for k in range(1,sum):
        if sum % k == 0:
            sam += k
    if i == sam:
        print(i,sum)

"""
