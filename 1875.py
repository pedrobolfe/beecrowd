for _ in range(int(input())):
        times = ["R", "B", "G"]
        
        gols = {
            "R" : 0,
            "B": 0,
            "G": 0,
        }
        
        for i in range(int(input())):
            m, s = input().split()
            
            if times[times.index(m)] == times[times.index(m)-1]:
                gols[m] += 2
            else:
                gols[m] += 1
                
        if gols["R"] > gols["B"] and gols["R"] > gols["G"]:
            print('red')
        elif gols["B"] > gols["R"] and gols["B"] > gols["G"]:
            print('blue')
        elif gols["G"] > gols["B"] and gols["G"] > gols["R"]:
            print('green')  
        elif gols["R"] == gols["B"] and gols["R"] == gols["G"]:
            print('trempate')
        elif gols["R"] == gols["B"] or gols["R"] == gols["G"] or gols["B"] == gols["G"]:
            print('empate')
