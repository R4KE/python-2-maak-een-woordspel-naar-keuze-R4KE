import time
import math
import random

#copyright gereserveerd

woorden = ["installering", "kwadraat", "zeeslag", "pantservoertuig", "laptop", "wiskunde", "banaan", "drol", "computer", "muismat", "bureaublad", "kabouter", "wapenstilstand", "terrorist", "aanslag", "waterstof", "animatie"]

while True:
    time.sleep(1)
    woord = random.choice(woorden)
    letters = len(woord)
    print(letters)
    print(woord)
    streepjes = letters * "-"
    print(streepjes)
    #reactie = input("Geef een letter : ")
