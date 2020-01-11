def solution(c):
    cnt=0
    h=max(c)+1
    c.sort()
    while cnt<h:
        cnt=0
        h-=1
        for i in range(len(c)):
            if c[i] >= h:
                cnt = len(c)-i
                break     
    return h
