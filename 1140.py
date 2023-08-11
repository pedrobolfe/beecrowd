while True:
    frase = input().split()
    if frase[0] == "*": break  

    aux = frase[0][0].lower()
    aux2=""
    
    for i in range(len(frase)):
        if frase[i][0].lower() != aux:
            aux2="N"
            break
        aux2 = "Y"
    print(aux2)
