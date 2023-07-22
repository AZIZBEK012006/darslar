"""
#   1 misol
x = 34
print(type(x))

#    2 misol

x = int (input("1 Sonni kiriting: "))
y = int (input( "2 sonni kiriting: "))
print((x+y)/2)


#     3 misol
#ishlanmagan

b = input("son kiriting: ") 

print("pyton " * int(b))

#   4 misol

a = input("son kiriting: ")

print(str(a)[::-1])


#   5 misol
a = int(input("sekund kiriting: "))
b = a // 3600
c = a - b * 3600
d = c // 60
e = c - d *60

print("soat:",b)
print("daqiqa: ",d)
print("soniya: ",e)

#   6 misol

a = int(input("faylning baytini kiriting: "))
b = a // 1024
print(int(b))

#   7 misol
a = int(input("kesmaning uzunligini kiriting: "))
b = int(input("1 - uzunlikdan kichikroq son kiriting: "))

c = a//b
print (int(c),"marta joylashtirish mumkin!")

#   8 misol
a = int(input("uchxonali son kiriting: "))
b = a // 10
c = b // 10
d = b % 10
e = a % 10
print(c,'-',d,'-',e)

#   9 misol

a = int(input("uchburchakning a tomonini kiriting: "))
b = int(input("uchburchakning b tomonini kiriting: "))
c = int(input("uchburchakning c tomonini kiriting: "))

p = a + b + c
print(int(p))
      
#   10 misol

a = str(input("ismingizni kiriting: "))
print("salom " + a[0:])

#   11 misol
M = int(input("milodiy yil kiriting: "))
H = M - 622 + (M - 622) / 32
print(int(H))

#   12 misol

a = int(input("yil kiriting: "))

print(a // 100 + 1)


#   13 misol

soz = input("soz kiriting: ")
kotta_harf = soz[0].upper() + soz[1:-1]+soz[-1].upper()

print(kotta_harf)
#   14 misol

a = "Welcome to najot talim. najot talim awesome, isn't it?"
b = input("soz kiriting: ")

c = a.count(b)

print(c)
"""













