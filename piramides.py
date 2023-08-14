# exercicio piramides, OBI 2022 2 fase

n=  int(input())

nums = ''

for i in range(1, n+1):
    for j in range(1, n+1):
        nums += str(min([i-1, j-1, n-i, n-j])+1) + " "
    nums+='\n'

print(nums)
