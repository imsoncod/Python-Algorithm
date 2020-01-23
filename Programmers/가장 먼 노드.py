def solution(n, edge):
    visit = [0]*(n+1)
    graph=[[] for _ in range(n+1)]
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    q = [1]
    visit[1] = 1
    while q:
        x = q.pop(0)
        for i in graph[x]:
            if visit[i]==0:
                visit[i]=visit[x]+1
                q.append(i)
    return visit.count(max(visit))
