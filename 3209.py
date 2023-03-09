for _ in range(int(input())):
    k = list(map(int, input().split()))
    print(sum(k[1:])-len(k)+2)