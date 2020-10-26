def solution(n):
    # 00:00:00 ~ N:00:00
    # 사이에 3이 포함되면 무조건 count
    cnt = 0

    for i in range(n+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    cnt += 1

    return cnt

print(solution(5))
