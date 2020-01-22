ans = 999999
def dfs(begin,target,step,words):
    if begin == target:
        global ans
        ans = min(ans,step)
        return
    for i in words:
        temp = [w for w in words]
        cnt = 0
        for j in range(len(i)):
            if begin[j]==i[j]:
                cnt+=1
        if cnt==len(i)-1:
            temp.remove(i)
            dfs(i,target,step+1,temp)

def solution(begin, target, words):
    if target not in words:
        return 0
    dfs(begin,target,0,words)
    return ans
