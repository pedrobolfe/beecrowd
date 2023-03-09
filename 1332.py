for _ in range(int(input())):
    palavra = input()
    
    if len(palavra) == 5:
        print('3')
    else:
        um='one'
        cont=0
        if len(palavra) == 3:# aqui
            for i in range(3):
                if um[i] == palavra[i]:
                    cont+=1
            if cont >= 2:
                print('1')
            else:
                print('2')