# 쉬운건데 감을 너무 잃었다...
n, m = map(int, input().split())

miro = [[0]*(m+1)]
for _ in range(n):
    miro.append([0]+list(map(int,input().split())))

for i in range(1,n+1):
    for j in range(1,m+1):
        miro[i][j] += max(miro[i-1][j-1], miro[i-1][j], miro[i][j-1])

print(miro[n][m])
