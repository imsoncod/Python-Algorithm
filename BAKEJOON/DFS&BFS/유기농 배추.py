# dfs 재귀 횟수 주의
import sys
sys.setrecursionlimit(100000)

def dfs(x,y):
    if visit[x][y]:
        return
    visit[x][y] = 1

    dirx = [-1,0,1,0]
    diry = [0,1,0,-1]
    for i in range(4):
        nx = x + dirx[i]
        ny = y + diry[i]
        if 0 <= nx < n and 0 <= ny < m:
            if ground[nx][ny] == 1:
                dfs(nx, ny)

T = int(input())
for _ in range(T):
    ans = 0
    m, n, k = map(int, input().split())

    ground = [[0]*m for _ in range(n)]
    visit = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        ground[y][x] = 1

    for i in range(n):
        for j in range(m):
            if ground[i][j] == 1 and visit[i][j] == 0:
                dfs(i,j)
                ans += 1
    print(ans)
