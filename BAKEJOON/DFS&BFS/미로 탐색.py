def bfs():
    q = [[0,0]]
    while q:
        x,y = q.pop(0)
        for i in range(4):
            nx = x + dirx[i]
            ny = y + diry[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1:
                    q.append([nx,ny])
                    arr[nx][ny] = arr[x][y] + 1
    return arr[n-1][m-1]

n, m = map(int, input().split())
arr = []
dirx = [-1,0,1,0]
diry = [0,1,0,-1]
for _ in range(n):
    arr.append(list(map(int, input())))
print(bfs())
