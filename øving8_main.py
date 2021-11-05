# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 09:27:32 2021

@author: Erlend Tøssebro
"""


teller = 0
ordliste = dict()
with open("oving_1_rein_tekst.txt", "r", encoding="UTF8") as fila:
    for i, linje in enumerate(fila):
        ordene = linje.split()
        for ordet in ordene:
            ordet = ordet.lower()
            if ordet in ordliste:
                pass
            else:
                ordliste[ordet] = i 
    for ordet in ordliste:
        print(f"Ordet {ordet} i linje {ordliste[ordet]}")



class spørsmål:
    def __init__(self, spørsmål, svar,alternativer=[]):
        self.spørsmål = spørsmål
        self.svar = svar
        self.svarAlternativ = alternativer
    def leggtilsvar(self, svar):
        self.svarAlternativ.append(svar)
    def __str__(self):
        streng =  f"{self.spørsmål}"
        teller = 1
        for alternativ in self.svarAlternativ:
            streng += f"\n{teller}) {alternativ} "
            teller += 1
             
            
        return streng
    def riktig_svar(self, svar):
        return self.svar == svar
    

    

test = ["1","2","3","4"]


spørsmålet_1 = spørsmål("Hva er 2+2?", 3+1,test)
spørsmålet_2 = spørsmål("20+2",1,["22", "23", "24"])
spørsmålet_3 = spørsmål("Hva er 5 ganger 5?", 2 , ["15", "25" , "35", "55"])


print(spørsmålet_1)
svar = input("Skriv inn svar alternativ nummer: ")
print(spørsmålet_1.riktig_svar(int(svar)))

if spørsmålet_1.riktig_svar(int(svar)):
    print("Riktig Svar")
else:
    print("Feil svar")


print(spørsmålet_2)
svar = input("Skriv inn svar alternativ nummer: ")
print(spørsmålet_2.riktig_svar(int(svar)))

if spørsmålet_2.riktig_svar(int(svar)):
    print("Riktig Svar")
else:
    print("Feil svar")

print(spørsmålet_3)
svar = input("Skriv inn svar alternativ nummer: ")
print(spørsmålet_3.riktig_svar(int(svar)))

if spørsmålet_3.riktig_svar(int(svar)):
    print("Riktig Svar")
else:
    print("Feil svar")


