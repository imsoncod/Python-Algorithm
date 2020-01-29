def hanoi(n, start, to, end, ans):
    if n==1:
        ans.append([start, end])
        return
    hanoi(n-1, start, end, to, ans)
    ans.append([start, end])
    hanoi(n-1, to, start, end, ans)

def solution(n):
    ans = []
    hanoi(n,1,2,3,ans)
    return ans
