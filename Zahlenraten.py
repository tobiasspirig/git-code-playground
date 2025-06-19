import random
anzahl=0
zahl=False
geszahl=random.randint(1,1000)
while zahl==False:
    eing=(int(input("Zahl raten:")))
    if geszahl<eing:
        print("zu gross")
        anzahl=anzahl+1
    elif geszahl>eing:
        print("zu klein")
        anzahl=anzahl+1
    else:
        print("erraten!")
        anzahl=anzahl+1
        zahl=True
print('Sie haben die Zahl',geszahl,"in", anzahl, "Versuchen erraten.")
