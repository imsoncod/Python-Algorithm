import heapq

n,m,c = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [1e9] * (n+1)

for _ in range(m):
    start, end, dist = map(int, input().split())
    #그래프 데이터 = (end, start부터 end까지의 거리)
    graph[start].append((end, dist))

q = []
#힙 데이터 = (시적지점부터 x까지의 거리, x)
heapq.heappush(q, (0, c))
distance[c] = 0

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

cnt = 0
max_dist = 0
for dist in distance:
    if dist != 1e9:
        cnt += 1
        max_dist = max(max_dist, dist)

print(cnt - 1, max_dist)
