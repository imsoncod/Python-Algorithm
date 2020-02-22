n = int(input())
#dp[n][k] : n층 k번째 왔을 때 수의 합의 최댓값
dp = []
for _ in range(n):
    dp.append(list(map(int, input().split(' '))))
for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + dp[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + dp[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1]+dp[i][j], dp[i-1][j]+dp[i][j])
print(max(dp[n-1]))
