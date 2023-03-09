#se N for par divide por dois e multplica por N
#se N for impar o branco vai ter um a mais que o preto e preto um a menos
num = int(input())
if num%2==0:
    i = (num//2)*num
    print(f'{i} casas brancas e {i} casas pretas')
else:
    i = int(((num*num)+1)/2)
    print(f'{i} casas brancas e {(num*num)-i} casas pretas')
