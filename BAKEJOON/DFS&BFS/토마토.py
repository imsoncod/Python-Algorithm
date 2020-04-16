from collections import deque
#deque는 pop과정이 시간복잡도 O(1)

def bfs(tomato):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    day = -1
    while q:
        day+=1
        #while문 안에 for문을 돌리는게 포인트
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if tomato[nx][ny] == 0:
                        q.append([nx, ny])
                        tomato[nx][ny] = tomato[x][y]+1
    for t in tomato:
        if 0 in t:
            return -1
    return day

m, n = map(int, input().split())
tomato = []
q = deque()

for i in range(n):
    tomato.append(list(map(int, input().split())))
    for j in range(m):
        #익어있는 토마토가 있는 부분을 큐에 다 넣고 한번에 탐색
        if tomato[-1][j] == 1:
            q.append([i, j])

print(bfs(tomato))
