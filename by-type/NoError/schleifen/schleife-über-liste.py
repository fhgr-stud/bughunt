# Warum produziert die folgende Schleife keine Ausgabe?
# Wie müsste man diese korrigieren?

haystack = "hallo"
needle = "l"

for pos, needle in enumerate(haystack, 1):
    if pos == haystack:
        print(pos)
