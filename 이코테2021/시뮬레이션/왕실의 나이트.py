def solution(c):
    answer = 0

    map = [[0]*9 for _ in range(9)]
    alpha = ['a','b','c','d','e','f','g','h']
    x,y = int(c[1]), alpha.index(c[0]) + 1

    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 < nx <= 8 and 0 < ny <= 8:
            answer += 1

    return answer

print(solution("a1"))
