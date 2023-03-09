MAXIDITON = []
cont = 0
while True:
    try:
        x = int(input())
        MAXIDITON.append(x)
        cont = cont + 1
    except:
        break
for i in MAXIDITON[0:cont]:
    if i == 0:
        print('vai ter copa!')
    if i != 0:
        print('vai ter duas!')