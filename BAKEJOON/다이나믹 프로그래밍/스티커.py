T = int(input())
for _ in range(T):
    n = int(input())
    s = []
    for _ in range(2):
        s.append(list(map(int, input().split())))
    #dp[0 or 1][n] : 0 or 1번행 n번째 열 스티커를 뜯었을 때 얻을 수 있는 점수의 최댓값
    #1.다른 행, 바로 이전 열 스티커 + 현재 스티커
    #2.다른 행, 2번째 전 열 스티커 + 현재 스티커
    dp = [[0]*n, [0]*n]
    for i in range(n):
        if i == 0 :
            dp[0][0] = s[0][0]
            dp[1][0] = s[1][0]
        elif i == 1:
            dp[0][1] = dp[1][0]+s[0][1]
            dp[1][1] = dp[0][0]+s[1][1]
        else:
            dp[0][i] = s[0][i] + max(dp[1][i-1], max(dp[0][i-2],dp[1][i-2]))
            dp[1][i] = s[1][i] + max(dp[0][i-1], max(dp[0][i-2],dp[1][i-2]))
    print(max(dp[0][n - 1], dp[1][n - 1]))
