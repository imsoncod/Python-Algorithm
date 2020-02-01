def solution(lines):
    logs = []
    for i in lines:
        a, b, c = i.split()
        h, m, s = b.split(':')
        end = (int(h)*3600 + int(m)*60 + float(s))*1000
        start = end-float(c[:-1])*1000+1 if end-float(c[:-1])*1000+1 > 0 else 0
        logs.append([start,end])
    max_ = 1
    #아래 알고리즘은 너무 어렵다...
    for i in range(len(logs)-1):
        cnt = 1
        for j in range(i+1,len(logs)):
            if logs[j][1]-logs[i][1] >= 4000:
                break
            if logs[j][0]-logs[i][1] < 1000:
                cnt+=1
        max_ = max(max_, cnt)
    return max_
