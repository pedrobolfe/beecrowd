num = float(input())

if num >= 0 and num <= 25.0:
    print('Intervalo [0,25]')   
elif num >= 25.01 and num <= 50.0:
    print('Intervalo (25,50]')   
elif num >= 50.01 and num <= 75.0:
    print('Intervalo (50,75)')   
elif num >= 75.01 and num <= 100.0:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')