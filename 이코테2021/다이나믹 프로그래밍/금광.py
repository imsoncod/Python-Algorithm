n,m = map(int, input().split())

temp = list(map(int, input().split()))
cave = []
idx = 0
for i in range(n):
    cave.append(temp[idx:idx+m])
    idx+=m

#접근 방향
#    ->
# -> ->
#    ->

#점화식
#dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1]) + dp[i][j]

#i,j좌표 분석하는게 매우 헷갈린다...

for j in range(1, m):
    for i in range(n):
        #왼쪽 위에서 오는 경우
        if i == 0:
            left_up = 0
        else:
            left_up = cave[i-1][j-1]
        #왼쪽 아래에서 오는 경우
        if i == n-1:
            left_down = 0
        else:
            left_down = cave[i+1][j-1]
        #왼쪽에서 오는 경우
        left = cave[i][j-1]
        cave[i][j] = max(left_up, left, left_down) + cave[i][j]

result = 0
for i in range(n):
    result = max(result, cave[i][m-1])
print(result)
