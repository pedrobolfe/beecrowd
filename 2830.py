a, b = (int(input()) - 1), (int(input()) - 1)

if (a//2) == (b//2):
    print("oitavas")
elif a//4 == b//4:
    print("quartas")
elif a//8 == b//8:
    print("semifinal")
else:
    print("final")
