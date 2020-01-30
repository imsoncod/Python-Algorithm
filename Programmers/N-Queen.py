ans = 0
N = 0
def check(i, chess):
    for j in range(i):
        #위쪽, 대각선에 퀸이 존재하면 False
        if chess[i]==chess[j] or abs(chess[i]-chess[j])==i-j:
            return False
    return True
def dfs(i, chess):
    global N
    if i == N:
        global ans
        ans += 1
    else:
        for j in range(N):
            chess[i]=j
            if check(i, chess):
                dfs(i+1, chess)
def solution(n):
    global ans
    global N
    N=n
    chess = [0]*n
    dfs(0, chess)
    return ans
