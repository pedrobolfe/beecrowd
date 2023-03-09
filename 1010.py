codigo, numero, valor_unitario = map(float,input().split())
codigo2, numero2, valor_unitario2 = map(float,input().split())

valor = (numero * valor_unitario) + (numero2 * valor_unitario2)

print(f'VALOR A PAGAR: R$  {valor:.2f}')
