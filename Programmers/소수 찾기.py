def solution(n):
    visit = [True]*(n+1)
    m = int(n**1/2)
    for i in range(2,m+1):
        if visit[i]==True:
            for j in range(i*2, n+1, i):
                visit[j]=False
    return len([i for i in range(2,n+1) if visit[i]==True])
