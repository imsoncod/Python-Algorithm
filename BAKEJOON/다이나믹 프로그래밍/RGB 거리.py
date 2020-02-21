n = int(input())
rgb = []
for i in range(n):
    r,g,b = input().split(' ')
    rgb.append([int(r),int(g),int(b)])

#dp[n][r,g,b] : n번째 집까지 칠했을 때 드는 비용의 최솟값
dp = [[0,0,0] for _ in range(n)]

for i in range(3):
   dp[0][i] = rgb[0][i]
    
for i in range(1, n):
   dp[i][0] = min(rgb[i][0]+dp[i-1][1], rgb[i][0]+dp[i-1][2]) #i번째 집에 빨간색을 칠할 경우
   dp[i][1] = min(rgb[i][1]+dp[i-1][0], rgb[i][1]+dp[i-1][2]) #i번째 집에 초록색을 칠할 경우
   dp[i][2] = min(rgb[i][2]+dp[i-1][0], rgb[i][2]+dp[i-1][1]) #i번째 집에 파란색을 칠할 경우
    
print(min(dp[n-1]))   
