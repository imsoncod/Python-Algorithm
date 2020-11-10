N, M = map(int, input().split())
coin = []
for _ in range(N):
    coin.append(int(input()))

#최대값으로 리스트를 초기화
dp = [10001]*(M+1)
dp[0] = 0

for c in coin:
    for i in range(c, M+1):
        #i-c원을 만드는 방법이 존재하는 경우
        if dp[i-c] != 10001:
            dp[i] = min(dp[i], dp[i-c] + 1)

print(dp[M] if dp[M] != 10001 else -1)
