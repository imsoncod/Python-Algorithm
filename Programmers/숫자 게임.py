def solution(A, B):
    ans = 0
    A.sort()
    B.sort()
    for i in A:
        for j in B:
            if i<j:
                ans+=1
                B.remove(j)
                break
    return ans
