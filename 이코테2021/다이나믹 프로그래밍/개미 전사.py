n = int(input())
food = list(map(int, input().split()))

dp = [0]*n
#점화식
#dp[n] = max(dp[n-2] + dp[n], dp[i-1])
#현재 식량창고를 터느냐 마느냐를 판단

for i in range(n):
    if i == 0:
        dp[0] = food[0]
    elif i == 1:
        dp[1] = max(dp[0], food[1])
    else:
        dp[i] = max(dp[i-2] + food[i], dp[i-1])

print(dp[n-1])
