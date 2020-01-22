import heapq as heap
def solution(oper):
    h = []
    for i in oper:
        cmd = i.split(' ')
        if cmd[0]=='I':
            heap.heappush(h,int(cmd[1]))
        else:
            try:
                if cmd[1]=='1':
                    h.pop()
                else:
                    heap.heappop(h)
            except:
                continue
    return [max(h), heap.heappop(h)] if len(h)>0 else [0,0]
