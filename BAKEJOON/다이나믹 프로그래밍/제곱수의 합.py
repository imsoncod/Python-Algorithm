n = int(input())

#dp[n] : n을 제곱수의 합으로 나타낼 때 그 제곱수 항의 최소 개수
#dp[7] = dp[2^2]+dp[3]
#n보다 작은 제곱수를 빼면서 탐색한다
dp = [0]*(n+1)

for i in range(1, n+1):
    dp[i] = i
    for j in range(1, i):
        if i - j*j < 0:
            break
        dp[i] = min(dp[i], dp[i-j*j]+1)
print(dp[n])
