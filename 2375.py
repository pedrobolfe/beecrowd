diametro = int(input())
alt, comp, vol = map(int,input().split())

if alt >= diametro:
  print('S')
else:
  print('N')
