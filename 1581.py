for _ in range(int(input())):
    idiomas = list()
    cont = 0
    aux = ''
    for _ in range(int(input())):
        idioma =input()
        idiomas.append(idioma)
        aux = idioma

    for i in range(len(idiomas)):
        if aux != idiomas[i-1]:
            cont -= 1    
        else:
            cont+=1
    if cont == len(idiomas):
      print(aux)    
    else:
      print("ingles")
