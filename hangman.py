import time
import math
import random
import os

#Gemaakt door Jurre

#Copyright reserved

#versie 0.1

woorden = ["installering", "kwadraat", "zeeslag", "pantservoertuig", "laptop", "wiskunde", "banaan", "drol", "computer", "muismat", "bureaublad", "kabouter", "wapenstilstand", "terrorist", "aanslag", "waterstof", "animatie"]

#os.system('cls')
#for x in range(0, 3):
#    os.system('cls')
#    time.sleep(0.5)
#    print("  ___    __    __    ___   ____  ____")
#    print(" / __)  /__\  (  )  / __) (_  _)( ___)")
#    print("( (_-. /(__)\  )(__( (_-..-_)(   )__)")
#    print(" \___/(__)(__)(____)\___/\____) (____)")
#    print("")
#    time.sleep(0.4)
#time.sleep(1)
#print("")
#print("Regels:")
#print("")
#time.sleep(1)
#print(" • Het doel van het spel is om het juiste woord te raden.")
#time.sleep(1)
#print(" • Elke beurt moet je steeds een letter opgeven, totdat het woord volledig is.  ")
#time.sleep(1)
#print(" • Maar... na 15 keer raden, is het spel over. ")
#time.sleep(1)
#print(" • Als je het woord denkt te weten, type '?'. ")
#time.sleep(3)
#print("")
print("Klik op enter om het spel te starten.")

Start = input("")
if Start == "":
    print("")

while True:
    woord = random.choice(woorden)
    letters = len(woord)
    #for letters in woord:
        #print(woord.replace(woord, "-"))
        #test = woord.replace(woord, "-")
        #print(test)
    streepjes = []
    for i in range(letters):
        streepjes.append("_")

    fout = ""
    goed = ""
    
    while True:
        os.system('cls')
        print("  ___    __    __    ___   ____  ____")
        print(" / __)  /__\  (  )  / __) (_  _)( ___)")
        print("( (_-. /(__)\  )(__( (_-..-_)(   )__)")
        print(" \___/(__)(__)(____)\___/\____) (____)")
        print("")
        print("")
        time.sleep(1)
        print("")
        print(streepjes)
        print("")
        print("")
        print("Geef een letter.")
        print("")
        reactie = input(" : ")
        print("")
        lettercount = len(reactie)
        if lettercount == 1:
            if "?" in reactie:
                print("  ___    __    __    ___   ____  ____")
                print(" / __)  /__\  (  )  / __) (_  _)( ___)")
                print("( (_-. /(__)\  )(__( (_-..-_)(   )__)")
                print(" \___/(__)(__)(____)\___/\____) (____)")
                print("")
                print("")
                for i in range(letters):
                    print(streepjes[i], end=" ")
                print("")
                print("Raad het woord.")
                print("")
                reactie = input(" : ")
                if reactie == woord:
                    print("")
                    time.sleep(1)
                    print("Je hebt het woord goed :)")
                    time.sleep(2)
                    os.system('cls')
                    break
                else:
                    print("")
                    time.sleep(1)
                    print("Helaas... je hebt het woord fout.")
    
            elif reactie.isalpha():
                if not reactie in fout and not reactie in goed:
                    if (reactie) in woord:
                        for i in range(letters):
                            if reactie == woord[i]:
                                streepjes[i] = reactie
                        print("")
                        print("Goed!")
                        goed = goed + reactie
                        goedteller = len(goed)
                        print("")
                        time.sleep(1)
                    else:
                        print("")
                        print("Fout!")
                        time.sleep(1)
                        fout = fout + reactie
                        print("")
                        print("De letters die je fout hebt geraden zijn: " + fout)
                        foutenteller = len(fout)
                        print("")
                        time.sleep(2)
                else:
                    print("")
                    print("Deze letter heb je al geraden")
                    time.sleep(1)
                    
            else:
                print("Gelieve een geldig teken in te voeren.")
                time.sleep(1)
        else:
            time.sleep(0.3)
            print("Gelieve 1 karakter in te vullen.")
            time.sleep(2)
    
