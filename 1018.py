a = int(input())
print(a)

cedulas = [100, 50, 20, 10, 5, 2, 1]
for i in cedulas:
    qnt_cedulas = int(a / i)
    a -= qnt_cedulas * i
    print('{} nota(s) de R$ {},00'.format(qnt_cedulas, i))