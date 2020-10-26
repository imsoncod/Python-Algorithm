def isInside(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    return False

def dfs(x, y):
    if not isInside(x, y):
        return False
    if ice[x][y] == 0:
        ice[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

answer = 0
n, m = map(int, input().split())
ice = []

for _ in range(n):
    ice.append(list(map(int, input())))

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            answer += 1

print(answer)
