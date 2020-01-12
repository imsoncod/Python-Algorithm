def solution(N):
    answer = 0
    x=[1,1]
    r=[4]
    for i in range(N-2):
        x.append(x[i]+x[i+1])    
    for i in range(N-1):
        r.append(r[i]+2*x[i+1])
    return r[-1]
