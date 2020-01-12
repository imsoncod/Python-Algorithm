def solution(n, costs):
    costs.sort(key=lambda x:x[2])
    visit = [0]*n
    visit[0]=1
    ans = 0
    while sum(visit)!=n:
        for c in costs:
            start, end, cost = c
            if visit[start] or visit[end]:
                if visit[start] and visit[end]:
                    continue
                visit[start] = 1; visit[end] = 1
                ans+=cost
                break
    return ans
