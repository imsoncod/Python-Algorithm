# DP
# 메모리 : 35308KB / 시간 : 1008ms
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

#dp[i][j] : (1,1)부터 (i,j)까지 모든 원소의 합
dp = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = arr[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[i-1][y] - dp[x][j-1] + dp[i-1][j-1])

#===========================================================================#

# 일반 풀이 
# 메모리 : 124568KB / 시간 : 2884ms
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

k = int(input())

for _ in range(k):
    i, j, x, y = map(int, input().split())
    ans = 0
    for f in range(i-1, x):
        ans += sum(arr[f][j-1:y])
    print(ans)
