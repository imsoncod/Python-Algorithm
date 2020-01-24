import math as m

def solution(n, k):
    ans = []
    k-=1
    num = list(range(1,n+1))
    while n!=0:
        n-=1
        a,b = divmod(k, m.factorial(n))
        ans.append(num[a])
        num.remove(num[a])
        k=b
    return ans
