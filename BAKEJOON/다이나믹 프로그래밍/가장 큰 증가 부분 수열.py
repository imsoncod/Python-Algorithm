#LIS(가장 긴 증가하는 부분 수열)과 비슷
n = int(input())
arr = list(map(int, input().split()))
dp = [0]*n

for i in range(n):
    dp[i] = arr[i]
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+arr[i])
print(max(dp))
