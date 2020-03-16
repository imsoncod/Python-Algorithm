#LIS...가장 긴 증가하는 부분 수열을 활용
#PyPy3로 제출해서 겨우 통과했다
#그리디하게 풀 수 있는 방법이 없을까..?

n = int(input())
port = list(map(int,input().split()))
dp = [0]*n

for i in range(n):
    dp[i] = 1
    for j in range(i):
        if port[j] < port[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
