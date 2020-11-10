n = int(input())

dp = [0]*(n+1)

#n을 1로 만드는 연산의 수는
#반대로
#1을 n으로 만드는 연산의 수와 같다

#점화식
#dp[n] = min(dp[n//5], dp[n//3], dp[n//2], dp[n-1]) + 1

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i%5 == 0:
        dp[i] = min(dp[i], dp[i//5] + 1)

print(dp[n])
