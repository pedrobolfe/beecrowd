n = int(input())
t = list(map(int, input().split()))

t.sort(reverse = True)

ans = t[0] + 2
for i in range(1, n):
    if i + 2 + t[i] > ans:
        ans = i + 2 + t[i]

print(ans)
