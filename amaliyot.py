from os import system
import time
import random

class Pult():
    def __init__(self,tv_holati="Off",tv_ovoz=0,kanal_listi=["BBC","MY5","Zo'rTv","MTV","UZB"],kanal="BBC"):
        print("Pult kiritilmoqda........")
        self.tv_holati = tv_holati
        self.tv_ovoz = tv_ovoz
        self.kanal_list = kanal_listi
        self.kanal = kanal
    def __str__(self):
        return f"""TV Holati: {self.tv_holati}
ovozi: {self.tv_ovoz}
kanal Listi: {self.kanal_list}
hozirgi kanal: {self.kanal}"""
    def ovoz_ozgartirish(self):
        while True:
            soniya = 5
            belgi =input("  +  ||  -  ")
            if belgi == "+":
                if self.tv_ovoz < 5:
                    self.tv_ovoz += 1
                    print("ovoz - ")












