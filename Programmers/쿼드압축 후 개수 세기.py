from collections import deque

def solution(arr):
    answer = [0, 0]

    q = deque()
    q.append((0, 0, len(arr)))

    while q:
        x, y, size = q.popleft()
        one, zero = True, True

        for i in range(x, x + size):
            for j in range(y, y + size):
                if arr[i][j] == 0:
                    one = False
                if arr[i][j] == 1:
                    zero = False
        if zero:
            answer[0] += 1
            continue
        if one:
            answer[1] += 1
            continue

        if size > 1:
            q.append((x, y, size // 2))
            q.append((x, y + size // 2, size // 2))
            q.append((x + size // 2, y, size // 2))
            q.append((x + size // 2, y + size // 2, size // 2))

    return answer
