n, k = input().split()
n = int(n)
k = int(k)

coin = [0]*n
for i in range(n):
    coin[i] = int(input())

ans = 0
for i in range(n-1, -1, -1):
    ans += k//coin[i]
    k = k%coin[i]

print(ans)
