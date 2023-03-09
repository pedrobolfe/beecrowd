n = float(input())
print('NOTAS:')
notas = [100, 50, 20, 10, 5, 2, ]
for i in notas:
    qnt_notas = int(n/i)
    n -= qnt_notas * i   
    print(f'{qnt_notas:.0f} nota(s) de R$ {i}.00')
print('MOEDAS:')
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
for a in moedas:
    n = round(n,2)
    qnt_moedas = int(n/a)
    n -= qnt_moedas * a
    print(f'{qnt_moedas:.0f} moeda(s) de R$ {a:.2f}')
    