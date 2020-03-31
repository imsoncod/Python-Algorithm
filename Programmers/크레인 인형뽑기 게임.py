def solution(board, moves):
    ans = 0
    stack = [0]
    n = len(board)

    for i in moves:
        for j in range(n):
            if board[j][i-1] != 0:
                stack.append(board[j][i-1])
                board[j][i-1] = 0
                break
        #배열의 길이 확인 조건을 먼저 넣어줘야 IndexError를 면할 수 있다        
        if len(stack) > 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            ans += 2
    return ans
