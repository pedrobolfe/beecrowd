while True:
    a = int(input())
    
    if a == 0: # se a for 0 o programa fecha
        break
    
    ini=10
    
    tempo = list(map(int,input().split())) # obtendo os tempos
    
    # cada pessoa fica 10s na escada, porem pode ter mais de uma pessoa na mesma escada
    # comparar se o tempo de cada pessoa for maior que 10s da pessoa que chegou antes, pegar a diferença delas
    # e ver se for maior que 10s add 10s, senao add a dif entre elas
    for i in range(1, len(tempo)): # i começa na 1 para poder pegar a pos anterior dele
        dif = tempo[i] - tempo[i -1] # i-1 para pegar a pos anterior e n dar erro, i+1 vai dar erro de memória
        if dif > 10:
            ini += 10
        else:
            ini += dif
        
    print(ini)
