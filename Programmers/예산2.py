#이분 탐색
def solution(budgets, M):
    ans = 0
    budgets.sort()
    left,right = 0,budgets[-1]
    while left<=right:
        result = 0
        pivot = (left+right)//2
        for i in budgets:
            result += min(pivot, i)
        if result>M:
            right = pivot-1
        else:
            ans = max(ans,pivot)
            left = pivot+1
    return ans
