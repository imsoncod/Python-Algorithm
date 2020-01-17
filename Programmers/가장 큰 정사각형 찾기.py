def solution(board):
    check = 0
    for i in board:
        if 1 in i:
            check = 1
            break
    if check:        
        w, h = len(board[0]), len(board)
        r=1
        for j in range(w-1):
            for i in range(h-1):
                if board[i][j]:
                    if board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
                        board[i+1][j+1]+=min(board[i][j], board[i+1][j], board[i][j+1])
                        r = max(r, board[i+1][j+1])
        return r**2
    else:
        return 0
