def solution(s):
    ans = 0
    for i in range(len(s)):
        for j in range(1,len(s)-i+1):
            temp = s[i:i+j]
            reverse = temp[::-1]
            if temp==reverse and ans < j:
                ans = j
    return ans
