n,m = map(int, input().split())
x,y,dir = map(int, input().split())

gameMap = []
for _ in range(n):
    gameMap.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[0]*n for _ in range(m)]

answer = 1

visited[x][y] = 1

while True:
    check = False
    for _ in range(4):
        dir -= 1
        if dir == -4:
            dir = 0
        nx = x + dx[dir]
        ny = y + dy[dir]
        if gameMap[nx][ny] == 0 and visited[nx][ny] == 0:
            x = nx
            y = ny
            check = True
            break

    if check == False:
        # 방향을 - 해주면 반대 방향을 가리키게 된다
        x = x - dx[dir]
        y = y - dy[dir]
        if gameMap[x][y] == 1:
            break
    else:
        visited[x][y] = 1
        answer += 1

print(answer)
