from itertools import combinations as cb
def solution(nums):
    ans = 0
    for c in cb(nums,3):
        cs = sum(c)
        for i in range(2,cs):
            if cs%i==0:
                break
        else:
            ans+=1
    return ans
