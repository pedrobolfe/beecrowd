for _ in range(int(input())):
    for _ in range(int(input())):
        idiomas=list()
        idioma =input()
        idiomas.append(idioma)
    test=idiomas[0]
    for i in idiomas:
        if i != test:
            test='ingles'
            break
    print(test)