# dupla de tenis, ex OBI 2021 fase 2 prog 1
a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(min({abs((a+b)-(c+d)), abs((a+c)-(b+d)), abs((a+d)-(b+c))}))
