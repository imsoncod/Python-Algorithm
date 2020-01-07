def solution(N, stages):
    fail = {}
    answer = []
    for i in range(1,N+1):
        xplayer = 0
        oplayer = 0
        for stage in stages:
            if stage >= i:
                oplayer+=1
                if stage == i:
                    xplayer+=1
        if oplayer == 0:
            fail[i] = 0
        else:
            fail[i] = xplayer/oplayer
    for i in range(N):
        answer.append(sorted(fail.items(), key=lambda k : k[1], reverse=True)[i][0])
    return answer
