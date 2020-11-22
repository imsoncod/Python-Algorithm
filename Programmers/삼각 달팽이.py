#항상 똑같은 3방향을 반복하며 순차적으로 탐색한다

def solution(n):
    answer = []

    arr = [[0] * n for _ in range(n)]

    cnt = 1
    x, y, idx = -1, 0, 0
    dirx = [1, 0, -1]
    diry = [0, 1, -1]

    for i in range(n, 0, -1):
        for j in range(i):
            x += dirx[idx % 3]
            y += diry[idx % 3]
            arr[x][y] = cnt
            cnt += 1
        idx += 1

    for i in range(n):
        for data in arr[i]:
            if data != 0:
                answer.append(data)

    return answer
