def solution(m, n, b):
    ans = 0
    board = [[0]*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            board[i][j] = b[i][j]
    score = 1
    while score != 0:
        score = 0
        check = [[1]*n for i in range(m)]
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j]!=0:
                    x = board[i][j]
                    if x == board[i+1][j] and x == board[i][j+1] and x == board[i+1][j+1]:
                        check[i][j], check[i+1][j], check[i][j+1], check[i+1][j+1] = 0,0,0,0
                        score = 1
        for i in range(m):
            for j in range(n):
                if check[i][j]==0:
                    board[i][j]=0
                    ans+=1
        for i in range(m-2,-1,-1):
            print(i)
            for j in range(n):
                if board[i+1][j]==0 and board[i][j]!=0:
                    idx = i
                    while board[idx+1][j]==0:
                        board[idx+1][j]=board[idx][j]
                        board[idx][j] = 0
                        idx+=1
                        if idx==m-1:
                            break
        #for i in board:
            #print(i, sep='\n')
            
    return ans
