def solution(p, loc):
    p = list(zip(list(range(0,len(p))),p))
    for idx in range(len(p)):
        for i in range(idx,len(p)):
            for j in range(idx,len(p)):
                if p[idx][1] < p[j][1]:
                    p.append(p[idx])
                    del p[idx]
                    break
    list1,list2 = zip(*p)
    return list1.index(loc)+1
