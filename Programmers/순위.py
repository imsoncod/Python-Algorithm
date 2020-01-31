ans = 0
def search(target, win, lose, arr, n, bigo):
    if len(win) + len(lose) == n-1:
        global ans
        ans+=1
        return
    for i in range(1,n+1):
        if arr[target][i] == 0:
            continue
        if arr[target][i] == 2 and i not in win and bigo == 2:
            win.append(i)
            search(i, win, lose, arr, n, 2)
        elif arr[target][i] == 1 and i not in lose and bigo == 1:
            lose.append(i)
            search(i, win, lose, arr, n, 1)
    return
def solution(n, results):
    arr = [[0]*(n+1) for _ in range(n+1)]
    for a, b in results:
        arr[a][b] = 2
        arr[b][a] = 1
    for i in range(1,n+1):
        win = []
        lose = []
        if arr[i].count(0) == 2:
            global ans
            ans+=1
        else:
            search(i, win, lose, arr, n, 2)
            if len(win) != n-1:
                search(i, win, lose, arr, n, 1)
    return ans
