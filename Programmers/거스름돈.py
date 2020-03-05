#백준 동전 1과 유사
def solution(n, money):
    answer = 0
    dp = [0]*(n+1)
    dp[0]=1
    for m in money:
        for i in range(m, n+1):
            dp[i] = dp[i] + dp[i-m]
    return dp[n]
