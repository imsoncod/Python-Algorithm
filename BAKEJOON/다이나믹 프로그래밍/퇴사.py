n = int(input())
t=[0]*17
p=[0]*17

for i in range(1,n+1):
    T,P = input().split()
    t[i] = int(T)
    p[i] = int(P)

#dp[n] : n일날 예약된 상담을 완료하였을 때 얻게 되는 금액의 최댓값
dp = [0]*17
for i in range(n,0,-1):
    if i + t[i] <= n+1:
        dp[i] = max(dp[i+t[i]]+p[i], dp[i+1])
    else:
        dp[i] = dp[i+1]
print(max(dp))
