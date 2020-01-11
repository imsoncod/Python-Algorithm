def solution(p, limit):
    boat = 0
    l = 0
    r = len(p)-1
    p.sort()
    while l <= r:
        boat+=1
        if p[l] + p[r] <= limit:
            l+=1
        r-=1
    return boat
