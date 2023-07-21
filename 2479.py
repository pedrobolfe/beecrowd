# 2479

comportadas = 0
nao_comportadas = 0

list_nome = []

for i in range(int(input())):
    list_nome.append(input().split(' '))
    
    if '+' in list_nome[i]:
        list_nome[i].remove('+')
        comportadas +=1
        
    else:
        list_nome[i].remove("-")
        nao_comportadas += 1

list_nome.sort()


for p in list_nome:
    print(p[0])
print(f"Se comportaram: {comportadas} | Nao se comportaram: {nao_comportadas}")
