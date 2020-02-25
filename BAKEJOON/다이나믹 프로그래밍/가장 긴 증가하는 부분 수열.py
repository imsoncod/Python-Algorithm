#LIS(Longest Increasing Subsequence)
n = int(input())

num = list(map(int, input().split()))

#dp[n] : n번째 수로 끝나는 가장 긴 증가하는 부분수열(LIS)의 길이
dp = [1]*n

for i in range(1, n):
    for j in range(i):
        if num[j] < num[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
