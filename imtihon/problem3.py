from os import system
system("cls")

a = int(input("son kiriting: "))
st = ""

if not a % 2 == 0:
    for i in range(a + 1):
        for j in range(1, i + 1):
            print(j, end="")
            if j != i:
                print("+",end="")
            else:      
                print("=",end=f"{sum(list(range(1,j+1)))}\n")
else:
    for i in range(a + 1):
        for j in range(1, i + 1):
            print(j,end="")
            if j != i:
                print("+",end="")
            else:
                print("=",end=f"{sum(list(range(1,j+1)))}\n")





