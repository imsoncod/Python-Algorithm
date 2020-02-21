#피보나치 규칙이 발견됨
n = int(input())
dp = [1,1]
for i in range(2,n):
    dp.append(dp[i-1]+dp[i-2])
print(dp[n-1])
