def isInside(x,y):
    if 0<= x < n and 0 <= y < n:
        return True
    else:
        return False

def bfs(x,y, cnt):
    q = [[x,y]]
    visit[x][y] = 1
    while q:
        x, y = q[0][0], q[0][1]
        q.pop(0)
        cnt+=1
        for i in range(4):
            nx = x + dirx[i]
            ny = y + diry[i]
            if isInside(nx, ny):
                if arr[nx][ny]==1 and visit[nx][ny] == 0:
                    q.append([nx,ny])
                    visit[nx][ny] = 1
    return cnt

n = int(input())
dirx = [-1,0,1,0]
diry = [0,1,0,-1]
ans = []
arr = []
visit = [[0]*n for _ in range(n)]

for _ in range(n):
    arr.append(list(map(int, input())))

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and visit[i][j] == 0:
            cnt = 0
            ans.append(bfs(i,j, cnt))
ans.sort()

print(len(ans))
for i in range(len(ans)):
    print(ans[i])
