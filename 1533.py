while True:
    num = input()
    if num == '0':
        break
    indices = list(map(int, input().split())) # cria uma lista de inteiros dos inputs
    indices[indices.index(max(indices))] = 0 # indices na pos do 1 maior numero vira 0
    print(indices.index(max(indices)) + 1) # printa o indice do 2 maior numero + 1
