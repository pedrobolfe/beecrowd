doces = int(input())

list_doces = [int(input()), int(input()), int(input())]
list_doces.sort()

cont=0
for i in list_doces:
    if i <= doces:
        doces-=i
        cont+=1
        
print(cont)
