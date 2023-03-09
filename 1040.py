N1, N2, N3, N4 = map(float,input().split())

media = ((N1*2)+(N2*3)+(N3*4)+(N4*1))/10

if media < 5.0:
    print(f'Media: {media:.1f}')
    print('Aluno reprovado.')
    
if media >= 5.0 and media <= 6.9:
    nota_exame  = float(input())
    print(f'Media: {media:.1f}')
    print('Aluno em exame.')
    print(f'Nota do exame: {nota_exame:.1f}')
    media_final = (media + nota_exame)/2.0
    if media_final >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {media_final:.1f}')
    
if media >= 7.0:
    print(f'Media: {media:.1f}')
    print('Aluno aprovado.')