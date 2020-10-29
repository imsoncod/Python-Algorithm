from collections import deque

N, M, K, X = map(int, input().split())
city = [[] for _ in range(N+1)]
# 모든 도시에 대한 최단거리 초기화 후 출발 도시에 대한 거리는 0으로 설정
distance = [-1]*(N+1)
distance[X] = 0

for _ in range(M):
    a, b = map(int, input().split())
    city[a].append(b)

# 큐 선언
q = deque()
q.append(X)

while q:
    x = q.popleft()
    for p in city[x]:
        # 모든 간선의 거리가 1인 BFS이다
        # 방문했던 도시를 다시 방문하는것은 무조건 경유지가 있고 거리가 더 늘어나기 때문에 따지지 않아도 된다
        if distance[p] == -1:
            distance[p] = distance[x] + 1
            q.append(p)

for i, dist in enumerate(distance):
    if K == dist:
        print(i)
if K not in distance:
    print(-1)
