dane = []
with open("dane.txt","r") as file:
    for line in file.readlines():
        line = line.strip()
        print(line)
        things = line.split(" ")
        dane.append(things)

# print(dane[1][1])
mandaty = []
for i in range(20):
    mandaty.append([0,0,0,0,0])
for i in range(0,20):
    # print(dane[i][1])
    for j in range(0,20):
        wspolczynniki = [0,0,0,0,0]
        for k in range(5):
            wspolczynniki[k] = int(dane[i][k+1]) / (mandaty[i][k]*2+1)
        for k in range(5):
            if wspolczynniki[k]>= max(wspolczynniki):
                mandaty[i][k]+=1
    print(mandaty[i])
    
    # for x in range(5):
        # print(mandaty[i][x])

maxmandat=[]
jegomandaty=[[],[],[],[],[]]
for i in range(5):
    for j in range(20):
        jegomandaty[i].append(mandaty[j][i])
    maxmandat.append(max(jegomandaty[i]))

print("max mandaty")
print(maxmandat)

wszytkiemandaty = []
for i in range(5):
    wszytkiemandaty.append(sum(jegomandaty[i]))
        

print("wszytkie mandaty")
print(wszytkiemandaty)

mandaty = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]



wszytkieglosy=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] 
for j in range(4):
    for i in range(5):
        for k in range(5):
            wszytkieglosy[j][k]+=int(dane[j*5+i][k+1])

for i in range(4):
    print(wszytkieglosy[i])

for i in range(0,4):
    # print(dane[i][1])
    for j in range(0,100):
        wspolczynniki = [0,0,0,0,0]
        for k in range(5):
            wspolczynniki[k] = float(wszytkieglosy[i][k]) / (mandaty[i][k]*2+1)
        for k in range(5):
            if wspolczynniki[k]>= max(wspolczynniki):
                mandaty[i][k]+=1
        # print(wspolczynniki)
        # print(mandaty[i])
    print(mandaty[i])

maxglosow = 100000
def mandaty(m,g1):
    g2 =100000-g1
    mandatym = [0,0]
    for i in range(m*2):
        wspolczynniki = [0,0]
        wspolczynniki[0]=g1/(mandatym[0]*2+1)
        wspolczynniki[1]=g2/(mandatym[1]*2+1)
        if wspolczynniki[0]>wspolczynniki[1]:
            mandatym[0]+=1
        else:
            mandatym[1]+=1
    # print(g)
    return mandatym[0]==m

m=10
g=0
while mandaty(m,g)==False:
    g+=1

print(g)
m=20
g=0
while True:
    g+=1
    if mandaty(m,g): break
print(g)
m=50
g=0
while True:
    g+=1
    if mandaty(m,g): break
print(g)
