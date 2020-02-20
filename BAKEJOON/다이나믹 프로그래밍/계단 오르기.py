n = int(input())
stairs = []
for i in range(n):
    stairs.append(int(input()))

#dp[n] : n번째 계단에 올라왔을 때 얻을 수 있는 점수의 최댓값
dp = [0]*n

#문제 조건상 n번째 계단은 무조건 밟아야 한다

dp[0] = stairs[0] #계단이 1개일 때
dp[1] = stairs[0] + stairs[1] #계단이 2개일 때
dp[2] = max(stairs[0] + stairs[2], stairs[1]+stairs[2]) #계단이 3개 일때

for i in range(3,n):
    #1칸아래 계단에서 올라오거나, 2칸아래 계단에서 올라올 경우중 큰 값
    dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])
    
print(dp[n-1])
