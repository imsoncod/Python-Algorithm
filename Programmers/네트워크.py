def dfs(n, computers, visit, start):
    if visit[start]==1 or start>=n:
        return
    visit[start] = 1
    for i in range(n):
        if i!=start and computers[start][i]:
            dfs(n,computers,visit,i)

def solution(n, computers):
    net = 0
    visit = [0]*n
    for i in range(n):
        if visit[i]!=1:
            dfs(n, computers, visit, i)
            net+=1
    return net
