#3050
# TIME LIMIT, mas a tendência é estar certo
n = int(input())
predios = list(map(int,input().split()))

aux = 0

for i in range(n-1): # pos da list
    for j in predios[i:]: 
        cont = predios[i] + j + abs(i - predios.index(j)+1)
        if cont > aux:
            aux = cont
        
print(aux)
