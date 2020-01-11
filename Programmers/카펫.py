def solution(b, r):
    br = b+r
    for n in range(1,br+1):
        if br%n!=0:
            continue
        m = br//n
        if (m-2)*(n-2) == r:
            return [m, n]
    return 0
