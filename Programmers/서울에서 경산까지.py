def solution(K, travel):
    dp = [[0]*100001 for _ in range(len(travel))]
    ans = 0
    dp[0][travel[0][0]] = travel[0][1]
    dp[0][travel[0][2]] = travel[0][3]
    for i in range(1,len(travel)):
        for k in range(K):
            if dp[i-1][k] == 0 :
                continue
            if k + travel[i][0] <= K:
                dp[i][k+travel[i][0]] = dp[i-1][k]+travel[i][1]
                ans = max(dp[i][k+travel[i][0]], ans)
            if k + travel[i][2] <= K:
                dp[i][k+travel[i][2]] = max(dp[i][k+travel[i][2]],dp[i-1][k]+travel[i][3])
                ans = max(dp[i][k+travel[i][2]], ans)
    return ans
