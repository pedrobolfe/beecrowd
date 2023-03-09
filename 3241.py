for i in range(int(input())):
    x = input()
    if x == 'P=NP':
        print('skipped')
    else:
        x = x.split('+')
        print(int(x[0])+int(x[1]))