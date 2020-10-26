from collections import deque

def isInside(x,y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False

def bfs(x, y):
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if isInside(nx, ny) and miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                q.append([nx, ny])

n, m = map(int, input().split())
miro = []
dx = [-1,0,1,0]
dy = [0,1,0,-1]

for _ in range(n):
    miro.append(list(map(int, input())))

bfs(0, 0)

print(miro[n-1][m-1])
