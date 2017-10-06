import time
import math
import random

#copyright gereserveerd

woorden = ["installering", "kwadraat", "zeeslag", "pantservoertuig", "laptop", "wiskunde", "banaan", "drol", "computer", "muismat", "bureaublad", "kabouter", "wapenstilstand", "terrorist", "aanslag", "waterstof", "animatie"]

print("welkom bij...")
print("  ___    __    __    ___   ____  ____")
print(" / __)  /__\  (  )  / __) (_  _)( ___)")
print("( (_-. /(__)\  )(__( (_-..-_)(   )__)")
print(" \___/(__)(__)(____)\___/\____) (____)")
print("")
    
while True:
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
    
