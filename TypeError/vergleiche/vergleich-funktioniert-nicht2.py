"""
Erklären Sie warum der folgende Vergleich nicht funktioniert.
Lösen Sie im Anschluss das Problem.
"""

def alter_in_monaten(jahre):
    jahre = int(input("Alter in Jahren: "))
    return 12 * jahre

if alter_in_monaten < 216:
    print("Minderjährig")
else:
    print("Volljährig")
