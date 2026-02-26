import random   
def eingabe_zahl():
    while True:
        try:
            return int(input("Rate eine Zahl zwischen 1 und 10: "))
        except ValueError:  
            print("Bitte nur eine ganze Zahl eingeben!")
while True: 
    geheime_zahl = random.randint(1, 10) 
    versuche = 0    
    while True: 
        eingabe = eingabe_zahl()    
        versuche += 1   
        if eingabe == geheime_zahl: 
            print(f"Richtig! Du hast die Zahl in {versuche} Versuchen erraten.")
            break    
        elif eingabe < geheime_zahl:  
            print("Zu niedrig!")
        else:       
            print("Zu hoch!")
        if versuche >= 4:    
            print(f"Leider verloren! Die Zahl war {geheime_zahl}. ")
            break
    nochmal = input("Willst du nochmal spielen? (j/n): ").lower()
    if nochmal != "j": # alles außer "j" = spiel beenden
        print("Danke fürs Spielen! Auf Wiedersehen!")
        break
    


