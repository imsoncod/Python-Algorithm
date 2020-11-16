from collections import deque

#노드와 간선의 개수를 입력 받음
v, e = map(int, input().split())
#모든 노드에 대한 진입차수를 0으로 초기화
indegree = [0]*(v+1)
#각 노드에 연결된 간선 정보를 담기위한 그래프 초기화
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) #a에서 b로 이동 가능
    indegree[b] += 1 #b의 진입차수 1 증가

def topology_sort():
    result = []
    q = deque()

    #진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            #해당 노드와 연결된 간선을 제거함 = 진입차수 - 1
            indegree[i] -= 1
            #진입차수가 0은 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')
        
topology_sort()
