for _ in range(int(input())):
    a, b = input().split()
    
    if int(b) > int(a):
        print('nao encaixa')
    else:
        if a[len(a)-len(b):] == b:
            print('encaixa')
        else: print('nao encaixa')
