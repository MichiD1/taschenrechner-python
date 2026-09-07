def eingabe_zahl(text):
    while True:                 
        try:
            return float(input(text))       
        except ValueError:
            print("Bitte nur Zahlen eingeben!")

def eingabe_operator():
    while True: 
        op = input("Welche Operation möchtest du? (+, -, *, %, /) oder 'q' zum Beenden: ")
        if op in ["+", "-", "*", "/", "%", "q"]:                
            return op
        else:
            print("Ungültiger Operator! Bitte +, -, *, %, / oder q eingeben.")


def berechne(zahl1, zahl2, operator):
    if operator == "+":
        return zahl1 + zahl2        
    elif operator == "-":           
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



name = input("Wie heißt du? ")                               
print(f"Willkommen, {name}, zu deinem Taschenrechner!")     

while True:
    zahl1 = eingabe_zahl("Gib die erste Zahl ein: ")
    zahl2 = eingabe_zahl("Gib die zweite Zahl ein: ")
    operator = eingabe_operator()
    
    if operator == "q":
        print("Taschenrechner beendet. Auf Wiedersehen!")
        break


    ergebnis = berechne(zahl1, zahl2, operator)
    print(f"{name}, dein Ergebnis ist: {ergebnis}\n")

