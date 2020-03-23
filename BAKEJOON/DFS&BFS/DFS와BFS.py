def dfs(v):
    if visit1[v]:
        return
    visit1[v] = 1
    print(v, end=' ')
    for i in range(1, n+1):
        if arr[v][i] == 1:
            dfs(i)

def bfs(v):
    q = [v]
    visit2[v] = 1
    while q:
        x = q.pop(0)
        print(x, end=' ')
        for i in range(1, n+1):
            if arr[x][i] == 1 and visit2[i] == 0:
                q.append(i)
                visit2[i] = 1

n, m, v = map(int, input().split())
arr = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

visit1 = [0] * (n + 1)
visit2 = [0] * (n + 1)

dfs(v)
print()
bfs(v)
