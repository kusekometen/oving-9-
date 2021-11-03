#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 22:24:35 2021

@author: naderkoleib
"""

class spørsmål:
    def __init__(self, spørsmål, svar, alternativer=[]):
        self.spørsmål = spørsmål
        self.svar = svar
        self.alternativer = alternativer
        
    def leggtilsvar(self, svar):
        self.alternativer.append(svar)
        
    def __str__(self):
        streng =  f"{self.spørsmål}"
        teller = 1
        for alternativ in self.alternativer:
            streng += f"\n{teller}) {alternativ} "
            teller += 1
        return streng
    
    def riktig_svar(self, svar):
        return self.svar == svar
    

def funksjon():
    svar = []
    sporsmaal = []
    alternativer = []
    with open("sporsmaalsfil.txt", "r", encoding="UTF8") as fila:
        for linje in fila:
            splitta_linje = linje.split(":")
            sporsmaal.append(splitta_linje[0])
            svar.append(int(splitta_linje[1]))
            alternativer.append(splitta_linje[2].strip("[]\n "))
        for i in range(len(alternativer)):
            alternativer[i] = alternativer[i].split(",")
                
    spm = []
    for index in range(len(svar)):
        spm.append(spørsmål(sporsmaal[index], svar[index], alternativer[index]))
    return spm

alleSporsmaal = funksjon()

spiller1_score = 0
spiller2_score = 0

for spm in alleSporsmaal:
    print(spm)
    spiller1 = input("alternativ for spiller1: ")
    spiller2 = input("alternativ for spiller2 ")
    if spm.riktig_svar(int(spiller1)):
        spiller1_score += 1
    if spm.riktig_svar(int(spiller2)):
        spiller2_score += 1

print(spiller1_score)
print(spiller2_score)
