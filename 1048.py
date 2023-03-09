a = float(input())

if 0 <= a <= 400.00:
    b = a * 1.15
    c = b - a 
    d = 15
    
elif 400.01 <= a <= 800.00:
    b = a *1.12
    c = b - a
    d = 12
    
elif 800.01 <= a <= 1200.00:
    b = a * 1.10
    c = b - a
    d = 10
elif 1200.01 <= a <= 2000.00:
    b = a * 1.07
    c = b - a
    d = 7
    
elif a >= 2000.01:
    b = a * 1.04
    c = b - a
    d = 4
    
print(f'Novo salario: {b:.2f}\nReajuste ganho: {c:.2f}\nEm percentual: {d} %')