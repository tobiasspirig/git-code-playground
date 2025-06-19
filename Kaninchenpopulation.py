#import matplotlib.pyplot as plt
kap=50
vermr=0.5
laenge=30
t=[0 for x in range (30)]
anzk=[2.0 for x in range (30)]

for i in range (1, laenge):
    t[i]=t[i-1]+1
    anzk[i]=anzk[i-1]+vermr*anzk[i-1]*((kap-anzk[i-1])/kap)
for i in range (1, laenge):
    print("Anzahl Kaninchen:", anzk[i-1], "Zeit:", t[i-1])
# plt.plot(anzk)
# plt.title("Kaninchenpopulation pro Zeit")
# plt.ylabel("Kaninchenpopulation")
# plt.xlabel("Zeit")
# plt.show()
