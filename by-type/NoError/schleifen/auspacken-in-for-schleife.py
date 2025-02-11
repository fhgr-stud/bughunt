# Warum liefert die folgende Schleife nicht eine Liste
# mit dem Namen, Alter und der Telefonnummer der Personen
# im Telefonbuch.
#
# Wie können Sie das Beispiel korrigieren.

tel = [{"name": "ana", "age": 12, "phone": 222},
       {"name": "jim", "age": 22, "phone": 122},
       {"name": "joe", "age": 27, "phone": 522},
       {"name": "zoe", "age": 42, "phone": 728}]

for name, alter, phone in tel:
    zeile = [name, alter, phone]
    print(zeile)
