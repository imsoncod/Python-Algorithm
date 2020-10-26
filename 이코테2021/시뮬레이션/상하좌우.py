def solution(n, plans):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    move = ['U', 'R', 'D', 'L']
    x,y = 1,1

    for plan in plans:
        idx = move.index(plan)
        nx = x + dx[idx]
        ny = y + dy[idx]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue

        x,y = nx,ny

    return (x,y)

print(solution(5, ['R','R','R','U','D','D']))
