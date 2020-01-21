def solution(n):
    f = [1,2]
    for i in range(2,n):
        f.append((f[i-1]+f[i-2])%1000000007)
    return f[-1]
