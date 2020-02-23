n = int(input())
#dp[n] : n번째 까지 마실수 있는 최대 와인의 양
dp = [0]*n
grape = []
for _ in range(n):
    grape.append(int(input()))
dp[0] = grape[0]
if n > 1:
    dp[1] = grape[0]+grape[1]
    if n > 2:
        dp[2] = max(grape[0]+grape[1],grape[0]+grape[2],grape[1]+grape[2])
for i in range(3,n):
    dp[i] = max(dp[i-3]+grape[i-1]+grape[i], dp[i-2]+grape[i], dp[i-1])
print(max(dp))
