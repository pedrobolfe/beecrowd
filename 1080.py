num=list()
for _ in range(100):
  x=int(input())
  num.append(x)
cont=0
for i in num:
  cont+=1
  if i == max(num):
    print(max(num))
    print(cont)
    break