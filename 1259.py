par = []
impar = []


for i in range(1,int(input())):
  #num = int(input())
  if i%2==0:#verifica se e par ou impar
    par.append(i)
  else:
    impar.append(i)

par.sort()#vai deixar em ordem crescente
impar.sort(reverse=True)#vai deixar em ordem decrescente


for par2 in par:
  print(par2)
for impar2 in impar:
  print(impar2)