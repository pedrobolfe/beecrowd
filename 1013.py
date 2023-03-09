a,b,c = input().split()
a,b,c = int(a),int(b),int(c)

maiorAB = (a+b+abs(a-b))//2
maiorAC = (a+c+abs(a-c))//2
maiorBC = (b+c+abs(b-c))//2

maior = max(maiorAB, maiorAC, maiorBC)#daria para fazer direto apenas usando max(a,b,c) 

print(f'{maior} eh o maior')