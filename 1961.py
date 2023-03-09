P,N = map(int,input().split())
x = input().split()
for i in range(len(x)):
    x[i] = int(x[i])

def verifica(a,b,P):
    if abs(a-b) > P:
        return True
    else:
        return False

a = False
for i in range(N-1):
    a = verifica(x[i],x[i+1],P)
    if a == True:
        print('GAME OVER')
        break
if a == False:
    print('YOU WIN')