"""
Warum liefert der folgende Code einen SyntaxError?
"""

betrag = int(input("Bitte Betrag eingeben:"))

if betrag > 100:
    return "Der Betrag ist grösser als 100."
else:
    return "Der Betrag ist nicht grösser als 100."
