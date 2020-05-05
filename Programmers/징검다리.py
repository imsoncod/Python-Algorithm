# 이분탐색
# mid : 돌과 돌사이의 거리
# mid보다 돌과 돌사이의 거리가 작으면 뒤의 돌을 제거한다

import math
def solution(distance, rocks, n):
    ans = 0
    rocks.sort() # 돌 오름차순 정렬
    rocks.append(distance) # 도착지점을 추가해줌

    left = 0
    right = distance

    while left <= right:
        remove_rock = 0  # 제거한 돌의 개수
        prev = 0 # 바로 앞의 돌
        mid = (left + right)//2

        for rock in rocks:
            if rock - prev < mid:
                remove_rock += 1 # 돌 제거
            else:
                prev = rock # 그대로 둠
        if remove_rock > n: # 제거한 돌의 수가 n보다 크면
            right = mid - 1 # 돌과 돌 사이의 거리를 줄이고 다시
        else:
            left = mid + 1 # 돌과 돌사이의 거리를 늘리고 다시
            ans = max(ans, mid) # 제거한 돌의 수가 n보다 작으면 우선 답이 될 여지가 있음
            
    return ans
