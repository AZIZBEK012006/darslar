from os import system
system("cls")

# #   S 1----------------------------------

# fayl = open("people_count.txt","r")

# odamlar = fayl.read().split("\n")

# for i in range(len(odamlar)):
#     odamlar[i] = odamlar[i].split(",")
#     if odamlar[i][2] == "Male":
#         print(odamlar[i])
# fayl.close()

#  S 2------------------------------------- 

# fayl = open("language.txt","r",encoding="utf-8")

# til = fayl.read().split("\n")

# for i in range(len(til)):
#     til[i] = til[i].split(",")
#     til[i][1] = int(til[i][1])
#     if til[i][1] > 1000000:
#         print(til[i])
# fayl.close()

#   S 3[1]------------------------------------

# fayl = open("product_material.txt","r",encoding="utf-8")
# product = fayl.read().split("\n")
# for i in range(len(product)):
#     product[i] = product[i].split(",")
#     if product[i][3] >= "$1000":
#         print(product[i][1])
#         print(product[i][2])

# fayl.close()

# # #   S 3[2]--------------------------------------
# fayl = open("product_material.txt","r",encoding="utf-8")
# material = fayl.read().split("\n")

# for i in range(len(material)):
#     material[i] = material[i].split(",")
#     if material[i][-1] == "true":
#         print(material[i][3])

#   S 3[3]--------------------------------------

# fayl = open("product_material.txt","r",encoding="utf-8")
# material = fayl.read().split("\n")

# for i in range(len(material)):
#     material[i] = material[i].split(",")
#     a = (material[i][3])
#     a = a[1:]
#     a = float(a)
#     if material[i][-1] == "false" and material[i][a] < (100.00):
#         print(material[i])

#   S 4[1]-------------------------------------

# fayl = open("cinema.txt","r",encoding=("utf-8"))
# kino = fayl.read().split("\n")
# soat = int(input("soatni kiriting: "))

# for i in range(len(kino)):
#     kino[i] = kino[i].split("\n")
#     if kino[i][-1] == soat:
#         print(kino[i])




































