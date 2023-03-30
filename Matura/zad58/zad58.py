import math

max_wart=[]

def dekoduj(a:str,b:int):
    odwrot = a
    minus = False
    if odwrot.startswith('-'):
        odwrot=odwrot[1:]
        minus = True
    odwrot = odwrot[::-1]
    wynik = int(0)
    for i in range(0,len(odwrot)):
        wynik += int(odwrot[i]) * math.pow(b,i)

    if minus: wynik*=-1
    return wynik



for i in range(1,4):
    with open("../dane/58/dane_systemy"+str(i)+".txt",mode="r") as file:
        j=0
        max=0
        for line in file:
            line = line.strip()
            print(line)

            czas=line.split(' ')[0]
            temp=line.split(' ')[1]
            pot = 2
            if i == 2: pot = 4
            if i == 3: pot = 8
            czas_dek = dekoduj(czas,pot)
            temp_dek = dekoduj(temp,pot)
            print(czas_dek,temp_dek,pot)
            if temp_dek > max: max = temp_dek

            j+=1

        max_wart.append(max)

print(max_wart)

