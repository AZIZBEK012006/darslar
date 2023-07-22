from os import system
system("cls")
import random

# random.randint(-100,100)

# class MyList(list):
#     def rand(self,n,RAND_MIN=(-100),RAND_MAX=100):
#         lst=[]
#         for i in range(n):
#             k=random.randint(RAND_MIN,RAND_MAX)
#             lst.append(k)
#         return lst

# n = int(input("son mkiriting: "))

# lst = MyList()
# print(lst.rand(n,-10))


#   2 masala ----------------------------------------

class Soldat:
    def __init__(self,yoshi: int,boyi: float,vazni: int,jinsi: str):
        self.yoshi=yoshi
        self.boyi=boyi
        self.vazni=vazni
        self.jinsi=jinsi


  


class Armiya(Soldat):
    def __init__(self, yoshi: int, boyi: float, vazni: int,jinsi: str):
        super().__init__(yoshi, boyi, vazni,jinsi)

    def yosh(self):
        if self.yoshi < 18 and self.jinsi.lower() == "ayol":
            print("armiyaga olinmaydi")
            return False
        else:
            True
            
    def yunalish(self):
        if self.yosh():
            if self.yoshi >= 18 and self.boyi <150 and self.vazni < 75 and self.jinsi.lower() == "erkak":
                print("piyoda qushinlariga yunaltirildi")
            else:
                print("tank qushinlariga yunaltirildi")

askar=Armiya(int(input("yoshini kirting: ")))
float(input("boyini kiritng: ")),int(input("vaznini kiritng: ")),input("jinsini kiriting: ")
askar.yunalish()
askar.yosh()






















