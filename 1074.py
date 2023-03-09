x = int(input())

for i in range(x):
    a = int(input())
    if a == 0:
        print('NULL')
    if a > 0:
        if a%2 ==0:
            print('EVEN POSITIVE')
        else:
            print('ODD POSITIVE')   
    if a < 0:
        if a%2 ==0:
            print('EVEN NEGATIVE')
        else:
            print('ODD NEGATIVE')       