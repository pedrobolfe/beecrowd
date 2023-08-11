while True:
    frase = input().split()
    cont =0
    if frase[0] == "*":
        break  
    aux = frase[0][0].lower()
    for i in range(len(frase)):
        if frase[i][0].lower() == aux:
            cont+=1
        else: break
    if cont==len(frase):
        print("Y")
    else: print("N")
