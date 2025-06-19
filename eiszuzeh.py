import random
i= 1
# while value < 10:
#     print("hello", value)
#     if value == 5:
#         break
#     value += 1

# while i <=10:
#     i +=1
#     if i == 5:
#         continue
#     print(i)
# else:
#     print("Value is now equal to" + str(i))
     
names = ["Dave", "Sara", "John"]

# for i in names:
#     print("Name:", i)

# for i in names:
#     if i == "Sara":
#         continue
#     else:
#         print(i)


# for x in range(2, 400, 20):
#     print(x)
# else:
#     print("Glad that's over")

# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# times = ["morning", "noon", "afternoon", "night"]

# for i in times:
#     for j in days:
#         print (j, i)
f = True
while f:
    print (f"Willkomme zum 1 zu 10 Spiel")

    q = True
    w = True
    i = 1
    a = 1
    add = "F"
    players = {}
    while q == True:
        if add != "N": 
            who = input (f"Gib din Name i!")
            num = input (f"Was isch dini Zahl vo 1 bis 10?")
            num_int = int(num)
            add = input (f"Wöttsch nomeh Spieler hinzuefüege? Druck igend e Taste für ja und N für nei!")
            q = True
            players[who] = num_int
        else:
            q = False

    for who, num_int in players.items():
        print(f"{who} het d Zahl {num_int} usgwählt")

    print("Luegemer was s Orakel usgwählt het")

    random_number = random.randint(1, 10)

    print("S Orakel het", random_number, "usgwählt")

    if random_number in players.values():
        for who, num_int in players.items():
            if num == random_number:
                print("Sorry,", {who}, "dich hets¨" )
    else:
        print("Glück gha!")

    again = "j"
    again = input ("Wöttsch nomol spiele?  Druck igend e Taste für ja und N für nei!")
    if again == "N":
        print("Bis zum nögschte Mol!")
        f = False

        
        



