def check(stones, k, mid):
    person = 0
    for st in stones:
        if st-mid < 0:
            person += 1
        else:
            person = 0
        if person >= k:
            return False
    return True

def solution(stones, k):
    left, right = 1, max(stones)+1 #마지막 돌도 계산범위에 넣어주기 위해 +1
    #이분탐색
    while left + 1 < right:
        #mid : 건널 수 있는 사람의 수
        mid = (left+right)//2
        if check(stones, k, mid):
            left = mid
        else:
            right = mid
    return left
