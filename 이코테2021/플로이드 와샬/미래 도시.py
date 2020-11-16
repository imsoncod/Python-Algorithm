n,m = map(int, input().split())
graph = [[1e9] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 1 -> K를 거쳐 -> X로 감
X, K = map(int, input().split())

for k in range(1, n+1):
    for x in range(1, n+1):
        for y in range(1, n+1):
            graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

distance = graph[1][K] + graph[K][X]

if distance >= 1e9:
    print(-1)
else:
    print(distance)
