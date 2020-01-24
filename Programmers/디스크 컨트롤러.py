def solution(jobs):
    n=len(jobs)
    ans = 0
    jobs = sorted(jobs, key=lambda x:(x[0],x[1]))
    start, time = jobs.pop(0)
    end = start+time
    ans = time
    while jobs:
        idx = 0
        for i in range(1,len(jobs)):
            if jobs[i][0]>=end:
                break
            else:
                if jobs[idx][1]>jobs[i][1]:
                    idx = i
        next = jobs.pop(idx)
        if next[0]<end:
            ans+=(end-next[0])+next[1]
            end+=next[1]
        else:
            ans+=next[1]
            end = sum(next)
    return ans//n
