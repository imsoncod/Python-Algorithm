n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

left = 0
right = max(arr)

answer = 0

while left <= right:
    sum = 0
    mid = (left+right)//2 # 절단기에 설정 할 높이
    for i in arr:
        if i > mid:
            sum += i - mid

    # 떡의 양이 충분할 경우 절단기의 높이를 높여 덜 자르기
    if sum >= m:
        answer = mid
        left = mid + 1
    # 떡의 양이 부족할 경우 절단기의 높이릘 낮추어 많이 자르기
    else:
        right = mid - 1

print(answer)
