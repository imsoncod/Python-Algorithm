n = int(input())

card = list(map(int, input().split()))
card.insert(0,0)

#dp[n] : n개의 카드를 갖기 위해 지불해야 하는 금액의 최댓값
dp = [0]*(n+1)
dp[1] = card[1]

for i in range(2,n+1):
    for j in range(i+1):
        dp[i] = max(dp[i-j]+card[j], dp[i])
print(dp[n])
