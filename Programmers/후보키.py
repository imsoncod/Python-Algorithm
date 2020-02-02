from itertools import combinations as cb
def solution(relation):
    ans = 0
    delete = []
    for idx in range(len(relation[0])):
        temp = []
        check = 1
        for i in relation:
            if i[idx] in temp:
                check = 0
                break
            temp.append(i[idx])
        if check:
            ans+=1
            delete.insert(0,idx)
    for i in delete:
        for j in relation:
            del j[i]
    storage = []
    for i in range(2,len(relation[0])+1):
        for j in list(cb([n for n in range(len(relation[0]))],i)):
            memory = []
            check = 1
            for row in relation:
                temp = []
                for col in j:
                    temp.append(row[col])
                if temp in memory:
                    check = 0
                    break
                memory.append(temp)
            if check:
                subset = 1
                j = set(j)
                for s in storage:
                    if set(s).issubset(j):
                        subset = 0
                        break
                if subset:
                    storage.append(j)
    return ans+len(storage)
