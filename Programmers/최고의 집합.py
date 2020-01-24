def solution(n, s):
    if s==1 or n>s: return [-1]
    ans = []
    while n!=0:
        ans.append(s//n)
        s-=ans[-1]
        n-=1
    return ans
