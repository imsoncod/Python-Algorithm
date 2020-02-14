def solution(cookie):
    ans = 0
    for m in range(len(cookie)-1):
        value1, idx1 = cookie[m], m
        value2, idx2 = cookie[m+1], m+1
        while True:
            if value1 == value2 and value1 > ans:
                ans = value1
            if value1 <= value2 and idx1 > 0:
                idx1 -= 1
                value1 += cookie[idx1]
            elif value1 >= value2 and idx2 < len(cookie)-1:
                idx2 += 1
                value2 += cookie[idx2]
            else:
                break
    return ans
