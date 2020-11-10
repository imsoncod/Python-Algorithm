#가장 긴 감소하는 부분 수열
#뒤집어서 가장 긴 증가하는 부분 수열(LIS)로 풀어도 됨

n = int(input())
attack = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if attack[j] > attack[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))
