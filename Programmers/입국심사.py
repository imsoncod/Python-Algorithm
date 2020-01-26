def solution(n, times):
    left = 0
    right = max(times)*n
    ans = right
    while left <= right:
        people = 0
        mid = (left+right)//2
        for i in times:
            people+=mid//i
        if people >= n:
            ans = mid
            right = mid-1
        elif people < n:
            left = mid+1
    return ans
