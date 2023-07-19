while True:
    num = input()
    if num == '0':
        break
    indices = list(map(int, input().split()))
    indices[indices.index(max(indices))] = 0 # o 1 maior numero  vira 0
    print(indices.index(max(indices)) + 1) # printa o indice do 2 maior numero + 1
