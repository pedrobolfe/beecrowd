while True: # n sei se sestá certo kkkk
        lar, comp, r1, r2 = input().split()
        
        if lar == '0' and comp == '0' and r1 == '0' and r2 =='0':
            break
        
        r_total = int(r1)*2 + int(r2)*2
        
        if r_total <= int(lar) or r_total <= int(comp):
            print("S")
        else:
            print("N")
