def solution(n):
    a=[0]*(n+1)
    a[0] = 1
    s = 0
    for i in range(2,n+1,2):
        a[i] = 3*a[i-2] + 2*s
        s += a[i-2]
    return a[n]%1000000007
