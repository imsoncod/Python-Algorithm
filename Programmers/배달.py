def solution(N, road, K):
    arr = [[0]*(N+1) for _ in range(N+1)]
    for a, b, c in road:
        if arr[a][b] == 0 and arr[b][a]==0:
            arr[a][b], arr[b][a] = c, c
        elif arr[a][b] > c:
            arr[a][b], arr[b][a] = c, c
    distance = [987654321]*(N+1)
    q=[1]
    distance[1]=0
    while len(q):
        x = q.pop(0)
        for y in range(1,N+1):
            if arr[x][y]!=0:
                #distance[y] = 1부터 y까지의 거리
                if distance[y] > distance[x]+arr[x][y] and distance[x]+arr[x][y] <= K:
                    distance[y] = distance[x]+arr[x][y]
                    q.append(y)
    return len([i for i in distance if i <= K])
