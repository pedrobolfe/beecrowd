#3050
# TIME LIMIT, mas a tendência é estar certo
n = int(input())
predios = list(map(int,input().split()))

aux = 0

for i in range(n): # pos da list
    for j in range(n): 
        cont = predios[i] + predios[j] + abs(i - j)
        if cont > aux:
            aux = cont
        
print(aux)
