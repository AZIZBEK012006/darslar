from os import system
system("cls")

st = input("gap kiriting: ").split()

st[0] = st[0][::-1]
st[-1] = st[-1][::-1]
print(st)







