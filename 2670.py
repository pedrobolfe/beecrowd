andar1, andar2, andar3 = int(input()), int(input()), int(input())

andares = [andar1, andar2, andar3]
temp=[]

temp.append(andares[0]*2 + andares[2]*2)
temp.append(andares[0]*4 + andares[1]*2)
temp.append(andares[1]*2 + andares[2]*4)

temp.sort()
print(temp[0])
