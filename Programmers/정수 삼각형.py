def solution(t):
    for i in range(len(t)-1):
        for j in range(len(t[i+1])):
            if j==0:
                    t[i+1][j] += t[i][j]
            elif j==len(t[i+1])-1:
                    t[i+1][j] += t[i][j-1]
            else:
                t[i+1][j] = max(t[i+1][j]+t[i][j-1],t[i+1][j]+t[i][j])         
    return max(t[-1])
