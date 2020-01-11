def solution(g, p):
    ans = []
    a = list(zip(g,p))
    b = dict(zip(g,[0]*len(g)))
    for i in a:
        b[i[0]] += i[1] 
    b = [i[0] for i in sorted(b.items(), key=lambda x:-x[1])]
    for i in b:
        temp = {}
        for j in range(len(a)):
            if i == a[j][0]:
                temp[j] = a[j][1]
        temp = sorted(temp.items(),key=lambda x:(-x[1],x[0]))
        if(len(temp)!=1):
            ans.append(temp[0][0])
            ans.append(temp[1][0])
        else:
            ans.append(temp[0][0])
    return ans
