n = int(input())

#dp[n][i] : 길이가 n이고 i로 시작하는 오르막 수의 개수
dp = [[0]*10 for _ in range(n+1)]
for i in range(10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][j:])

# n i  0  1  2  3  4  5  6  7  8  9
# 1 |  1  1  1  1  1  1  1  1  1  1
# 2 | 10  9  8  7  6  5  4  3  2  1
# 3 | 55 45 36 28 21 15 10  6  3  1

print(sum(dp[n]))
