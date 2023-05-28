import random
import math

one = int(random.random()*100)+1
two = int(random.random()*100)+1

# one=68
# two=16

razem = one + two
liczby=[]
print(one,two,razem)

for i in range(0,one):
    liczby.append(1)


for i in range(0,two):
    liczby.append(2)


found = False
ind = int(math.floor(razem/2))
turn = 1

while True:
    turn+=1
    if liczby[ind] == 1:
        diff = int(razem/turn/turn)
        if diff == 0:
            diff = 1
        ind+=diff

    else:
        if liczby[ind-1] == 1:
            break;
        else:
            diff = int(razem/turn/turn)
            if diff == 0:
                diff = 1
            ind-=diff
    if(turn>30):break

print(ind,"w turach:",turn)
