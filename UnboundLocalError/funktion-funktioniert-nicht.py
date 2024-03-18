"""
Warum funktioniert dieses Programm nicht?
"""

summe = 0

def berechne_summe(zahl1, zahl2):
    if summe > 5:
        print("Grösser 5")
    else:
        print("Kleiner gleich 5")

    summe = zahl1 + zahl2
    return summe

print(berechne_summe(200, 4))
