import math
czp=int(0)
ile=int(0)

moce=[0,0,0,0,0,0,0,0,0,0]
min = -1
max = 0

def get_nums(x):
    nums = []
    if x==1: return [1]
    if x==2: return [2]
    while True:
        for i in range(2,int(x)+1):
            if i == x:
                nums.append(i)
                return nums
            if x % i == 0:
                nums.append(i)
                x /= i
                break
j=0 

def odwrot(x):
    x = str(x)
    odwrot = ""
    for i in range(0,len(x)):
        odwrot += x[len(x)-1-i]
    # print(x,odwrot)
    return odwrot

with open("../dane/59/liczby.txt","r") as file:
    for line in file:
        j+=1
        num = int(line)
        # print(num)

        #59.1
        is_good = True
        nums = get_nums(num)
        nums = dict.fromkeys(nums)
        for x in nums:
            if x%2==0:
                is_good=False
        if len(nums) != 3:
            is_good=False
        if is_good:
            czp=czp+1 
        print(j,czp)

        #59.2
        odwrotnosc = odwrot(num)
        suma = str(num+int(odwrotnosc))
        is_good = True
        for k in range(0,math.floor(len(suma)/2)):
            if suma[k] != suma[len(suma)-1-k]:
                is_good = False
        if is_good:
            ile += 1

        #59.3
        cyfra = str(num)
        moc = 0
        while int(cyfra) > 9:
            iloczyn = 1
            for k in range(0,len(cyfra)):
                iloczyn *= int(cyfra[k])
            cyfra = str(iloczyn)
            moc+=1
        moce[moc] += 1
        if moc == 1:
            if num > max:
                max = num
            if num < min or min < 0:
                min = num
        # print(num,moc)


print("==============")
print("59.1:",czp)
print("59.2:",ile)
print("59.3\n")
for i in range(0,len(moce)):
    print("moc",i,moce[i])
print("min o mocy 1:",min)
print("max o mocy 1:",max)

with open("wyniki_liczby.txt","w") as file:
    file.write("59.1: ");
    file.write(str(czp));
    file.write("\n\n59.2: ");
    file.write(str(ile));
    file.write("\n\n59.3: ");
    for i in range(0,len(moce)):
        file.write("liczby o mocy "+str(i)+": "+str(moce[i])+"\n")
    file.write("\nmin o mocy 1: "+str(min))
    file.write("\nmax o mocy 1: "+str(max))