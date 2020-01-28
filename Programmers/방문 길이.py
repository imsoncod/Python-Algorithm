def solution(dirs):
    ans = 0
    idx = 0
    arr = [[0]*11 for _ in range(11)]
    visit = []
    q=[[5,5]]
    while idx != len(dirs):
        x,y = q[0][0], q[0][1]
        q.pop(0)
        if dirs[idx]=='U':
                nx = x-1
                ny = y
        elif dirs[idx]=='R':
                nx = x
                ny = y+1
        elif dirs[idx] == 'D':
                nx = x+1
                ny = y
        elif dirs[idx] == 'L':
                nx = x
                ny = y-1
        idx+=1
        if nx<0 or 10<nx or ny<0 or 10<ny:
            q.append([x, y])
            continue
        if [x, y, nx, ny] in visit:
            q.append([nx, ny])
            continue
        visit.append([x, y, nx, ny])
        visit.append([nx, ny, x, y])
        q.append([nx, ny])
        ans+=1
    return ans
