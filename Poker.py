print("*********")
print("P O K E R")
print("*********")
print("EINGABE IHRER KARTEN")
print("Geben Sie die höchste Karte ein: ")
print()
wert1 = int(input("1. Wert: "))
farbe1 = int(input("1. Farbe: "))
wert2 = int(input("2. Wert: "))
farbe2 = int(input("2. Farbe: "))
wert3 = int(input("3. Wert: "))
farbe3 = int(input("3. Farbe: "))
wert4 = int(input("4. Wert: "))
farbe4 = int(input("4. Farbe: "))
wert5 = int(input("5. Wert: "))
farbe5 = int(input("5. Farbe: "))
print()
print("Sie haben eingegeben: ")
print("Karte 1 (Wert|Farbe): ", wert1, farbe1)
print("Karte 2 (Wert|Farbe): ", wert2, farbe2)
print("Karte 3 (Wert|Farbe): ", wert3, farbe3)
print("Karte 4 (Wert|Farbe): ", wert4, farbe4)
print("Karte 5 (Wert|Farbe): ", wert5, farbe5)

if farbe1 == farbe2 == farbe3 == farbe4 == farbe5 and wert1 + wert2 + wert3 + wert4 +wert5 == 55:
    print("ROYAL FLUSH")
elif farbe1 == farbe2 == farbe3 == farbe4 == farbe5 and wert1 == wert2 + 1 == wert3 + 2 == wert4 + 3 == wert5 +4:
    print("FLUSH")
elif wert1 == wert2 == wert3 == wert4 or wert2 == wert3 == wert4 == wert5:
    print("FOUR OF A KIND")
elif wert1 == wert2 == wert3 and wert4 == wert5 or wert1 == wert2 and wert3 == wert4 == wert5:
    print("FULL HOUSE")
elif wert1 == wert2 + 1 == wert3 + 2 == wert4 + 3 == wert5 +4:
    print("STRAIGHT")
elif wert1 == wert2 == wert3 or wert4 == wert2 == wert3 or wert5 == wert4 == wert3:
    print("THREE OF A KIND")
elif wert1 == wert2 and wert3 == wert4 or wert1 == wert2 and wert4 == wert5 or wert2==wert3 and wert4==5:
    print ("TWO PAIRS")
elif wert1 == wert2 or wert2 == wert3 or wert4 == wert5 or wert3 == wert4:
    print("ONE PAIR")
else:
    print ("KEINE KARTENKOMBINATION ERKANNT")