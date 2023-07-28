list_nums = [int(input()) for _ in range(int(input()))]
   
cont = 1 
for i in range(0, len(list_nums)-1):
    atual = list_nums[i]
    prox = list_nums[i+1]
    
    if atual != prox:
        cont+=1

print(cont)
