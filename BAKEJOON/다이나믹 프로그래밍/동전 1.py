n, k = map(int, input().split())

coin = []
for _ in range(n):
    coin.append(int(input()))

#dp[n] : n원을 만들 수 있는 경우의 수
dp = [0]*(k+1)
dp[0] = 1
for c in coin:
    for j in range(c, k+1):
        dp[j] += dp[j-c]
print(dp[k])

#동전이 1원 한 개 일때
#      k 1 2 3 4 5 6 7 8 9 10
#경우의수 1 1 1 1 1 1 1 1 1 1

#동전이 1,2원 두 개 일때
#      k 1 2 3 4 5 6 7 8 9 10
#경우의수 1 2 2 3 3 4 4 5 5 6

#동전이 1,2,5 세 개 일때
#      k 1 2 3 4 5 6 7 8 9 10
#경우의수 1 2 2 3 4 5 6 7 8 10
