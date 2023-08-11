while True:
        x1, y1, x2, y2 = input().split()
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        if x1 ==0  and y1 == 0 and x2 == 0 and y2 ==0:
            break
        
        if x1 == x2 and y1 == y2: # verificar se estao no msm lugar
            print(0)
        elif x1 == x2 or y1 == y2: # msm linha, vertical ou horizontal 
            print(1)
        else: 
            # verificar se estao na adjacente, obs: deixar em módulo - abs()
            if abs(x1-x2) - abs(y1-y2) == 0:
                print(1)
            else: # se n estiverem, será 2 movimento
                print(2)
