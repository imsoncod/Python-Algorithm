def solution(maps):
    n = len(maps[0])
    m = len(maps)
    visit = [[0]*n for _ in range(m)]
    dirx = [-1,0,1,0]
    diry = [0,1,0,-1]
    q = [(0,0)]
    check = 0
    while len(q):
        x, y = q.pop(0)
        if x == m-1 and y == n-1:
            check = 1
        for i in range(4):
            nx = x + dirx[i]
            ny = y + diry[i]
            if 0 <= nx < m and 0 <= ny < n:
                if visit[nx][ny] == 0 and maps[nx][ny] == 1:
                    visit[nx][ny] = visit[x][y]+1
                    q.append((nx,ny))
    return visit[m-1][n-1]+1 if check else -1
