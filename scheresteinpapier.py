import random as rd
runden =int(input("Wie viele Runden?"))
spieler1=[0 for c in range(0,runden)]
spieler2=[0 for j in range(0,runden)]

punkte1=[0 for k in range(0, runden)]
punkte2=[0 for l in range(0, runden)]

figuren=("Schere", "Stein", "Papier")

def ausgabe (x,y):
    for i in range (0,runden):
        x[i]=rd.choice(figuren)
        y[i]=rd.choice(figuren)
    print("Spieler1:",x, "Spieler2", y)
def auswerten():
    for i in range(0, runden):
        if spieler1[i]==spieler2[i]:
            punkte1[i]=0
            punkte2[i]=0
        elif spieler1[i] == "Schere" and spieler2[i] == "Papier":
            punkte1[i]=1
            punkte2[i]=0
        elif spieler1[i]== "Schere" and spieler2[i]== "Stein":
            punkte1[i]=0
            punkte2[i]=1
        elif spieler1[i]== "Stein" and spieler2[i]== "Papier":
            punkte1[i]=0
            punkte2[i]=1
        elif spieler1[i]=="Stein" and spieler2[i]== "Schere":
            punkte1[i]=1
            punkte2[i]=0
        elif spieler1[i]== "Papier" and spieler2[i]== "Schere":
            punkte1[i]=0
            punkte2[i]=1
        else:
            punkte1[i]=1
            punkte2[i]=0
        print("Spieler1:", punkte1, "Spieler2:", punkte2)
def gewinner():
    summe1=sum(punkte1)
    summe2=sum(punkte2)
    if summe1>summe2:
        print("Spieler 1 gewinnt mit", summe1, "zu", summe2)
    elif summe2>summe1:
        print("Spieler 2 gewinnt mit", summe2, "zu", summe1)
    else:
        print("Unentschieden!")
ausgabe(spieler1,spieler2)
auswerten()
gewinner()

