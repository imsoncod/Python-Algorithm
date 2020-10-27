from bisect import bisect_left, bisect_right

def cnt_by_range(arr, left_value, right_value):
    return bisect_right(arr, right_value) - bisect_left(arr, left_value)

n, x = map(int, input().split())
arr = list(map(int, input().split()))

# [x, x] 범위에 있는 데이터의 개수 계산
cnt = cnt_by_range(arr, x, x)

if cnt == 0:
    print(-1)
else:
    print(cnt)
