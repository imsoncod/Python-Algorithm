def solution(money):
    dp1 = [0]*(len(money)-1)
    dp1[0] = money[0]
    dp1[1] = money[0]
    for i in range(2,len(money)-1):
        dp1[i] = max(dp1[i-2]+money[i], dp1[i-1])
    dp2 = [0]*len(money)
    dp2[0] = 0
    dp2[1] = money[1]
    for i in range(2,len(money)):
        dp2[i] = max(dp2[i-2]+money[i], dp2[i-1])
    return max(dp1[-1], dp2[-1])
