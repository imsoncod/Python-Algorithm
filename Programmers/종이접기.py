def solution(n):
    ans = [0]
    for i in range(n-1):
        temp = []
        for j in range(len(ans)):
            if j%2==0:
                temp.append(0)
                temp.append(ans[j])
                temp.append(1)
            else:
                temp.append(ans[j])
        ans = [i for i in temp]       
    return ans
