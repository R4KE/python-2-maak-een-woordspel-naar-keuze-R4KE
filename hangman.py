import time
import math
import random
import os

#Gemaakt door Jurre

#Copyright reserved

#versie 0.1

woorden = ["installering", "kwadraat", "zeeslag", "pantservoertuig", "laptop", "wiskunde", "banaan", "drol", "computer", "muismat", "bureaublad", "kabouter", "wapenstilstand", "terrorist", "aanslag", "waterstof", "animatie"]


for x in range(0, 3):
    print("  ___    __    __    ___   ____  ____")
    print(" / __)  /__\  (  )  / __) (_  _)( ___)")
    print("( (_-. /(__)\  )(__( (_-..-_)(   )__)")
    print(" \___/(__)(__)(____)\___/\____) (____)")
    print("")
    time.sleep(0.5)
    os.system('cls')
    time.sleep(0.5)

print("")
print("Regels:")
print("")
time.sleep(1)
print(" • Het doel van het spel is om het juiste woord te raden.")
time.sleep(1)
print(" • Elke beurt moet je steeds een letter opgeven, totdat het woord volledig is.  ")
time.sleep(1)
print(" • Maar... na 15 keer raden, is het spel over. ")
time.sleep(1)
print(" • Als je het woord denkt te weten, type '?'. ")
time.sleep(3)
print("")
print("Klik op enter om het spel te starten.")

Start = input("")

if Start == "":
    print("")
    
while True:
    os.system('cls')
    print("")
    time.sleep(1)
    woord = random.choice(woorden)
    letters = len(woord)
    print(woord)
    #for letters in woord:
        #print(woord.replace(woord, "-"))
        #test = woord.replace(woord, "-")
        #print(test)
    streepjes = letters * "-"
    print(streepjes)
    reactie = input("Geef een letter : ")
    

    if "?" in reactie:
        print("")
        time.sleep(1)
        reactie = input("Raad het woord: ")
        if reactie == woord:
            print("")
            time.sleep(1)
            print("Je hebt het woord goed :)")
    if "a" or "b" or "c" or "d" or "e" or "f" or "g" or "h" or "i" or "j" or "k" or "l" or "m" or "n" or "o" or "p" or "q" or "r" or "s" or "t" or "u" or "v" or "w" or "x" or "y" or "z" in reactie:
        print("")
        time.sleep(1)
    else:
        print("")
        time.sleep(1)
        print("Helaas is dit teken ongeldig en word je vervolgd.")
    
