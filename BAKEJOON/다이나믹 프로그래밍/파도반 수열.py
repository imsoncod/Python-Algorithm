T = int(input())

for i in range(T):
    n = int(input())
    dp = [0,1,1,1,2,2]
    for j in range(6, n+1):
        dp.append(dp[j-1]+dp[j-5])
    print(dp[n])
