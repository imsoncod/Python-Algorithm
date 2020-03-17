#가로, 세로에 따라 움직일 수 있는 곳에 제한이 있음
n, m = map(int, input().split())
ans = 1
if n == 2:
    ans = min(4, (m+1)//2)
elif n >= 3:
    if m >= 7:
        ans = m - 2
    else:
        ans = min(4, m)
print(ans)
