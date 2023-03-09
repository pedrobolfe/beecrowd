nome = input()
salario_fixo = float(input())
total_vendas = float(input())

comissao = total_vendas * 0.15

salario_mes = salario_fixo + comissao 

print(f'TOTAL = R$ {salario_mes:.2f}')