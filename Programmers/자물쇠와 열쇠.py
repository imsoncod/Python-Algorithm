def checking(key, lock):
    m = len(key)
    n = len(lock)
    r = n+2*(m-1)
    #위아래로 한칸씩 key를 이동시켜봄
    for a in range(r-m+1):
        for b in range(r-m+1):
            #background 초기화
            background = [[0] * r for _ in range(r)]
            for i in range(n):
                for j in range(n):
                    background[m-1+i][m-1+j] = lock[i][j]
            #key를 자물쇠에 대입시켜봄
            for i in range(m):
                for j in range(m):
                    if key[i][j]==1:
                        background[a+i][b+j] += 1
            check = 0
            for i in range(n):
                for j in range(n):
                    if background[m-1+i][m-1+j] == 2 or background[m-1+i][m-1+j] == 0:
                        check = 1
                        break
                if check:
                    break
            if check == 0:
                return True
    return False

def turn(key):
    m = len(key)
    newkey = [[0]*m for _ in range(m)]
    for i in range(m-1, -1, -1):
        for j in range(0,m):
            newkey[j][i] = key[abs(i-m+1)][j]
            #print('newkey[',j,'][',i,'] : ' , 'key[',abs(i-m+1),'][',j,']')
    return newkey

def solution(key, lock):
    answer = True
    for i in range(4):
        if checking(key,lock) == True:
            return True
        key = turn(key)
    return False
