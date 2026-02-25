def eingabe_zahl(text):
    while True:                 # Schleife läuft unendlich break beendet die Schleife
        try:
            return float(input(text))       # float() = wandelt Text (z.B. 3.14) in eine Zahl um
        except ValueError:
            print("Bitte nur Zahlen eingeben!")

def eingabe_operator():
    while True: 
        op = input("Welche Operation möchtest du? (+, -, *, %, /) oder 'q' zum Beenden: ")
        if op in ["+", "-", "*", "/", "%", "q"]:                # Prüft, ob der Wert in der Liste enthalten ist 
            return op
        else:
            print("Ungültiger Operator! Bitte +, -, *, %, / oder q eingeben.")

# def = definiert eine Funktion
# Alles, was eingerückt darunter steht, gehört zu dieser Funktion
def berechne(zahl1, zahl2, operator):
    if operator == "+":
        return zahl1 + zahl2        # return = gibt das Ergebnis der Funktion zurück
    elif operator == "-":           # Der Code außerhalb der Funktion kann dieses Ergebnis dann benutzen
        return zahl1 - zahl2
    elif operator == "%":
        return zahl1 * zahl2 / 100
    elif operator == "*":
        return zahl1 * zahl2
    elif operator == "/":
        if zahl2 != 0:
            return zahl1 / zahl2
        else:
            return "Fehler: Division durch 0"
# if = wenn Bedingung erfüllt ist
# elif = sonst wenn eine andere Bedingung erfüllt ist
#else = sonst

#HauptProgramm 
name = input("Wie heißt du? ")                              # input() = fragt den Benutzer nach einer Eingabe 
print(f"Willkommen, {name}, zu deinem Taschenrechner!")     # Das Ergebnis ist immer ein Text (String)

while True:
    zahl1 = eingabe_zahl("Gib die erste Zahl ein: ")
    zahl2 = eingabe_zahl("Gib die zweite Zahl ein: ")
    operator = eingabe_operator()
    
    if operator == "q":
        print("Taschenrechner beendet. Auf Wiedersehen!")
        break
# break = verlässt die aktuelle Schleife sofort

    ergebnis = berechne(zahl1, zahl2, operator)
    print(f"{name}, dein Ergebnis ist: {ergebnis}\n")
