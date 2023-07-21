alternativa = ['A', 'B', 'C', 'D', 'E']

while True:
    n = int(input())
    
    if n ==0:
        break
    else:
        for _ in range(n):
            pixel = list(map(int,input().split(' ')))
            cont =0
            
            for i in range(5):
                if pixel[i] > 127:
                    # print('aaaa', pixel[i])
                    pixel[i] = 255
                    cont+=1

            if cont == 4:
                for p in pixel:
                    if p != 255:
                        print(alternativa[pixel.index(p)])
            else:
                print('*')
